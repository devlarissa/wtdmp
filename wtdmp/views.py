from django.http import JsonResponse
from .models import XD
from .models import Package 
from .serializers import XDSerializer
from .serializers import PackageSerializer
from .serializers import DeliverSerializer
from django.core.exceptions import ObjectDoesNotExist


def xd_list(request):
    #get all the xds, serialize them, return json
    xds = XD.objects.all()
    serializer = XDSerializer(xds, many = True)
    return JsonResponse({"xds": serializer.data}, safe = False)

def package_list(request):
    #get all the packages, serialize them, return json
    package = Package.objects.all()
    serializer = PackageSerializer(package, many = True)
    return JsonResponse({"packages": serializer.data}, safe = False)

def deliver_to(request, id):
    #get all the packages, serialize them, return json
    xds = XD.objects.all()
    try:
        package = Package.objects.get(id=id)
    except Exception as e:
        return JsonResponse({"erro": str(e)}, safe = False)

    xd_min_distance = package.distance_between(xds)
    serializer = DeliverSerializer(xd_min_distance)
    
    return JsonResponse({"xd mais proximo": serializer.data}, safe = False)
    # return HttpResponseRedirect(xd_min_distance)
