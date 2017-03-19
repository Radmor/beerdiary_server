import pytest

from django.test import TestCase
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

from styles.serializers import StyleSerializer
from styles.models import Style


class SerializerTest(TestCase):
    def setUp(self):
        self.empty_data = {
        }

        self.data_with_empty_name = {
            "name":""
        }

        self.data_with_proper_name = {
            "name":"name"
        }

    def test_empty_data(self):
        serializer = StyleSerializer(data=self.empty_data)
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
        assert any('required' in error for error in serializer.errors['name'])

    def test_empty_name(self):
        serializer = StyleSerializer(data=self.data_with_empty_name)
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
        assert any('blank' in error for error in serializer.errors['name'])

    def test_proper_name(self):
        serializer = StyleSerializer(data=self.data_with_proper_name)
        serializer.is_valid(raise_exception=True)


class APIFlowTest(TestCase):
    def create_style(self):
        self.client.post(reverse('styles-list'), self.data)
        return Style.objects.get(name="name").id
    def setUp(self):
        self.data = {
            "name":"name"
        }
        self.user = get_user_model().objects.create(email='test@test.com')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    def test_post(self):
       
        response = self.client.post(reverse('styles-list'), self.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Style.objects.filter(name="name")

    def test_get_list(self):
        self.client.post(reverse('styles-list'), self.data)
        response = self.client.get(reverse('styles-list'))
        assert response.status_code == status.HTTP_200_OK
        assert response.data == [self.data]
        
    def test_get_detail(self):
        id = self.create_style()
        response = self.client.get(reverse('styles-detail', args=(id,)))
        assert response.status_code == status.HTTP_200_OK
        assert response.data == self.data

    def test_delete(self):
        id = self.create_style()
        response = self.client.delete(reverse('styles-detail', args=(id,)))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Style.objects.filter(id=id)