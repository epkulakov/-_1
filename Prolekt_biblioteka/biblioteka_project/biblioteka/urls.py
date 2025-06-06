from operator import index

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.index, name = 'index'),
    path('udalen/', views.udalen, name = 'udalen'),
    path('dobavlen/', views.dobavlen, name='dobavlen'),
    path('izmenenie/', views.izmenenie, name='izmenenie'),
    path('podrobnos/<int:book_id>/', views.podrobn, name='podrobn')
]