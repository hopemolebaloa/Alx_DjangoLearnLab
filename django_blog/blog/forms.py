# blog/forms.py
from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # If editing an existing post, populate the tags field
            self.initial['tags'] = ', '.join([tag.name for tag in self.instance.tags.all()])
    
    def save(self, commit=True):
        post = super().save(commit=False)
        
        if commit:
            post.save()
            
            # Clear existing tags
            post.tags.clear()
            
            # Process the tags
            tag_names = [name.strip() for name in self.cleaned_data['tags'].split(',') if name.strip()]
            
            for tag_name in tag_names:
                # Convert tag name to lowercase and create slug
                from django.utils.text import slugify
                tag_slug = slugify(tag_name)
                
                # Get or create the tag
                tag, created = Tag.objects.get_or_create(
                    slug=tag_slug,
                    defaults={'name': tag_name}
                )
                
                # Add tag to post
                post.tags.add(tag)
        
        return post