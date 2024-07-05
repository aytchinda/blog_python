from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Category, Tag, Post, Comment
from blog.forms.ContactForm import ContactForm  # Importer le formulaire
from django.contrib import messages

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
        "title":title, 
        "posts":posts, 
        })


def post(request):
    title = "Title : New post"
    return render(request, "blog/post.html",{"title":title})

def single_post(request,slug):
    post =  get_object_or_404(Post, slug=slug)
    return render(request, "blog/single_post.html",{"post": post})

def contact(request):
    if request.method == 'POST':
        #Traiter le formulaire
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a bien été envoyé')
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, "blog/components/contact.html" ,{"form":form})
