# Generated by Django 5.0.4 on 2024-05-09 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_clickcount_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clickcount',
            name='user',
        ),
    ]