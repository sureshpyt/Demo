from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework . generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin



# Create your views here.

class Booklist(GenericAPIView,ListModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def get(self,request):
        return self.list(request)

class Bookcreate(GenericAPIView,CreateModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def post(self,request):
        return self.create(request)

class Bookdis(GenericAPIView,RetrieveModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)


class Bookupdate(GenericAPIView,UpdateModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def put(self,request,**kwargs):
        return self.Update(request,**kwargs)


class Bookdel(GenericAPIView,DestroyModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def delete(self,request,**kwargs):
        return self.destory(request,**kwargs)


