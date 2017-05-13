class RateBeerReview:
    def __init__(self, beer, rating, review, id=None):
        self.id = id
        self.beer = beer
        self.rating = rating
        self.review = review
    

class APIBadRequestException(Exception):
    def __init__(self, api_errors):
        self.errors = api_errors

class APINotFoundException(Exception):
    def __init__(self, api_errors):
        self.errors = api_errors

class RateBeerClient:
    def __init__(self, api_client):
        self.client = api_client
    
    def dict_to_object(self, ratebeer_review):
        return RateBeerReview(ratebeer_review.get('beer'),
            ratebeer_review.get('rating'), ratebeer_review.get('review'), ratebeer_review.get('id'))

    def object_to_dict(self, ratebeer_review):
        return {'beer': ratebeer_review.beer,
                'rating': ratebeer_review.rating, 
                'review': ratebeer_review.review}

    def object_to_dict_with_id(self, ratebeer_review):
        return {'id': ratebeer_review.id,
                'beer': ratebeer_review.beer,
                'rating': ratebeer_review.rating, 
                'review': ratebeer_review.review}

    def get_list(self):
        response = self.client.get()
        return [self.dict_to_object(ratebeer_review) 
            for ratebeer_review in response.data]

    def get(self, review_id):
        response = self.client.get(review_id)
        if response.status_code == 404:
            raise APINotFoundException(response.data)
        return self.dict_to_object(response.data)

    def create(self, ratebeer_review):
        response = self.client.post(self.object_to_dict(ratebeer_review))
        if response.status_code == 400:
            raise APIBadRequestException(response.data)
        return self.dict_to_object(
            response.data
            )

    def delete(self, review_id):
        response = self.client.delete(review_id)
        if response.status_code == 404:
            raise APINotFoundException(response.data)

    def put(self, review):
        response = self.client.put(self.object_to_dict_with_id(review))
        if response.status_code == 404:
            raise APINotFoundException(response.data)
        elif response.status_code == 400:
            raise APIBadRequestException(response.data)
        return response.data