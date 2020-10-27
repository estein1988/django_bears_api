from django.shortcuts import render
from rest_framework import viewsets
from .models import Bear, PicnicBasket
from .serializers import BearSerializer, PicnicBasketSerializer

# Create your views here.
class BearView(viewsets.ModelViewSet):
    queryset = Bear.objects.all()
    serializer_class = BearSerializer

class PicnicBasketView(viewsets.ModelViewSet):
    queryset = PicnicBasket.objects.all()
    serializer_class = PicnicBasketSerializer
