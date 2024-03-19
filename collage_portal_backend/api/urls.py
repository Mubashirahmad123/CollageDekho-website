from django.urls import path
from .views import CollegeListView, CollegeDetailView, CollegeCreateView, CollegeUpdateView, CollegeDeleteView

from .models import *
from django.urls import reverse_lazy



urlpatterns = [
    path('colleges/', CollegeListView.as_view(), name='college-list'),
    path('colleges/<int:pk>/', CollegeDetailView.as_view(), name='college-detail'),
    path('colleges/create/', CollegeCreateView.as_view(), name='college-create'),
    path('colleges/update/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/delete/<int:pk>/', CollegeDeleteView.as_view(), name='college-delete'),
]
  
  








