from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.db import models
from .models import Book
from .forms import BookForm

# Create your views here.

def homepage(request):
    books = Book.objects.all()
    
    return render (request, 'homepage.html', {'books': books})

# use django form
# def add_book(request):
#     if request.method == 'POST':
#         form = Book(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         return render(request, 'add_book.html')
def add_book(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        published_year = request.POST.get('published_year')
        
        # bookInfo = Book.objects.create(
        #     title=title,
        #     author=author,
        #     description=description,
        #     published_year=published_year
        # )
        bookInfo = Book(
            title=title,
            author=author,
            description=description, published_year=published_year)
        bookInfo.save()
        return render(request, 'success.html')
    return render(request, 'add_book.html')

# View to update an existing book
def update_book(request, pk):
    # Get the book object by its primary key
    book = get_object_or_404(Book, pk=pk)

    # If the request is a POST (form submission), we need to handle the form submission
    if request.method == 'POST':
        # Bind the POST data to the form and include the existing book instance
        form = BookForm(request.POST, instance=book)

        # Check if the form is valid
        if form.is_valid():
            form.save()  # Save the updated book instance
            return redirect('/')  # Redirect to the book list after updating
    else:
        # If it's a GET request, just create the form with the existing book data
        form = BookForm(instance=book)

    # Render the template with the form
    return render(request, 'book_update.html', {'form': form, 'book': book})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    print(book)
    
    if book:
        book.delete()
        return render(request,'delete_success.html')
    return render(request, 'homepage')