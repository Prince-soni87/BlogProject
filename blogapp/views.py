from django.shortcuts import render, redirect
from .forms import PostForm, UserRegistrationForm
from .models import Post    
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts=Post.objects.all().order_by('-created_at')
        else:
            posts=Post.objects.filter(author=request.user).order_by('-created_at')
    else:
        posts=Post.objects.all().order_by('-created_at')
    return render(request, 'blogapp/home.html', {'posts': posts})

def signup(request):
    pass    
def create_post(request):
    pass        
def post_detail(request, post_id):
    pass