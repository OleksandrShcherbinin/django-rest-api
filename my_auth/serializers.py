from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from requests.exceptions import HTTPError
from pyhunter import PyHunter
import clearbit

from .models import Profile

hunter = PyHunter(settings.PY_HUNTER_KEY)
clearbit.key = settings.CLEARBIT_KEY


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name',
                  'last_name')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    def validate(self, attrs):
        try:
            email = hunter.email_verifier(attrs.get('email', None))
        except HTTPError as error:
            email = {}
            print(type(error), error)
        if email.get('status') == 'invalid' \
                or email.get('result') == "undeliverable":
            raise serializers.ValidationError(
                {"email": "Not valid email, please give us your real email"}
            )
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        try:
            response = clearbit.Enrichment.find(email=validated_data['email'],
                                                stream=True)
        except HTTPError:
            response = {}

        if response:
            Profile.objects.create(info=response, user=user)

        user.set_password(validated_data['password'])
        user.save()

        return user
