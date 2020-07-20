import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Endereco
from .serializers import EnderecoSerializer
from .views import EnderecoView

class EnderecoTestCase(APITestCase):
    def test_post(self):
        data = {
            "streetName": "rua teste",
            "number" : "teste",
            "complement" : "teste",
            "neighbourhood" : "teste",
            "city" : "teste",
            "state" : "teste",
            "country" : "teste",
            "zipcode" : "teste",
            "latitude" : "teste",
            "longitude" : "teste"
        }
        response = self.client.post("/endereco/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        response = self.client.get(reverse("endereco-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get(self):
        response = self.client.get(reverse("endereco-list"), kwargs={"pk": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        data = {
            "streetName": "rua teste",
            "number" : "teste",
            "complement" : "teste",
            "neighbourhood" : "teste",
            "city" : "teste",
            "state" : "teste",
            "country" : "teste",
            "zipcode" : "teste",
            "latitude" : "teste",
            "longitude" : "teste"
        }
        post_teste = self.client.post("/endereco/", data)
        teste_id = json.loads((post_teste.content)).get("id")
        data = {
            "streetName": "rua teste2",
            "number" : "teste",
            "complement" : "teste",
            "neighbourhood" : "teste",
            "city" : "teste",
            "state" : "teste",
            "country" : "teste",
            "zipcode" : "teste",
            "latitude" : "teste",
            "longitude" : "teste"
        }
        response = self.client.put('/endereco/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        data = {
            "streetName": "rua teste",
            "number" : "teste",
            "complement" : "teste",
            "neighbourhood" : "teste",
            "city" : "teste",
            "state" : "teste",
            "country" : "teste",
            "zipcode" : "teste",
            "latitude" : "teste",
            "longitude" : "teste"
        }
        post_teste = self.client.post("/endereco/", data)
        teste_id = json.loads((post_teste.content)).get("id")

        response = self.client.delete('/endereco/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)