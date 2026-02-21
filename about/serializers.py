# app/serializers.py
from rest_framework import serializers
from .models import AboutImage

class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = ["id", "image"]




from rest_framework import serializers
from .models import MissionVision

class MissionVisionSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = MissionVision
        fields = ["type", "icon"]

    def get_icon(self, obj):
        request = self.context.get("request")
        if obj.icon:
            return request.build_absolute_uri(obj.icon.url)
        return None


from rest_framework import serializers
from .models import EcosystemSection, EcosystemItem

class EcosystemItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcosystemItem
        fields = '__all__'

class EcosystemSectionSerializer(serializers.ModelSerializer):
    items = EcosystemItemSerializer(many=True, read_only=True)

    class Meta:
        model = EcosystemSection
        fields = '__all__'


from rest_framework import serializers
from .models import ValueCard

class ValueCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueCard
        fields = ['id', 'title', 'icon', 'bullets']




# serializers.py
from rest_framework import serializers
from .models import TrainingStep

class TrainingStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingStep
        fields = ['id', 'title', 'description', 'image', 'order', 'journey_name']


from rest_framework import serializers
from .models import WhoCanJoin

class WhoCanJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoCanJoin
        fields = ['id', 'name', 'image', 'color']  




        # serializers.py
from rest_framework import serializers
from .models import CareerPerson

class CareerPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPerson
        fields = ['id', 'name', 'image']     


