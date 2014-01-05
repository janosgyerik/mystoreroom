from datetime import timedelta

from django.utils import timezone
from django.db import models


def tomorrow():
    return timezone.now() + timedelta(days=1)


class Item(models.Model):
    name = models.CharField(max_length=100)
    buy_dt = models.DateTimeField(default=timezone.now)
    expires_dt = models.DateTimeField(default=tomorrow)
    created_dt = models.DateTimeField(default=timezone.now, blank=True)
    updated_dt = models.DateTimeField(default=timezone.now, blank=True)
