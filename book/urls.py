from django.urls import path
from .views  import homepage
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
]
