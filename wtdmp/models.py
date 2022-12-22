from django.db import models

class XD(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return '[' + str(self.lat) + ', ' + str(self.lng) + ']'

class Package(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return '[' + str(self.lat) + ', ' + str(self.lng) + ']'