from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def start(request):
    posts = ["1", "2", "3", "44"]
    return render(request, 'reg/home.html', context={"posts": posts})
    # добавить импорт постов в бд
def registr_page(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save( )
    context={'form':form}
    return render(request, 'reg/registration.html', context)


def loginn(request):
    context={}
    return render(request, 'reg/login_page.html', context)



def show_posts(request):
    posts = Post.objects.all()
    return render(request,'reg/posts.html', context={'items':posts})
