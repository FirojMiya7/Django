from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Book
from .forms import BookForm
# Create your views here.


#Read Operations
@login_required
def book_list(request):
    query = request.GET.get('q', '').strip()
    books = Book.objects.all()

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        ).distinct()

    return render(request, 'book/book.html', {'books': books, 'query': query})

#Read Operation with unique Id 
@login_required
def Book_detail(request,id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book/book_detail.html', {'book': book})

#CREATE operation
@login_required
def Book_create(request):
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})


#Update Operation
@login_required
def Book_update(request,id):
    book= get_object_or_404(Book,pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form =BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})

#Delete operation
@login_required
def Book_delete(request,id):
    book= get_object_or_404(Book,pk=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book')
    return render(request, 'book/book_delete.html', {'book': book})


#Home page view
def home(request):
    return render(request, 'book/home.html')