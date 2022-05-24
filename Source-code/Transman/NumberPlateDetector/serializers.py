from rest_framework import serializers
from .models import carEntry

class carEntrySerializers(serializers.ModelSerializer):
     class Meta:
         model=carEntry
         fields = '__all__'
