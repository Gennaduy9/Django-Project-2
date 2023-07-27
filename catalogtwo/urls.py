
from django.urls import path

from catalogtwo.views import index, contact

urlpatterns = [
    path('', index),
    path('contact/', contact)
]