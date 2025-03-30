# blog/forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add a comment...'}),
        required=True,
        min_length=3,
        max_length=1000,
        label='',
        error_messages={
            'required': 'Comment content is required',
            'min_length': 'Comment must be at least 3 characters long',
            'max_length': 'Comment cannot exceed 1000 characters'
        }
    )
    
    class Meta:
        model = Comment
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content and content.strip() == '':
            raise forms.ValidationError('Comment cannot be blank or contain only whitespace')
        return content