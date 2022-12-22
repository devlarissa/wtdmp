from django.db import models

class XD(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()