from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('new-costumer/', ),
    path('consult-all-costumers/', ),
    path('consult-costumer/id=?', ),
]
