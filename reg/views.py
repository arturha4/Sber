from django.shortcuts import render
from django.http import HttpResponse
from.models import Post
def start(request):
    posts = ["1", "2", "3", "44"]
    return render(request, 'reg/cards.html',context={"posts":posts})

def reg(request):
    return HttpResponse('LAter...')

