from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator


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
    poster = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-user_rating', 'title']
