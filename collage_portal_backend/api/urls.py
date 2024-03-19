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
    path('search/', CollegeSearchView.as_view(), name='college-search'),

    
    # Course url
     path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course-create'),
    path('courses/update/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/delete/<int:pk>/', CourseDeleteView.as_view(), name='course-delete'),
    path('search/course', CourseSearchView.as_view(), name='course-search'),

]
  
  








