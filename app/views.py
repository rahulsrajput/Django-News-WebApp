from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def logout_page(request):
    pass





def dashboard(request):
    return render(request, 'dashboard/dashboard_page.html')

def add_post(request):
    return render(request, 'dashboard/add_post.html')

def edit_post(request):
    return render(request, 'dashboard/edit_post.html')



def news_home(request):
    return render(request, 'news_home.html')

def news_detail(request):
    return render(request, 'news_detail.html')

def about(request):
    return render(request, 'about.html')