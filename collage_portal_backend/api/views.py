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
        





# Specialization view

class SpecializationListView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class SpecializationDetailView(RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class SpecializationCreateView(CreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().post(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can create data"}, status=status.HTTP_403_FORBIDDEN)


class SpecializationUpdateView(UpdateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def put(self, request, *args, **kwargs ):
       if request.user.is_superuser :
           return super().put(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can update data"}, status=status.HTTP_403_FORBIDDEN)


class SpecializationDeleteView(DestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
    def delete(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().destroy(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can delete data."}, status=status.HTTP_403_FORBIDDEN)
       
       
class SpecializationSearchView(generics.ListAPIView):
    serializer_class = SpecializationSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Specialization.objects.filter(name__icontains=query)
           


# department view

class DepartmentListView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentCreateView(CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().post(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can create data"}, status=status.HTTP_403_FORBIDDEN)


class DepartmentUpdateView(UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def put(self, request, *args, **kwargs ):
       if request.user.is_superuser :
           return super().put(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can update data"}, status=status.HTTP_403_FORBIDDEN)


class DepartmentDeleteView(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
    def delete(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().destroy(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can delete data."}, status=status.HTTP_403_FORBIDDEN)
       
       
class DepartmentSearchView(generics.ListAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Department.objects.filter(name__icontains=query)


# Fee view

class FeeListView(ListAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class FeeDetailView(RetrieveAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class FeeCreateView(CreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().post(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can create data"}, status=status.HTTP_403_FORBIDDEN)


class FeeUpdateView(UpdateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def put(self, request, *args, **kwargs ):
       if request.user.is_superuser :
           return super().put(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can update data"}, status=status.HTTP_403_FORBIDDEN)


class FeeDeleteView(DestroyAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
    def delete(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().destroy(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can delete data."}, status=status.HTTP_403_FORBIDDEN)
       
       
class FeeSearchView(generics.ListAPIView):
    serializer_class = FeeSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Fee.objects.filter(name__icontains=query)


# Country view

class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryCreateView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().post(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can create data"}, status=status.HTTP_403_FORBIDDEN)


class CountryUpdateView(UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAdminUser]
    
    def put(self, request, *args, **kwargs ):
       if request.user.is_superuser :
           return super().put(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can update data"}, status=status.HTTP_403_FORBIDDEN)


class CountryDeleteView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAdminUser]
    
    
    def delete(self, request, *args, **kwargs):
       if request.user.is_superuser :
           return super().destroy(request,*args,**kwargs)
       else:
           return Response({"error": "Only superusers can delete data."}, status=status.HTTP_403_FORBIDDEN)
       
       
class CountrySearchView(generics.ListAPIView):
    serializer_class = FeeSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Country.objects.filter(name__icontains=query)
