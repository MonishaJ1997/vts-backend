from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None





from rest_framework import serializers
from .models import Coursedetails, CourseTechnology

class CourseTechnologySerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(read_only=True)

    class Meta:
        model = CourseTechnology
        fields = ["id", "name", "icon"]

class CourseDetailSerializer(serializers.ModelSerializer):
    video_thumbnail = serializers.ImageField(read_only=True)
    technologies = CourseTechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Coursedetails
        fields = ["id", "title", "video_thumbnail", "technologies"]



from rest_framework import serializers
from .models import PaymentMethod

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ["id", "title", "method_type", "icon"]