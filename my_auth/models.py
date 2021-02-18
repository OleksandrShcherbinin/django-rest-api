from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField


class Profile(models.Model):
    info = JSONField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.__class__.__name__} - {self.user}"
