from django.urls import path
from .views import home, about, portfolio, service, contact,login, UserLoginAPIView, LocationCreateAPIView, LocationUpdateAPIView, LocationListAPIView, LocationDeleteAPIView, export_to_excel
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
    
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('porfolio/', portfolio, name='portfolio'),
    path('services/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('login/api/', UserLoginAPIView.as_view(), name='user-login'),
    path('locations/api/', LocationListAPIView.as_view(), name='locationApi'),
    path('location/create/', LocationCreateAPIView.as_view(), name='createLocation'),
    path('location/<int:pk>/', LocationUpdateAPIView.as_view(), name='updateLocation'),
    path('location/<int:pk>/delete/', LocationDeleteAPIView.as_view(), name='updateLocation'),
    path('export/', export_to_excel, name='export'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]