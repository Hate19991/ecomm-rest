from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
from django.db.models.functions import Lower
# from customer.models import Customer

# Create your views here.
class CartViewSet(APIView):
    def get(self , request, cart_id:str):
        cart = Cart.objects.filter(id=cart_id)
        serializer = CartSerializer(cart , many=True)
        if cart.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializers = CartSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def put(self, request,  id, format=None):
        cart =  self.get_by_id(id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id:str):
        cart = self.get_by_id(id)
        cart.delete()
        return Response({"message": "Cart deleted"}, status=status.HTTP_200_OK)
    
class CartItemViewSet(APIView):
    def get(self , request , cart_id:str , id:str):
        cart = Cart.objects.filter(id=cart_id)
        cartitem = CartItem.objects.filter(cart_id=cart_id, id=id)
        serializers = CartItemSerializer(cartitem , many=True)
        if cartitem:
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({"error":"it appears this cartitem does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    def post (self, request , format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)