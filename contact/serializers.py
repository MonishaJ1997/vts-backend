from rest_framework import serializers
from .models import ContactMap

class ContactMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMap
        fields = ['id', 'map_image']





from rest_framework import serializers
from .models import LearningEnvironment

class LearningEnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningEnvironment
        fields = ['id', 'image']