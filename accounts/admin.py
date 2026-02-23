from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "logo")



from django.contrib import admin
from .models import WebsiteContent

@admin.register(WebsiteContent)
class WebsiteContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


from django.contrib import admin
from .models import AboutContent


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ("title", "established_year", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


    from django.contrib import admin

from django.contrib import admin
from .models import WhyChooseUsSection, WhyChooseUsFeature

# Inline for Features inside a Section
class WhyChooseUsFeatureInline(admin.TabularInline):
    model = WhyChooseUsFeature
    extra = 1  # Number of extra blank forms
    fields = ("title", "description", "icon", "order")
    ordering = ("order",)

# Admin for Section
@admin.register(WhyChooseUsSection)
class WhyChooseUsSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    inlines = [WhyChooseUsFeatureInline]

# Optional: separate admin for features if you want
@admin.register(WhyChooseUsFeature)
class WhyChooseUsFeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "order")
    list_filter = ("section",)
    ordering = ("section", "order")



from django.contrib import admin
from .models import HowItWorksStep, HowItWorksSection

@admin.register(HowItWorksStep)
class StepAdmin(admin.ModelAdmin):
    list_display = ['step_number', 'title', 'is_active']
    list_editable = ['is_active']


@admin.register(HowItWorksSection)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']



from django.contrib import admin
from .models import FeaturedCourse

@admin.register(FeaturedCourse)
class FeaturedCourseAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "level", "is_active", "order")
    list_editable = ("is_active", "order")


from django.contrib import admin
from .models import StudentProject

@admin.register(StudentProject)
class StudentProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "student_name", "category", "order")
    list_editable = ("order",)



from django.contrib import admin
from .models import SuccessStory

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ["name", "role", "order"]
    list_editable = ["order"]


from django.contrib import admin
from .models import FooterLogo

@admin.register(FooterLogo)
class FooterLogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo', 'created_at']



  
  
from django.contrib import admin
from .models import EcosystemSectioned, EcosystemItemed

class EcosystemItemInline(admin.TabularInline):
    model = EcosystemItemed
    extra = 1

@admin.register(EcosystemSectioned)
class EcosystemSectionAdmin(admin.ModelAdmin):
    inlines = [EcosystemItemInline]



    
    # admin.py
from django.contrib import admin
from .models import CareerMen

@admin.register(CareerMen)
class CareerMenAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


from django.contrib import admin
from .models import Storyrole, StoryImage


class StoryImageInline(admin.TabularInline):
    model = StoryImage
    extra = 3   # show 3 upload fields


@admin.register(Storyrole)
class StoryroleAdmin(admin.ModelAdmin):
    list_display = ['name', 'role']
    inlines = [StoryImageInline]


@admin.register(StoryImage)
class StoryImageAdmin(admin.ModelAdmin):
    list_display = ['story']