from django.db import models

from base.models.helpers.namemodel import NamedDateTimeModel
from school.models.app_settings import AppSettingModel


# Create your models here.
class SchoolModel(NamedDateTimeModel):
    setting = models.OneToOneField(AppSettingModel, on_delete=models.SET_NULL, null=True, related_name="school_app_setting_id")
    name = models.CharField(max_length=255)
    url_logo= models.URLField(max_length=255)

    def __str__(self):
        return self.name