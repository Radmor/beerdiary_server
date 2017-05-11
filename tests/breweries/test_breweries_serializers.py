import pytest

from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import exceptions


from breweries.serializers import BrewerySerializer
from breweries.models import Brewery


class BreweriesSerializerTest(TestCase):
    def setUp(self):
        self.no_data = {

        }

        self.empty_name = {
            "name": "",
        }
        
        self.correct_name_no_overall_and_note = {
            "name": "name1"

        }

        self.all_correct = {
            "name": "name1",
            "overall": "1",
            "note": "note"
        }

        self.overall_min_value = {
            "name": "name1",
            "overall": "0",
        }

        self.overall_max_value = {
            "name": "name1",
            "overall": "7",
        }

        self.overall_float_value = {
            "name": "name1",
            "overall": "1.8",
        }

        self.overall_string_value = {
            "name": "name1",
            "overall": "name",
        }

    def test_no_data(self):
        serializer = BrewerySerializer(data=self.no_data)
        with pytest.raises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
        assert any('required' in error for error in serializer.errors['name'])

    def test_empty_name(self):
        serializer = BrewerySerializer(data=self.empty_name)
        with pytest.raises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
        assert any('blank' in error for error in serializer.errors['name'])

    def test_correct_name_no_overall_and_note(self):
        serializer = BrewerySerializer(data=self.correct_name_no_overall_and_note)
        serializer.is_valid(raise_exception=True)

    def test_all_correct(self):
        serializer = BrewerySerializer(data=self.all_correct)
        serializer.is_valid(raise_exception=True)

    def test_overall_min_value(self):
        serializer = BrewerySerializer(data=self.overall_min_value)
        with pytest.raises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
        assert any('valid choice' in error for error in serializer.errors['overall'])

    def test_overall_max_value(self):
        serializer = BrewerySerializer(data=self.overall_max_value)
        with pytest.raises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
        assert any('valid choice' in error for error in serializer.errors['overall'])

    def test_overall_float_value(self):
        serializer = BrewerySerializer(data=self.overall_float_value)
        with pytest.raises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
        assert any('valid choice' in error for error in serializer.errors['overall'])

    def test_overall_string_value(self):
        serializer = BrewerySerializer(data=self.overall_string_value)
        with pytest.raises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
        assert any('valid choice' in error for error in serializer.errors['overall'])


