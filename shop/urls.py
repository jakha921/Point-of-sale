from django.urls import path

from .views import ShopListAPIView, VisitingListAPIView

urlpatterns = [
    path('phone/<str:phone>', ShopListAPIView.as_view(), name='phone'),
    path('shop/<int:shop_pk>/<lat>/<lon>', VisitingListAPIView.as_view(), name='visiting'),
]
