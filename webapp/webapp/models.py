from django.db import models
from django.utils import timezone
from datetime import date, datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def upload_to(instance, file_name):
    formatted_date = datetime.now().strftime("%d-%m-%Y")
    return f"{formatted_date}/{file_name}"


class Data(models.Model):
    """Model used to store data, that my web-scraping spider collected"""
    title = models.CharField(max_length=100)
    release_year = models.IntegerField(validators=[
        MaxValueValidator(date.today().year),
        MinValueValidator(1895),
    ])
    directors_and_actors = models.CharField(max_length=100)
    user_rating = models.DecimalField(max_digits=5, decimal_places=2,
                                      validators=[
                                          MaxValueValidator(10),
                                          MinValueValidator(0),
                                      ])
    poster = models.ImageField(upload_to=upload_to)
