from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Changed to OneToOneField
    # name = models.CharField(max_length=100, blank=True, null=True)
    clicks = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'
