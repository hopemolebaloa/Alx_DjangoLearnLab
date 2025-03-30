# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Post 
from .forms import PostForm
from taggit.models import Tag

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # Save the tags - django-taggit specific
            form.save_m2m()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the user is the author
    if post.author != request.user:
        return redirect('blog:post_detail', pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the user is the author
    if post.author != request.user:
        return redirect('blog:post_detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def tag_posts(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag.name)
    
    context = {
        'tag': tag,
        'posts': posts,
    }
    
    return render(request, 'blog/tag_posts.html', context)

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