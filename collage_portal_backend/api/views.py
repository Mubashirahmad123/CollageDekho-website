from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import *
from .serializers import *

class CollegeListView(ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeDetailView(RetrieveAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeCreateView(CreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeUpdateView(UpdateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeDeleteView(DestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer





class Department():
    def  __init__(self, name):
        pass
