from django.urls import path
from .views import ProductApi, StudentApi


urlpatterns = [
    path('api', ProductApi.as_view()),
    path('students', StudentApi.as_view()),
]
