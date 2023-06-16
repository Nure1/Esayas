from django.urls import path
from . import views

urlpatterns = [
    path('locations/api/', views.LocationListAPIView.as_view(), name='locationApi'),
    path('location/create/', views.LocationCreateAPIView.as_view(), name='createLocation'),
    path('location/<int:pk>/', views.LocationUpdateAPIView.as_view(), name='updateLocation'),
    path('location/<int:pk>/delete/', views.LocationDeleteAPIView.as_view(), name='updateLocation'),
    path('export/', views.export_to_excel, name='export')
]