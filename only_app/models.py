from django.db import models

class CityName(models.Model):
    name = models.CharField(max_length=25)

    