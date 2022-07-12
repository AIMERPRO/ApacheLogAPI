from rest_framework import serializers

from apacheAPI.models import Log


class LogFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"