from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_person, name='add_person'),
    path('display/', views.display_name, name='display_name'),
]

