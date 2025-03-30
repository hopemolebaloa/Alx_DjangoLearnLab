# blog/views.py
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from django_blog.blog.forms import PostForm
from .models import Post, Tag

def search_posts(request):
    query = request.GET.get('q', '')
    
    if query:
        # Search in title, content, or tags
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    
    context = {
        'query': query,
        'posts': posts,
    }
    
    return render(request, 'blog/search_results.html', context)

def tag_posts(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags=tag)
    
    context = {
        'tag': tag,
        'posts': posts,
    }
    
    return render(request, 'blog/tag_posts.html', context)
# Modify your existing post_create view
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save()  # This additional save() is needed to save the tags
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form})

# Modify your existing post_update view
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the user is the author
    if post.author != request.user:
        return redirect('blog:post_detail', pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})