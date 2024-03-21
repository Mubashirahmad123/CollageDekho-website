from django.urls import path
from .views import *

from .models import *
from django.urls import reverse_lazy



urlpatterns = [
    # college urls
    path('colleges/', CollegeListView.as_view(), name='college-list'),
    path('colleges/<int:pk>/', CollegeDetailView.as_view(), name='college-detail'),
    path('colleges/create/', CollegeCreateView.as_view(), name='college-create'),
    path('colleges/update/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/delete/<int:pk>/', CollegeDeleteView.as_view(), name='college-delete'),
    path('search/college', CollegeSearchView.as_view(), name='college-search'),

    
    # Course url
     path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course-create'),
    path('courses/update/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/delete/<int:pk>/', CourseDeleteView.as_view(), name='course-delete'),
    path('search/course', CourseSearchView.as_view(), name='course-search'),
    
    
    # Specialization url
     path('specialization/', SpecializationListView.as_view(), name='specialization-list'),
    path('specialization/<int:pk>/', SpecializationDetailView.as_view(), name='specialization-detail'),
    path('specialization/create/', SpecializationCreateView.as_view(), name='specialization-create'),
    path('specialization/update/<int:pk>/', SpecializationUpdateView.as_view(), name='specialization-update'),
    path('specialization/delete/<int:pk>/', SpecializationDeleteView.as_view(), name='specialization-delete'),
    path('search/specialization', SpecializationSearchView.as_view(), name='specialization-search'),
    
    
    # Department url
    
    path('department/', DepartmentListView.as_view(), name='department-list'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('department/create/', DepartmentCreateView.as_view(), name='department-create'),
    path('department/update/<int:pk>/', DepartmentUpdateView.as_view(), name='specialization-update'),
    path('department/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department-delete'),
    path('search/department', DepartmentSearchView.as_view(), name='department-search'),
    
    
    
    # Fee urls
    
    path('fee/', FeeListView.as_view(), name='fee-list'),
    path('fee/<int:pk>/', FeeDetailView.as_view(), name='fee-detail'),
    path('fee/create/', FeeCreateView.as_view(), name='fee-create'),
    path('fee/update/<int:pk>/', FeeUpdateView.as_view(), name='fee-update'),
    path('fee/delete/<int:pk>/', FeeDeleteView.as_view(), name='fee-delete'),
    path('search/fee', FeeSearchView.as_view(), name='fee-search'),
    
    
    #   Country url
    
    path('country/', CountryListView.as_view(), name='Country-list'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
    path('country/create/', CountryCreateView.as_view(), name='country-create'),
    path('country/update/<int:pk>/', CountryUpdateView.as_view(), name='country-update'),
    path('country/delete/<int:pk>/', CountryDeleteView.as_view(), name='country-delete'),
    path('search/country', CountrySearchView.as_view(), name='country-search'),



# Review url

    path('reviews/', ReviewView.as_view(), name='review-list'),  # Endpoint to list all reviews
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),  # Endpoint to create a new review
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),  # Endpoint to retrieve a specific review
    path('reviews/update/<int:pk>/', ReviewUpdateView.as_view(), name='review-update'),  # Endpoint to update a review
    path('reviews/delete/<int:pk>/', ReviewDeleteView.as_view(), name='review-delete'),  
    
# Admission Urls
    path('admission/', AdmissionListView.as_view(), name='admission-list'),
    path('admission/<int:pk>/', AdmissionDetailView.as_view(), name='admission-detail'),
    path('admission/create/', AdmissionCreateView.as_view(), name='admission-create'),
    path('admission/update/<int:pk>/', AdmissionUpdateView.as_view(), name='admission-update'),
    path('admission/delete/<int:pk>/', AdmissionDeleteView.as_view(), name='admission-delete'),

]
  
  








