from rest_framework import status
from rest_framework.test import APITestCase
from .models import Car


class Cars(APITestCase):

    def test_find_car_with_make_and_model_passes(self):
        data = {"make": "tesla", "model_name": "model 3"}
        response = self.client.post('/cars/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_find_car_without_model_fails(self):
        data = {"make": "tesla"}
        response = self.client.post('/cars/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_find_car_without_make_fails(self):
        data = {"model_name": "model s"}
        response = self.client.post('/cars/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_find_car_without_data_fails(self):
        response = self.client.post('/cars/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_find_car_with_wrong_data_fails(self):
        data = {"make": "test", "model": "test2"}
        response = self.client.post('/cars/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CarsRate(APITestCase):

    def test_add_rate_passes(self):
        """ Create an object first """
        Car.objects.create(make="tesla", model_name="model 3")

        data = {"make": "tesla", "model_name": "model 3", "rate": "5"}
        response = self.client.post('/rate/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_rate_without_rate_fails(self):
        """ Create an object first """
        Car.objects.create(make="honda", model_name="civic")

        data = {"make": "honda", "model_name": "civic"}
        response = self.client.post('/rate/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_rate_with_wrong_value_fails(self):
        """ Create an object first """
        Car.objects.create(make="tesla", model_name="model 3")

        data = {"make": "tesla", "model_name": "model 3", "rate": "10"}
        response = self.client.post('/rate/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_rate_without_model_fails(self):
        """ Create an object first """
        Car.objects.create(make="tesla", model_name="model 3")

        data = {"make": "tesla", "rate": "4"}
        response = self.client.post('/rate/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_rate_with_wrong_model_fails(self):
        """ Create an object first """
        Car.objects.create(make="tesla", model_name="model 3")

        data = {"make": "tesla", "model_name": "test", "rate": "4"}
        response = self.client.post('/rate/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_rate_without_make_fails(self):
        """ Create an object first """
        Car.objects.create(make="honda", model_name="civic")

        data = {"model_name": "civic", "rate": "4"}
        response = self.client.post('/rate/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_rate_with_wrong_make_fails(self):
        """ Create an object first """
        Car.objects.create(make="honda", model_name="civic")

        data = {"make": "test", "model_name": "civic", "rate": "4"}
        response = self.client.post('/rate/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_rate_with_wrong_method_fails(self):
        """ Create an object first """
        Car.objects.create(make="tesla", model_name="model s")

        params = {"make": "tesla", "model_name": "model s", "rate": "5"}
        response = self.client.get('/rate/', params)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class CarsLists(APITestCase):

    def test_list_cars_passes(self):
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_cars_with_carmake_order_passes(self):
        """ Create objects to work with. List will be ordered by 'make'!"""
        Car.objects.create(make="tesla", model_name="model s")
        Car.objects.create(make="honda", model_name="civic")
        Car.objects.create(make="tesla", model_name="model 3")
        Car.objects.create(make="tesla", model_name="model y")

        response = self.client.get('/cars/')

        self.assertEqual(response.data[0]["make"], "honda")
        self.assertEqual(response.data[1]["make"], "tesla")
        self.assertEqual(response.data[2]["make"], "tesla")
        self.assertEqual(response.data[3]["make"], "tesla")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PopularCarsLists(APITestCase):

    def test_list_popular_cars_passes(self):
        response = self.client.get('/popular/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_popular_cars_with_wrong_method_fails(self):
        response = self.client.post('/popular/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_popular_cars_with_ratescount_order_passes(self):
        """ Create objects to work with. List will be ordered with 'rates_count'! """
        Car.objects.create(make="tesla", model_name="model s", rates_counter=3, total_rates=13, average_rate=4.3)
        Car.objects.create(make="tesla", model_name="model 3", rates_counter=2, total_rates=10, average_rate=5)
        Car.objects.create(make="honda", model_name="civic", rates_counter=5, total_rates=10, average_rate=2)
        Car.objects.create(make="tesla", model_name="model y", rates_counter=1, total_rates=4, average_rate=4)

        response = self.client.get('/popular/')

        self.assertEqual(response.data[0]["make"], "honda")
        self.assertEqual(response.data[0]["model_name"], "civic")
        self.assertEqual(response.data[1]["make"], "tesla")
        self.assertEqual(response.data[1]["model_name"], "model s")
        self.assertEqual(response.data[2]["make"], "tesla")
        self.assertEqual(response.data[2]["model_name"], "model 3")
        self.assertEqual(response.data[3]["make"], "tesla")
        self.assertEqual(response.data[3]["model_name"], "model y")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
