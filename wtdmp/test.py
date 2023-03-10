from django.test import TestCase
from wtdmp.models import Package
from wtdmp.models import XD
from wtdmp.views import deliver_to

class TestExampleTestCase(TestCase):
    
    def test_classes(self):
        xd = XD(lat=1, lng=1)
        xd.save()

        assert XD.objects.all().count() == 1
        
        pg = Package(lat=5, lng=5)
        pg.save()

        assert Package.objects.all().count() == 1

    def test_package(self):
        xds = [XD(lat=i, lng=i) for i in range(5)] 
        assert len(xds) == 5
        
        package = Package(lat=2.2, lng=2.2)
        
        assert package.distance_between(xds) != None
        assert package.distance_between(xds) == xds[2]
    
    def test_package_does_not_exist(self):

        result = deliver_to(None, 2)

        assert result._container[0] == b'{"erro": "Package matching query does not exist."}'


