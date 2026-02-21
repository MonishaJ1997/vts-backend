# app/urls.py
from django.urls import path
from .views import AboutImageView
from .views import MissionVisionView
from .views import ecosystem_view
from .views import value_cards_api
from . import views
from .views import training_steps_api
from .views import WhoCanJoinList
from .views import CareerPersonView

urlpatterns = [
    path("about-image/", AboutImageView.as_view(), name="about-image"),
    path("mission-vision/", MissionVisionView.as_view(), name="mission-vision"),
    path('ecosystem/', ecosystem_view, name='ecosystem'),
   path('value-cards/', value_cards_api, name='value-cards'),
    path('training-steps/', training_steps_api, name='training-steps'),
    path('who-can-join/', WhoCanJoinList.as_view(), name='who-can-join'),
    path('career-person/', CareerPersonView.as_view(), name='career-person'),

]