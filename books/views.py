from .models import Book
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list_view.html'