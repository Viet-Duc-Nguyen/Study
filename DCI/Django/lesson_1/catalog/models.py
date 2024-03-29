from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.PositiveBigIntegerField()
    director = models.CharField(max_length=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title
