from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product


@api_view()
def api_home(request, *args, **kwargs):

    return Response({'message': 'hello world'})
