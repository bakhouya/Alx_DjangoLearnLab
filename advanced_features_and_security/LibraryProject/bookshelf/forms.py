from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
class BookSearchForm(forms.Form):
    q = forms.CharField(max_length=200, required=False)


class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, label='Book Title')
    author = forms.CharField(max_length=100, label='Author')