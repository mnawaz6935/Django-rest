from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer, StudentSerializer
from .models import Product, Student


class ProductApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StudentApi(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
