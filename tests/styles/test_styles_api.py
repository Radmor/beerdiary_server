import pytest

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from styles.models import Style
from styles.serializers import StyleSerializer

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


    def getDataWithID(self, id):
        data = self.data
        data.update({"id":id})
        return data

    def test_post(self):
        response = self.client.post(reverse('styles-list'), self.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Style.objects.filter(name="name")

    def test_get_list(self):
        id = self.create_style()
        response = self.client.get(reverse('styles-list'))
        assert response.status_code == status.HTTP_200_OK
        response_detail_data = self.getDataWithID(id)
        assert response.data == [dict(response_detail_data)]

    def test_get_detail(self):
        id = self.create_style()
        response = self.client.get(reverse('styles-detail', args=(id,)))
        assert response.status_code == status.HTTP_200_OK
        response_data = self.getDataWithID(id)
        assert response.data == response_data

    def test_delete(self):
        id = self.create_style()
        response = self.client.delete(reverse('styles-detail', args=(id,)))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Style.objects.filter(id=id)
        