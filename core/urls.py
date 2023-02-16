from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from .views import CadCustumer, GetAllCostumers

urlpatterns = [
    path('new-costumer/', CadCustumer.as_view()),
    path('consult-all-costumers/', GetAllCostumers.as_view()),
    #path('consult-costumer/id=?', ),
]
