from django import forms
from .models import Post

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','page_title','author','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter the Title of the post'}),
            'page_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter the page title of the post'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder':'select the one of the author'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter the content for the blog post'}),
        }