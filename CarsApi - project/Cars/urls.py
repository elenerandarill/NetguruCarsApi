from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('cars/', views.cars),
    path('rate/', views.rate_car),
    # path('cars/', views.ListCars.as_view()),
    path('popular/', views.ListPopularCars.as_view())
])


