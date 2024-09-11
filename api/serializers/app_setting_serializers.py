from rest_framework import serializers

from school.models.app_settings import AppSettingModel
from user.models.user import UserModel


class AppSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSettingModel
        fields = "__all__"