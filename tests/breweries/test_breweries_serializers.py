import pytest

from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model

from breweries.serializers import BrewerySerializer
from breweries.models import Brewery


# class SerializerTest(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create(email='test@test.com')