from rest_framework import serializers
from .models import Section

class SimpleSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['name','image']
