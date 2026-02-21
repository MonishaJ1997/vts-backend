from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactMap

@admin.register(ContactMap)
class ContactMapAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']


    from django.contrib import admin
from .models import LearningEnvironment

@admin.register(LearningEnvironment)
class LearningEnvironmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']