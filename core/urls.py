from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from .views import CadCustumer, GetAllCustumers, GetCustumer

urlpatterns = [
    path('new-custumer/', CadCustumer.as_view()),
    path('consult-all-custumers/', GetAllCustumers.as_view()),
    path('consult-custumer', GetCustumer.as_view()),
]
