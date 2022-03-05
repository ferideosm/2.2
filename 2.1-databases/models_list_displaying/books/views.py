from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    print('books==', books)
    context = {'books': books}
    return render(request, template, context)

def books_show(request, pub_date):
    template = 'books/book.html'
    book = Book.objects.get(pub_date=pub_date)
    context = {'book': book}
    print('book==', book)

    st_ = list()

    obj = Book.objects.all()
    for o in obj:
        st_.append(0)   

    paginator = Paginator(st_, 1) 
    current_page = request.GET.get('pub_date', 1) 
    print('current_page==', current_page)
    page = paginator.get_page(current_page)
    print('page==', page)
    print('page==', page.object_list)
    context = {
        'book': book,
        'books': page.object_list,
        'page': page,
    }
    return render(request, template, context)

