from django.db import models

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=50, null=False)
    genre = models.CharField(max_length=30, null=False)
    director = models.CharField(max_length=50, null=False)
    year = models.IntegerField(null=False)
    sinopsis = models.TextField(null=False)
    
    def __str__(self) -> str:
        return self.title