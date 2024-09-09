from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_stock, name='add_stock'),
    path('display/', views.display_name, name='display_name'),
]

