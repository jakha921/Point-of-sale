from shop.models import Worker, Shop, Visiting
from shop.serializers import WorkerSerializer, ShopSerializer, VisitingSerializer

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics


class ShopListAPIView(generics.ListAPIView):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer(queryset, many=True)       
    
    def get_queryset(self):
        return self.queryset.filter(worker__phone = self.kwargs['phone'])

    def list(self, request, phone):
        queryset = self.get_queryset()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)


class VisitingListAPIView(generics.ListAPIView):
    
    queryset = Visiting.objects.all()
    serializer_class = VisitingSerializer(queryset, many=True)
    
    def get_queryset(self):
        return self.queryset.filter(shop__pk = self.kwargs['shop_pk'], \
                                    latitude = self.kwargs['lat'], longitude = self.kwargs['lon'])
    def list(self, request, shop_pk, lat, lon):
        queryset = self.get_queryset()
        serializer = VisitingSerializer(queryset, many=True)
        return Response(serializer.data)
        