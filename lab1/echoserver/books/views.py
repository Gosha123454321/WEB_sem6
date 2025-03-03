from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator

def book_list(request):
    books = Book.objects.all().order_by('id')
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_obj': page_obj})

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_edit.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_edit.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')