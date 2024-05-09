from django.conf import settings
from django.db import models


# class ClickCount(models.Model):
#     count = models.IntegerField(default=0)
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False) 

class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=100, default="username")
    password = models.CharField(max_length=100, default="password")
    clicks = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'
