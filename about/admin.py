from django.contrib import admin

# Register your models here.
# app/admin.py
from django.contrib import admin
from .models import AboutImage

@admin.register(AboutImage)
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ("title",)




# app/admin.py
from django.contrib import admin
from .models import MissionVision

@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ("type",)




from django.contrib import admin
from .models import EcosystemSection, EcosystemItem

class EcosystemItemInline(admin.TabularInline):
    model = EcosystemItem
    extra = 1

@admin.register(EcosystemSection)
class EcosystemSectionAdmin(admin.ModelAdmin):
    inlines = [EcosystemItemInline]



from django.contrib import admin
from .models import ValueCard

@admin.register(ValueCard)
class ValueCardAdmin(admin.ModelAdmin):
    list_display = ('title',)




from django.contrib import admin
from .models import TrainingStep

class TrainingStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'journey_name', 'order')
    ordering = ('journey_name', 'order')

admin.site.register(TrainingStep, TrainingStepAdmin)



from django.contrib import admin
from .models import WhoCanJoin

@admin.register(WhoCanJoin)
class WhoCanJoinAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'image')





    # admin.py
from django.contrib import admin
from .models import CareerPerson

@admin.register(CareerPerson)
class CareerPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')