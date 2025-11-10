from django import forms
from .models import Book


# ===================================================================================
#  book form for create and update book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# ===================================================================================
# book search form
class BookSearchForm(forms.Form):
    q = forms.CharField(max_length=200, required=False)

# ===================================================================================
# example form with basic fields
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, label='Book Title')
    author = forms.CharField(max_length=100, label='Author')