from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests
from Cars.serializers import FindCarSerializer, AddCarSerializer, AddRateSerializer, CarSerializer, CarPopularSerializer
from Cars.models import Car


def is_model_valid(results: dict, model: str):
    # Chcecks is model is present inside of a (r)esponse message.
    for r in results:
        if model == r['Model_Name'].lower():
            return True
    return False


def save_if_new(request, model, make):
    # Saves car to db if it is not there yet.
    try:
        car = Car.objects.get(model_name=model, make=make)
        if car:
            return
    except Car.DoesNotExist:
        serializer = AddCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return


@api_view(['POST'])
def find_car(request):
    """ Client can find a car giving it's make and model in request.
    Then car is checked with 'https://vpic.nhtsa.dot.gov' website,
    and if exists, is saved into our database. """

    if request.method == 'POST':
        serializer = FindCarSerializer(data=request.data)
        if serializer.is_valid():
            # Make and model of a car client want`s to get info about.
            make = serializer.validated_data['make']
            model_name = serializer.validated_data['model_name']
            # Sending a request.
            url = "https://vpic.nhtsa.dot.gov/api//vehicles/GetModelsForMake/"
            params = {'format': 'json'}
            resp = requests.get(url + make, params=params)
            r = resp.json()     # dict
            # Results of the 'make' search from the site.
            results = r['Results']
            if is_model_valid(results, model_name):
                save_if_new(request, model_name, make)
                data = {'message': f"Car of '{make}' make and model '{model_name}' exists!"}
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                data = {'message': f"Car of '{make}' make and model '{model_name}' does not exist. Please, double-check it."}
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def rate_car(request):
    """ Client can rate cars, existing in database, from 1 to 5. """

    if request.method == 'POST':
        serializer = AddRateSerializer(data=request.data)
        if serializer.is_valid():
            model_name = serializer.validated_data['model_name']
            make = serializer.validated_data['make']
            try:
                car = Car.objects.get(model_name=model_name, make=make)
            except Car.DoesNotExist:
                data = {f"This car is not in our database yet."}
                return Response(status=status.HTTP_404_NOT_FOUND, data=data)
            car.rate(instance=car, validated_data=serializer.validated_data)
            data = {'message': f"Success! You have rated the car."}
            return Response(status=status.HTTP_201_CREATED, data=data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ListCars(APIView):
    """ List all cars saved in database [make, model, average rate]. """

    def get(self, request):
        cars = Car.objects.all().order_by('make')
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


class ListPopularCars(APIView):
    """ List all cars saved in database, but from most to less poluar.
     Polular - meaning - have the biggest amount of rates. """

    def get(self, request):
        cars = Car.objects.all().order_by('-rates_counter')
        serializer = CarPopularSerializer(cars, many=True)
        return Response(serializer.data)
