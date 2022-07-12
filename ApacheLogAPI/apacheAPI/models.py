from django.db import models


class Log(models.Model):
    ip = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=255)
    request = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    bytes = models.CharField(max_length=255)
    referer = models.CharField(max_length=255)
    useragent = models.CharField(max_length=255)
