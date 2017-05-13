import pytest
from django.test import TestCase

from ratebeer.utils import RateBeerClient
from ratebeer.utils import RateBeerReview
from ratebeer.utils import APIBadRequestException, APINotFoundException

class RateBeerReviewMock:
    def __init__(self, beer=None, rating=None, review=None, id=None):
        self.id = id
        self.beer = beer
        self.rating = rating
        self.review = review

class MockedResponse:
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code

class MockedApiClient:
    def __init__(self, reviews=[]):
        self.reviews = reviews
        self.id = 0

    def reset(self):
        self.reviews = []
        self.id = 0

    def get_with_id(self, id):
        for review in self.reviews:
            if review.get('id') == id:
                return review
        return None

    def get(self, id=None):
        if id is not None:
            review = self.get_with_id(id)
            if review:
                return MockedResponse(review, 200)
            return MockedResponse({'error': 'not found'}, 404)
        else:
            return MockedResponse(self.reviews, 200)
        
    def delete(self, id=None):
        if id is not None:
            review = self.get_with_id(id)    
            if review:
                self.reviews.remove(review)
                return MockedResponse(review, 204)
            return MockedResponse({'error': 'not found'}, 404)
        else:
            return MockedResponse(self.reviews, 200)

    def put(self, review):
        
        error_dict = {}
        this_field_required_message = 'This field is required'
        empty_field_message = 'This field cannot be empty'
        required_field_list = ('id', 'beer', 'rating', 'review')

        for required_field in required_field_list:
            if not review.get(required_field) and review.get(required_field) != 0:
                if review.get(required_field) == '':
                    
                    error_dict.update({required_field: empty_field_message})
                else:
                    error_dict.update({required_field: this_field_required_message})

        if error_dict:
            return MockedResponse(error_dict, 400)

        for index, ratebeer_review in enumerate(self.reviews):
            if ratebeer_review.id == review.id:
                self.reviews[index] = review
                return MockedResponse(self.reviews[index], 200)

        return MockedResponse({'error': 'not found'}, 404)

    def post(self, review):
        error_dict = {}
        this_field_required_message = 'This field is required'
        empty_field_message = 'This field cannot be empty'
        required_field_list = ('beer', 'rating', 'review')

        for required_field in required_field_list:
            if not review.get(required_field):
                if review.get(required_field) == '':
                    error_dict.update({required_field: empty_field_message})
                else:
                    error_dict.update({required_field: this_field_required_message})

        
        if error_dict:
            return MockedResponse(error_dict, 400)

        review.update({'id': self.id})
        self.id += 1
        self.reviews.append(review)
        return MockedResponse(review, 201)


class RateBeerClientTests(TestCase):
    def setUp(self):
        self.api_client = MockedApiClient()
        self.ratebeer_client = RateBeerClient(self.api_client)

        self.correct_review_data = {
            'beer': 'beer',
            'rating': '1',
            'review': 'review'
        }

    def test_no_reviews(self):
        self.api_client.reset()
        assert self.ratebeer_client.get_list() == []

    def test_create_correct_data(self):
        
        review_object = RateBeerReview('beer', '1', 'review')

        self.api_client.reset()
        assert self.ratebeer_client.create(review_object).__dict__ == RateBeerReview('beer', '1', 'review', 0).__dict__

    def test_no_field_exception(self):
        review_object = RateBeerReviewMock(beer='beer', rating='rating')
        with pytest.raises(APIBadRequestException) as exception:
            self.ratebeer_client.create(review_object)
        assert 'required' in exception.value.errors['review']

    def test_multiple_no_fields_exception(self):
        review_object = RateBeerReviewMock(beer='beer')
        with pytest.raises(APIBadRequestException) as exception:
            self.ratebeer_client.create(review_object)
        assert 'required' in exception.value.errors['review']
        assert 'required' in exception.value.errors['rating']

    def test_empty_field_exception(self):
        review_object = RateBeerReviewMock(beer='beer', rating='rating', review='')
        with pytest.raises(APIBadRequestException) as exception:
            self.ratebeer_client.create(review_object)
        assert 'empty' in exception.value.errors['review']

    def test_object_not_found_exception(self):
        self.api_client.reset()
        with pytest.raises(APINotFoundException) as exception:
            self.ratebeer_client.get(0)
        assert 'not found' in exception.value.errors['error']

    def test_object_found(self):
        review_object = RateBeerReview('beer', '1', 'review')

        self.api_client.reset()
        created_object_id = self.ratebeer_client.create(review_object).id
        review_object.id = created_object_id
        assert self.ratebeer_client.get(created_object_id).__dict__ == review_object.__dict__

    def test_object_delete(self):
        review_object = RateBeerReview('beer', '1', 'review')

        self.api_client.reset()
        created_object_id = self.ratebeer_client.create(review_object).id
        review_object.id = created_object_id

    def test_no_object_delete(self):
        self.api_client.reset()
        created_object_id = 0
        
        with pytest.raises(APINotFoundException) as exception:
            self.ratebeer_client.delete(created_object_id)
        assert 'not found' in exception.value.errors['error']

    def test_no_object_put(self):
        self.api_client.reset()
        
        changed_object = RateBeerReview('beer', '1', 'review', 0)

        with pytest.raises(APINotFoundException) as exception:
            self.ratebeer_client.put(changed_object)
        assert 'not found' in exception.value.errors['error']

    def test_no_field_put(self):
        self.api_client.reset()
        
        changed_object = RateBeerReviewMock('beer', '1', 'review')

        with pytest.raises(APIBadRequestException) as exception:
            self.ratebeer_client.put(changed_object)
        assert 'required' in exception.value.errors['id']











        