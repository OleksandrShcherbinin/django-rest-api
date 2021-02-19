from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post
from .serializers import PostSerializer


def authenticate_from_token(request):
    jwt_object = JWTAuthentication()
    header = jwt_object.get_header(request)
    raw_token = jwt_object.get_raw_token(header)
    validated_token = jwt_object.get_validated_token(raw_token)
    user = jwt_object.get_user(validated_token)
    request.data["user"] = user.id
    return request


class PostAPIView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request = authenticate_from_token(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request = authenticate_from_token(request)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
