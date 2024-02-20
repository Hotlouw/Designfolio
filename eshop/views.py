from rest_framework import generics
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer
from .models import CartItem
from django.shortcuts import render, redirect
from django.http import HttpResponse


def contact_list(request):
    # Your code here
    return HttpResponse("Contact")

def aboutus_list(request):
    # Your code here
    return HttpResponse("About Us")

def login_list(request):
    # Your code here
    return HttpResponse("Login")

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def main_view(request):
    return render(request,'main.html')

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer