from django.shortcuts import render
from RestAPP.serializers import ProductSerializer
from RestAPP.models import Products
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# Create your views here.
class ProdList(GenericAPIView,ListModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs )
    
class ProdCreate(GenericAPIView,CreateModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs )
    
class ProdRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs )
    
class ProdUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs )
    
class Proddelete(GenericAPIView,DestroyModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs )
    