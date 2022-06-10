from django.db import models
from datetime import date, datetime
#   from django.contrib.auth.models import User #   maybe at the end develop this????
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
    ], blank=True)
    directors_and_actors = models.CharField(max_length=100, blank=True)
    user_rating = models.DecimalField(max_digits=5, decimal_places=2,
                                      validators=[
                                          MaxValueValidator(10),
                                          MinValueValidator(0),
                                      ], default=5.0)
    poster = models.ImageField(upload_to=upload_to, blank=True)

    def __str__(self):
        return str(self.title) + '  |  ' + str(self.release_year)\
               + '  |  ' + str(self.directors_and_actors) + '  |  ' + str(self.user_rating)

    class Meta:
        ordering = ['title']
