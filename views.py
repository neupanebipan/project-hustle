from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#importing important fuunctions from djagno for post blogs
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForms


def home(request):
    return render(request, 'accounts/index.html')

@login_required(login_url='login')
def program(request):
    return render(request, 'accounts/programs.html')

def videos(request):
    return render(request, 'accounts/videos.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def services(request):
    return render(request, 'accounts/services.html') 

@login_required(login_url='login')
def trainers(request):
    return render(request, 'accounts/trainers.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

#blogs post requirment functions and classes
class homeview(ListView):
    model = Post
    template_name = "accounts/blogs.html"

class articledetailview(DetailView):
    model = Post
    template_name = "accounts/article_details.html"

class postview(CreateView):
    model = Post
    form_class = PostForms
    template_name = "accounts/add_post.html"

class updatepost(UpdateView):
    model=Post
    template_name = 'accounts/update_post.html'
    fields = ['title', 'title_tag', 'body']