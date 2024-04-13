from django.shortcuts import render, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        Book.objects.create(title=title, author=author, genre=genre)
        return redirect('book_list')
    return render(request, 'create_book.html')

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.genre = request.POST.get('genre')
        book.save()
        return redirect('book_list')
    return render(request, 'update_book.html', {'book': book})

def delete_book(request, book_id):
    if request.method =="POST":
        book = Book.objects.get(id=book_id)
        book.delete()
    return redirect('book_list')
