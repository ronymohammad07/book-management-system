from django.shortcuts import render
from .models import Book

# Create your views here.

def homepage(request):
    books = Book.objects.all()
    
    # context = {
    #     'books': books
    # }
    # print(books)
    
    return render (request, 'homepage.html', {'books': books})