from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions

# Base class for views with common functionality
class BaseAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            return Response({"error": "Only superusers can create data"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().put(request, *args, **kwargs)
        else:
            return Response({"error": "Only superusers can update data"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().delete(request, *args, **kwargs)
        else:
            return Response({"error": "Only superusers can delete data."}, status=status.HTTP_403_FORBIDDEN)


# College views
class CollegeListView(BaseAPIView, generics.ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeDetailView(BaseAPIView, generics.RetrieveAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeCreateView(BaseAPIView, generics.CreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeUpdateView(BaseAPIView, generics.UpdateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeDeleteView(BaseAPIView, generics.DestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeSearchView(generics.ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return self.queryset.filter(name__icontains=query)


# Course views
class CourseBaseView(BaseAPIView, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListView(CourseBaseView, generics.ListAPIView):
    pass


class CourseDetailView(CourseBaseView, generics.RetrieveAPIView):
    pass


class CourseCreateView(CourseBaseView, generics.CreateAPIView):
    pass


class CourseUpdateView(CourseBaseView, generics.UpdateAPIView):
    pass


class CourseDeleteView(CourseBaseView, generics.DestroyAPIView):
    pass


class CourseSearchView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return self.queryset.filter(name__icontains=query)




















from django.urls import path, include
from .views import *

app_name = 'your_app_name'

college_urls = [
    path('', CollegeListView.as_view(), name='college-list'),
    path('<int:pk>/', CollegeDetailView.as_view(), name='college-detail'),
    path('create/', CollegeCreateView.as_view(), name='college-create'),
    path('update/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('delete/<int:pk>/', CollegeDeleteView.as_view(), name='college-delete'),
    path('search/', CollegeSearchView.as_view(), name='college-search'),
]

course_urls = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='course-delete'),
    path('search/', CourseSearchView.as_view(), name='course-search'),
]

specialization_urls = [
    path('', SpecializationListView.as_view(), name='specialization-list'),
    path('<int:pk>/', SpecializationDetailView.as_view(), name='specialization-detail'),
    path('create/', SpecializationCreateView.as_view(), name='specialization-create'),
    path('update/<int:pk>/', SpecializationUpdateView.as_view(), name='specialization-update'),
    path('delete/<int:pk>/', SpecializationDeleteView.as_view(), name='specialization-delete'),
    path('search/', SpecializationSearchView.as_view(), name='specialization-search'),
]

department_urls = [
    path('', DepartmentListView.as_view(), name='department-list'),
    path('<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('create/', DepartmentCreateView.as_view(), name='department-create'),
    path('update/<int:pk>/', DepartmentUpdateView.as_view(), name='department-update'),
    path('delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department-delete'),
    path('search/', DepartmentSearchView.as_view(), name='department-search'),
]

fee_urls = [
    path('', FeeListView.as_view(), name='fee-list'),
    path('<int:pk>/', FeeDetailView.as_view(), name='fee-detail'),
    path('create/', FeeCreateView.as_view(), name='fee-create'),
    path('update/<int:pk>/', FeeUpdateView.as_view(), name='fee-update'),
    path('delete/<int:pk>/', FeeDeleteView.as_view(), name='fee-delete'),
    path('search/', FeeSearchView.as_view(), name='fee-search'),
]

country_urls = [
    path('', CountryListView.as_view(), name='country-list'),
    path('<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
    path('create/', CountryCreateView.as_view(), name='country-create'),
    path('update/<int:pk>/', CountryUpdateView.as_view(), name='country-update'),
    path('delete/<int:pk>/', CountryDeleteView.as_view(), name='country-delete'),
    path('search/', CountrySearchView.as_view(), name='country-search'),
]

urlpatterns = [
    path('colleges/', include((college_urls, 'college'), namespace='college')),
    path('courses/', include((course_urls, 'course'), namespace='course')),
    path('specializations/', include((specialization_urls, 'specialization'), namespace='specialization')),
    path('departments/', include((department_urls, 'department'), namespace='department')),
    path('fees/', include((fee_urls, 'fee'), namespace='fee')),
    path('countries/', include((country_urls, 'country'), namespace='country')),
]
