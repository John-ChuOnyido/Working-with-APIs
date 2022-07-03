from django.shortcuts import render

# Create your views here.
from .models import Link
from .models import LinkSerializer
from django.views.generic.list import ListAPIView
from django.views.generic.edit import CreateAPIView
from django.views.generic.detail import DetailAPIView
from django.views.generic.edit import UpdateAPIView
from django.views.generic.edit import DeleteAPIView

class PostListApi(ListAPIView):
    queryset = Link.object.filter(active=True) 
    serializer_class = LinkSerializer
    
class PostCreateApi(CreateAPIView):
    queryset = Link.object.filter(active=True) 
    serializer_class = LinkSerializer
    
  
class PostDetailApi(DetailAPIView):
    queryset = Link.object.filter(active=True) 
    serializer_class = LinkSerializer
    
    
class PostUpdateApi(UpdateAPIView):
   queryset = Link.object.filter(active=True)
   serializer_class = LinkSerializer
    
class PostDeleteApi(DeleteAPIView):
    queryset = Link.object.filter(active=True) 
    serializer_class = LinkSerializer
    