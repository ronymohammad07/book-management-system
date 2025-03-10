from django.shortcuts import render
from .models import Book

# Create your views here.

def homepage(request):
    books = Book.objects.all()
    
    return render (request, 'homepage.html', {'books': books})


def add_book(request):
    
    return render(request, 'add_book.html')