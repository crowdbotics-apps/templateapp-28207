from django.conf import settings
from django.db import models


class Login(models.Model):
    "Generated Model"
    user_id = models.IntegerField()
    username = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    password = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
