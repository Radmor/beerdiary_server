import pytest

from django.test import TestCase
from rest_framework.exceptions import ValidationError


from styles.serializers import StyleSerializer



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