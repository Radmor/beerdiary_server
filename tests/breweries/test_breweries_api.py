import pytest

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from breweries.models import Brewery

class APITest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='test@test.com')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.valid_data = {
            'name':'name',
        }
        self.valid_data_response = {
            'name':'name',
            'overall': None,
            'note': ''
        }

        self.with_same_name1 = {
            "name": "name1",
            "overall": "1",
        }

        self.with_same_name2 = {
            "name": "name1",
            "overall": "2",
        }

    def getDataWithID(self, data, id):
        data.update({"id":id})
        return data

    def create_brewery(self):
        self.client.post(reverse('breweries-list'), data=self.valid_data)
        return Brewery.objects.get(name='name').id

    def test_post(self):
        response = self.client.post(reverse('breweries-list'), data=self.valid_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Brewery.objects.filter(name='name')

    def test_get_list(self):
        id = self.create_brewery()
        response = self.client.get(reverse('breweries-list'))
        assert response.status_code == status.HTTP_200_OK
        valid_data_response = self.getDataWithID(self.valid_data_response, id)
        assert response.data == [dict(valid_data_response)]

    def test_get_detail(self):
        brewery_id = self.create_brewery()
        response = self.client.get(reverse('breweries-detail',args=(brewery_id,)))
        assert response.status_code == status.HTTP_200_OK
        valid_data_response = self.getDataWithID(self.valid_data_response, brewery_id)
        assert response.data == valid_data_response

    def test_delete(self):
        brewery_id = self.create_brewery()
        response = self.client.delete(reverse('breweries-detail', args=(brewery_id,)))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Brewery.objects.filter(id=brewery_id)
