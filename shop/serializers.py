from rest_framework import serializers

from .models import Worker, Shop, Visiting


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['name', 'phone']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['worker', 'shop_name']


class VisitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visiting
        fields = ['shop', 'date']
