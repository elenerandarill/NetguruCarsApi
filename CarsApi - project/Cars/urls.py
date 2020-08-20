from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('cars/find/', views.find_car),
    path('cars/rate/', views.rate_car),
])


