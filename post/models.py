from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='posts'
                             )

    def __str__(self):
        return self.title


class BotContentSource(models.Model):

    name = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name
