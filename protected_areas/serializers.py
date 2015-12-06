from rest_framework import serializers
from .models import BaseProtectedArea


class BaseProtectedAreaSerializers(serializers.ModelSerializer):

    class Meta:
        model = BaseProtectedArea
        exclude = ['geometry', ]
