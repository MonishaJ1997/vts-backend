from django.urls import path
from .views import CompanyLogoView
from .views import WebsiteContentView
from .views import AboutContentView
from .views import WhyChooseUsAPIView
from .views import HowItWorksAPI
from .views import FeaturedCourseAPI
from .views import student_projects
from .views import SuccessStoryListView
from .views import FooterLogoView
from .views import ecosystemed_view
from .views import CareerMenView
from .views import StoryroleView

urlpatterns = [
    path("logo/", CompanyLogoView.as_view()),
    path('website-content/', WebsiteContentView.as_view() ),
    path("about-content/", AboutContentView.as_view(), name="about-content"),
    path("why-choose-us/", WhyChooseUsAPIView.as_view(), name="why-choose-us"),
    path('api/how-it-works/', HowItWorksAPI.as_view()),
    path("api/featured-courses/", FeaturedCourseAPI.as_view()),
     path("api/student-projects/", student_projects),
     path("api/success-stories/", SuccessStoryListView.as_view(), name="success-stories"),
path('api/footer-logo/', FooterLogoView.as_view(), name='footer-logo'),
 path('api/ecosystemed/', ecosystemed_view, name='ecosystem'),
path('api/career-men/', CareerMenView.as_view(), name='career-men'),

    path('api/storyrole/', StoryroleView.as_view(), name='storyrole'),
]




