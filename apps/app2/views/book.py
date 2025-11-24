# apps.app3/views.py
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Book
from ..forms import BookForm
from django.contrib.auth.decorators import login_required

# List all books
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'app2/book_list.html', {'books': books})

# View book details
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'app2/book_detail.html', {'book': book})

# Create a new book
@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'app2/book_form.html', {'form': form})

# Update an existing book
@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'app2/book_form.html', {'form': form})

# Delete a book
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'app2/book_confirm_delete.html', {'book': book})
