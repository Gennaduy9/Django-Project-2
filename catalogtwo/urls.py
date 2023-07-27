
from django.urls import path

from catalogtwo.views import index, contact

app_name = 'catalog'

urlpatterns = [
    path('', index, name='catalog'),
    path('contact/', contact, name='contact')
]