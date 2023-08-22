from rest_framework import serializers
from .models import CookieStand

class CookieStand_serializers(serializers.ModelSerializer):
    class Meta:
        model=CookieStand
        fields="__all__"