from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Home Page View - shows all blog posts
def home(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})

# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Create New Blog Post (Login Required)
@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# View Single Blog Post
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

# Edit Existing Blog Post (Login Required)
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

# Delete Blog Post (Login Required)
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-home')
    return render(request, 'blog/delete_post.html', {'post': post})
