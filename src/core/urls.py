from django.urls import path,include
from .views import TestView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('',TestView.as_view(),name='index'),
    path('rest-auth/', include('rest_auth.urls'))
  
]