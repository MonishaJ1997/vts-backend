from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company
from .serializers import CompanyLogoSerializer

class CompanyLogoView(APIView):
    def get(self, request):
        company = Company.objects.first()
        serializer = CompanyLogoSerializer(company)
        return Response(serializer.data)



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WebsiteContent
from .serializers import WebsiteContentSerializer

class WebsiteContentView(APIView):
    def get(self, request):
        content = WebsiteContent.objects.first()
        serializer = WebsiteContentSerializer(content, context={"request": request})
        return Response(serializer.data)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AboutContent
from .serializers import AboutContentSerializer

class AboutContentView(APIView):
    def get(self, request):
        content = AboutContent.objects.first()
        serializer = AboutContentSerializer(content, context={"request": request})
        return Response(serializer.data)



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HowItWorksStep, HowItWorksSection
from .serializers import StepSerializer, SectionSerializer

class HowItWorksAPI(APIView):

    def get(self, request):
        steps = HowItWorksStep.objects.filter(is_active=True)
        section = HowItWorksSection.objects.first()

        return Response({
            "section": SectionSerializer(section, context={'request': request}).data,
            "steps": StepSerializer(steps, many=True, context={'request': request}).data
        })
    

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FeaturedCourse
from .serializers import FeaturedCourseSerializer

class FeaturedCourseAPI(APIView):

    def get(self, request):
        courses = FeaturedCourse.objects.filter(is_active=True)
        serializer = FeaturedCourseSerializer(courses, many=True, context={"request": request})
        return Response(serializer.data)
    

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentProject
from .serializers import StudentProjectSerializer

@api_view(["GET"])
def student_projects(request):
    projects = StudentProject.objects.all()
    serializer = StudentProjectSerializer(projects, many=True)
    return Response(serializer.data)



from rest_framework.generics import ListAPIView
from .models import SuccessStory
from .serializers import SuccessStorySerializer

class SuccessStoryListView(ListAPIView):
    queryset = SuccessStory.objects.all()
    serializer_class = SuccessStorySerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WhyChooseUsSection
from .serializers import WhyChooseUsSectionSerializer

class WhyChooseUsAPIView(APIView):
    def get(self, request):
        section = WhyChooseUsSection.objects.prefetch_related('features').first()
        if not section:
            return Response({"detail": "No content found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = WhyChooseUsSectionSerializer(section)
        return Response(serializer.data)




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FooterLogo
from .serializers import FooterLogoSerializer

class FooterLogoView(APIView):
    def get(self, request):
        logo = FooterLogo.objects.last()  # get latest logo
        serializer = FooterLogoSerializer(logo)
        return Response(serializer.data)
    



    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EcosystemSectioned

@api_view(['GET'])
def ecosystemed_view(request):
    section = EcosystemSectioned.objects.first()

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
            
            "site_link": item.site_link
        })

    return Response(data)



    # views.py
from rest_framework import generics
from .models import CareerMen
from .serializers import CareerMenSerializer

class CareerMenView(generics.ListAPIView):
    queryset = CareerMen.objects.all()
    serializer_class = CareerMenSerializer



from rest_framework import generics
from .models import Storyrole
from .serializers import StoryroleSerializer

class StoryroleView(generics.ListAPIView):
    queryset = Storyrole.objects.all()
    serializer_class = StoryroleSerializer