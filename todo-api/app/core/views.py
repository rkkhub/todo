from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def maintenance_view(request):
    return Response(data="Service under maintenance",
                    status=status.HTTP_503_SERVICE_UNAVAILABLE)
