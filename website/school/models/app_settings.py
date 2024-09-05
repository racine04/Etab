from django.db import models

from base.models.helpers.namemodel import NamedDateTimeModel


# Create your models here.

class AppSettingModel(NamedDateTimeModel):
    smtp_server = models.CharField(max_length=255)
    smtp_port = models.IntegerField()
    smtp_username = models.CharField(max_length=255)
    smtp_password = models.CharField(max_length=255)

    def __str__(self):
        return f"Server: {self.smtp_server}, Port: {self.smtp_port}, Username:{self.smtp_username}"