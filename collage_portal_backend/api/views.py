from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions


# collage view
class CollegeListView(ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeDetailView(RetrieveAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeCreateView(CreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().post(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can create data"}, status=status.HTTP_403_FORBIDDEN)


class CollegeUpdateView(UpdateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def put(self, request, *args, **kwargs ):
       if request.user.is_superuser :
           return super().put(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can update data"}, status=status.HTTP_403_FORBIDDEN)


class CollegeDeleteView(DestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
    def delete(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().destroy(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can update, delete, or create data."}, status=status.HTTP_403_FORBIDDEN)



class CollegeSearchView(generics.ListAPIView):
    serializer_class = CollegeSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return College.objects.filter(name__icontains=query) 



# Course View

class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseCreateView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().post(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can create data"}, status=status.HTTP_403_FORBIDDEN)


class CourseUpdateView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def put(self, request, *args, **kwargs ):
       if request.user.is_superuser :
           return super().put(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can update data"}, status=status.HTTP_403_FORBIDDEN)


class CourseDeleteView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
    def delete(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().destroy(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can delete data."}, status=status.HTTP_403_FORBIDDEN)
       
       
class CourseSearchView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Course.objects.filter(name__icontains=query)
        
           






class Department():
    def  __init__(self, name):
        pass
