from django.shortcuts import render

# Create your views here.
# app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AboutImage
from .serializers import AboutImageSerializer

class AboutImageView(APIView):
    def get(self, request):
        image = AboutImage.objects.last()
        serializer = AboutImageSerializer(image, context={"request": request})
    
    
        return Response(serializer.data)
    




    from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MissionVision
from .serializers import MissionVisionSerializer

class MissionVisionView(APIView):
    def get(self, request):
        data = MissionVision.objects.all()
        serializer = MissionVisionSerializer(
            data, many=True, context={"request": request}
        )
        return Response(serializer.data)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EcosystemSection

@api_view(['GET'])
def ecosystem_view(request):
    section = EcosystemSection.objects.first()

    data = {
        "title": section.title,
        "center_text": section.center_text,
        "left_image": section.left_image.url,
        "items": []
    }

    for item in section.items.all():
        data["items"].append({
            "name": item.name,
            "logo": item.logo.url,
            "point1": item.point1,
            "point2": item.point2,
            "site_link": item.site_link
        })

    return Response(data)

from django.http import JsonResponse
from .models import ValueCard

def value_cards_api(request):
    cards = ValueCard.objects.all()
    data = []
    for card in cards:
        data.append({
            "id": card.id,
            "title": card.title,
            "icon": card.icon.url,  # URL to icon image
            "bullets": card.bullets
        })
    return JsonResponse(data, safe=False)




from django.http import JsonResponse
from .models import TrainingStep

def training_steps_api(request):
    steps = TrainingStep.objects.all().order_by('journey_name', 'order')
    data = []
    for step in steps:
        data.append({
            "id": step.id,
            "title": step.title,
            "description": step.description,
            "image": step.image.url,
            "journey_name": step.journey_name
        })
    return JsonResponse(data, safe=False)




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WhoCanJoin
from .serializers import WhoCanJoinSerializer

class WhoCanJoinList(APIView):
    def get(self, request):
        items = WhoCanJoin.objects.all()
        serializer = WhoCanJoinSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)
    


    # views.py
from rest_framework import generics
from .models import CareerPerson
from .serializers import CareerPersonSerializer

class CareerPersonView(generics.ListAPIView):
    queryset = CareerPerson.objects.all()
    serializer_class = CareerPersonSerializer


    