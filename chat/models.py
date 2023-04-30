from django.db import models
# from django.contrib.auth import get_user_model
from accounts.models import User
# Create your models here.


class Chat(models.Model):
    roomname = models.CharField(blank=True, max_length=255)
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.roomname


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    related_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def last_message(self, roomname):
        # return Message.objects.order_by("-timestamp").all()
        return Message.objects.filter(related_chat__roomname=roomname)

    def __str__(self):
        return self.author.username