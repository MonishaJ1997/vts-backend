from django.urls import path
from .views import ContactMapView
from .views import LearningEnvironmentView



urlpatterns = [
    path('contact-map/', ContactMapView.as_view()),
    path('learning-environment/', LearningEnvironmentView.as_view()),
]