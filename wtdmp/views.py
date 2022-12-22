from django.http import JsonResponse
from .models import XD
from .models import Package 
from .serializers import XDSerializer
from .serializers import PackageSerializer

def xd_list(request):
    #get all the xds, serialize them, return json
    xd = XD.objects.all()
    serializer = XDSerializer(xd, many = True)
    return JsonResponse({"xds": serializer.data}, safe = False)

def package_list(request):
    #get all the packages, serialize them, return json
    package = Package.objects.all()
    serializer = PackageSerializer(package, many = True)
    return JsonResponse({"packages": serializer.data}, safe = False)