from rest_framework import serializers
from .models import Company

class CompanyLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["logo"]


from rest_framework import serializers
from .models import WebsiteContent


class WebsiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteContent
        fields = "__all__"



from rest_framework import serializers
from .models import AboutContent

class AboutContentSerializer(serializers.ModelSerializer):
    about_image = serializers.SerializerMethodField()

    class Meta:
        model = AboutContent
        fields = "__all__"

    def get_about_image(self, obj):
        request = self.context.get("request")
        if obj.about_image:
            return request.build_absolute_uri(obj.about_image.url)
        return None

from rest_framework import serializers
from .models import WhyChooseUsSection, WhyChooseUsFeature

class WhyChooseUsFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUsFeature
        fields = ["id", "title", "description", "icon", "order"]

class WhyChooseUsSectionSerializer(serializers.ModelSerializer):
    features = WhyChooseUsFeatureSerializer(many=True, read_only=True)
    left_image = serializers.ImageField()

    class Meta:
        model = WhyChooseUsSection
        fields = ["id", "title", "description", "left_image", "features"]


from rest_framework import serializers
from .models import HowItWorksStep, HowItWorksSection

class StepSerializer(serializers.ModelSerializer):
    icon_image = serializers.SerializerMethodField()

    class Meta:
        model = HowItWorksStep
        fields = '__all__'

    def get_icon_image(self, obj):
        request = self.context.get('request')
        if obj.icon_image:
            return request.build_absolute_uri(obj.icon_image.url)
        return None


class SectionSerializer(serializers.ModelSerializer):
    student_image = serializers.SerializerMethodField()

    class Meta:
        model = HowItWorksSection
        fields = '__all__'

    def get_student_image(self, obj):
        request = self.context.get('request')
        if obj.student_image:
            return request.build_absolute_uri(obj.student_image.url)
        return None




from rest_framework import serializers
from .models import FeaturedCourse

class FeaturedCourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = FeaturedCourse
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


from rest_framework import serializers
from .models import StudentProject

class StudentProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProject
        fields = "__all__"





from rest_framework import serializers
from .models import SuccessStory

class SuccessStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStory
        fields = "__all__"



from rest_framework import serializers
from .models import FooterLogo

class FooterLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLogo
        fields = ['id', 'logo']





        
from rest_framework import serializers
from .models import EcosystemSectioned, EcosystemItemed

class EcosystemItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcosystemItemed
        fields = '__all__'

class EcosystemSectionSerializer(serializers.ModelSerializer):
    items = EcosystemItemSerializer(many=True, read_only=True)

    class Meta:
        model = EcosystemSectioned
        fields = '__all__'



       # serializers.py
from rest_framework import serializers
from .models import CareerMen

class CareerMenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerMen
        fields = ['id', 'name', 'image']     



from rest_framework import serializers
from .models import Storyrole

class StoryroleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStory
        fields = '__all__'