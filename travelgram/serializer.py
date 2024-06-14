from .models import *
from rest_framework import serializers

class travelgramSerializers(serializers.ModelSerializer):
    Place_img=serializers.ImageField(required=False)

    class Meta:
        model=Travelgram
        fields='__all__'