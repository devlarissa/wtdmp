from django.db import models
import math

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

    def distance_between(self, xds_objects):

        def measure_distance(origem, destino):
            return math.sqrt((destino[0] - origem[0])**2 + (destino[1] - origem[1])**2)

        xds_positions_list = [[xd.lat, xd.lng] for xd in xds_objects]
        package_position = [self.lat, self.lng]
        position_min = 0
        min_value = measure_distance(package_position, xds_positions_list[0])

        for i in range(len(xds_positions_list)):
            value = measure_distance(package_position, xds_positions_list[i])
            if value < min_value:
                min_value = value
                position_min = i

        return xds_objects[position_min]