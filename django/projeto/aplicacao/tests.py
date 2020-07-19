import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer

class EnderecoTestCase(APITestCase):
    def test_get(self):
        data = {}