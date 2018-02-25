from django.db import models


class Resource(models.Model):
    hostname = models.CharField('hostname', max_length=256, primary_key=True)
    is_available = models.BooleanField('is_available', blank=True, default=True)
    locking_user = models.CharField('locking_user', blank=True, max_length=256)

    def __str__(self):
        return self.hostname
