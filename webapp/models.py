from django.db import models

# Create your models here.
class ClickCount(models.Model):
    count = models.IntegerField(default=0)