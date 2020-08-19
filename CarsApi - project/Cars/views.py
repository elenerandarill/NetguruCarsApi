import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from Cars.serializers import FindCarSerializer, AddCarSerializer
from Cars.models import Car


def is_model_valid(results: dict, model: str):
    for r in results:
        if model == r['Model_Name'].lower():
            return True
    return False


def save_if_new(request, model, make):
    # Save car to db if it is not there yet.
    try:
        car = Car.objects.get(model_name=model)
        if car:
            return
    except Car.DoesNotExist:
        serializer = AddCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return


@api_view(['POST'])
def find_car(request):
    if request.method == 'POST':
        serializer = FindCarSerializer(data=request.data)
        if serializer.is_valid():
            # Make and model of a car client want`s to get info about.
            make = serializer.validated_data['make']
            model_name = serializer.validated_data['model_name']

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
    return Response(status=status.HTTP_400_BAD_REQUEST)

