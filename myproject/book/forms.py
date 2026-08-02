from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','description','price','publishedDate']
        widgets = {
            'publishedDate':forms.DateInput(attrs={'type':'date'}),
            'description':forms.Textarea(attrs={'rows':4, 'cols':15}),
        }