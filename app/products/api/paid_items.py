from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Basket


class BasketPaid(APIView):
    def get(self, request):
        items = Basket.objects.filter(status='paid')
        return Response({"items": items})
