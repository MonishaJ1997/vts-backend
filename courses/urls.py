from django.urls import path
from .views import CourseListView
from .views import CourseDetailView
from .views import PaymentMethodList

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path("courses/<int:pk>/", CourseDetailView.as_view()),
   path("payment-methods/", PaymentMethodList.as_view()),

]
