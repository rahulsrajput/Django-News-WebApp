from django.shortcuts import render
from .models import Category, Article
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import login_form,signup_form

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        if request.method == 'POST':
            form = login_form(request, data=request.POST)
            if form.is_valid():
                uname = request.POST['username']
                upass = request.POST['password']
                user_obj = authenticate(username=uname, password=upass)
                if user_obj is not None:
                    login(request, user_obj)
                    return HttpResponseRedirect('/')

        form = login_form()
    return render(request, 'login.html', context={'form':form})

def signup_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        if request.method == 'POST':
            form = signup_form(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login')
            
        form = signup_form()
    return render(request, 'signup.html', context={"form":form})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')




def dashboard(request):
    return render(request, 'dashboard/dashboard_page.html')

def add_post(request):
    return render(request, 'dashboard/add_post.html')

def edit_post(request):
    return render(request, 'dashboard/edit_post.html')



def news_home(request):
    category_filter = request.GET.get('category')
    search = request.GET.get('search')
    print(search)

    if category_filter is not None:
        articles = Article.objects.filter(category__name=category_filter)

    elif search is not None:
        articles = Article.objects.filter(title__icontains=search)
    
    else:
        articles = Article.objects.all()

    categories = Category.objects.all()
    return render(request, 'news_home.html',context={'categories':categories,'articles':articles})

def news_detail(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'news_detail.html',context={'article':article})

def about(request):
    return render(request, 'about.html')