from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100, null=True)
    name_amharic = models.CharField(max_length=100)
    name_afaan_oromo = models.CharField(max_length=100)
    job_type_amharic = models.CharField(max_length=100)
    job_type_afaan_oromo = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    width = models.FloatField()
    height = models.FloatField()
    square = models.FloatField(blank=True, null=True)
    completed = models.BooleanField(default=False)



    def __str__(self):
        return self.name_amharic
