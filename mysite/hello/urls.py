from django.urls import path
from . import views

urlpatterns = [
    
    path('demo', views.demo, name='demo'),  # This will be for `/demo/home/`
]
