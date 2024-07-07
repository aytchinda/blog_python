from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Category, Tag, Post, Comment
from blog.forms.ContactForm import ContactForm  # Importer le formulaire
from blog.forms.PostForm import PostForm  # Importer le formulaire
from django.contrib import messages
import os

# Create your views here.
def index(request):
    title = "Hello World" 
    posts = Post.objects.all()
    
    paginator = Paginator(posts, 8)
    page = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except:
        posts = paginator.page(1)
    
    return render(request, "blog/index.html",{
        "title": title, 
        "posts": posts, 
    })


def post(request):
    title = "Title : New post"
    return render(request, "blog/post.html", {"title": title})

def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/single_post.html", {"post": post})

def contact(request):
    if request.method == 'POST':
        # Traiter le formulaire
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a bien été envoyé')
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, "blog/components/contact.html", {"form": form})

@login_required
def dashboard_post(request):
    posts = Post.objects.filter(author=request.user)
    
    paginator = Paginator(posts, 8)
    page = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except:
        posts = paginator.page(1)
    
    return render(request, "blog/dashboard/post_index.html", { "posts": posts,})

@login_required
def dashboard_post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/dashboard/post_view.html", {"post": post})

@login_required
def dashboard_post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Votre article a bien été créé")
            return redirect('dashboard_post')
    else: 
        form = PostForm()
    return render(request, "blog/dashboard/post_new.html", {"form": form})

@login_required
def dashboard_post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre article a bien été modifié")
            return redirect('dashboard_post')
    else:
        form = PostForm(instance=post)
    
    return render(request, "blog/dashboard/post_new.html", {"form": form, "post": post})

@login_required
def dashboard_post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if post.author != request.user:
        messages.error(request, "Vous n'avez pas le droit de supprimer cet article")
        return redirect('dashboard_post')

    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            if post.image:
                image_path = post.image.path
                if os.path.exists(image_path):
                    os.remove(image_path)
            post.delete()
            messages.success(request, "Votre article a bien été supprimé")
            return redirect('dashboard_post')
    
    return render(request, "blog/dashboard/post_confirm_delete.html", {"post": post})
