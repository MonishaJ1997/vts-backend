from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ContactMap
from .serializers import ContactMapSerializer

class ContactMapView(APIView):
    def get(self, request):
        obj = ContactMap.objects.last()
        serializer = ContactMapSerializer(obj)
        return Response(serializer.data)
    


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LearningEnvironment
from .serializers import LearningEnvironmentSerializer

class LearningEnvironmentView(APIView):
    def get(self, request):
        data = LearningEnvironment.objects.all()
        serializer = LearningEnvironmentSerializer(data, many=True)
        return Response(serializer.data)