from django.db import models
from django.core import validators

RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class RatingField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = RATING_CHOICES
        kwargs['max_length'] = 16
        super().__init__(*args, **kwargs)


class SliderField(models.FloatField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = (validators.MinValueValidator(0.0),
                                validators.MaxValueValidator(1.0))
        super().__init__(*args, **kwargs)
