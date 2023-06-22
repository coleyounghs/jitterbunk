import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=50)
    photo = models.CharField(max_length=64)


class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    time = models.DateTimeField()