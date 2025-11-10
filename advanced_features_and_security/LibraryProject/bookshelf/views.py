from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
from .forms import ExampleForm


# =====================================================================================
# get all book if has permission and user is logged in
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
# =====================================================================================


# =====================================================================================
# create new book if has permission and user is logged in
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
# =====================================================================================


# =====================================================================================
# update book if has permission and user is logged in
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/form_example.html', {'form': form, 'book': book})
# =====================================================================================


# =====================================================================================
# delete book if has permission and user is logged in
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')
# =====================================================================================
