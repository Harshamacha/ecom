from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer
from django.http import JsonResponse
from .models import Product
from django.shortcuts import render
import json
def index(request):
    if request.method  =='POST':
        payload =json.loads1(request.body)
        Product= payload.get('product')

        for product_data in Product:
            name=product_data.get('name')
            description=product_data.get('description')
            imagepath=product_data.get('imagepath')
            price=product_data.get('price')
            manufacturer=product_data.get('manufacturer')
            return JsonResponse

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'imagepath', 'price', 'manufacturer']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'imagepath', 'price', 'manufacturer']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')



class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View for a single Product (GET, PUT, DELETE) by ID
class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return JsonResponse({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return JsonResponse({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return JsonResponse({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
