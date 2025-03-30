# blog/forms.py
from django import forms
from .models import Post
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }
        help_texts = {
            'tags': 'Enter tags separated by commas',
        }