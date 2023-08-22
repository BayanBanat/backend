from django.shortcuts import render
from .models import CookieStand
from .serializers import CookieStand_serializers

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView


class ListApiView(ListCreateAPIView):
    queryset= CookieStand.objects.all()
    serializer_class=CookieStand_serializers

class DetailApiView(RetrieveUpdateDestroyAPIView):
    queryset= CookieStand.objects.all()
    serializer_class=CookieStand_serializers

