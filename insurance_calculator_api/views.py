from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('calculate_insurance:user-list', request=request, format=format),
        'Car Information': reverse('calculate_insurance:car-list', request=request,format=format),
    })
