from django.urls import path
from .views  import homepage, add_book,update_book
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('add_book', views.add_book, name = 'add_book'),
    path('book/<int:pk>/update/', views.update_book, name='update_book'),
]
