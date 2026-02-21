from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category')

        if category and category != "All":
            queryset = queryset.filter(category=category)

        return queryset

    def get_serializer_context(self):
        return {"request": self.request}

from rest_framework import generics
from .models import Coursedetails
from .serializers import CourseDetailSerializer

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Coursedetails.objects.all()
    serializer_class = CourseDetailSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer

class PaymentMethodList(APIView):
    def get(self, request):
        qs = PaymentMethod.objects.filter(is_active=True)
        serializer = PaymentMethodSerializer(qs, many=True)
        return Response(serializer.data)