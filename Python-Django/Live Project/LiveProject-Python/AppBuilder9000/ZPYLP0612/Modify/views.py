from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import requests
from .models import MNews
from .forms import MNewsForm
# from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'Modify/Modify_home.html')

def index(request):
    get_MNews = MNews.MNews.all()
    context = {'mnews': get_MNews}
    return render(request, 'Modify/Modify_index.html', context)


def add_news(request):
    form = MNewsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('modify')
    else:
        print(form.errors)
        form = MNewsForm()
    return render(request, 'Modify/Modify_create.html', {'form':form})

def details_mnews(request, pk):
    pk = int(pk) #
    mnews = get_object_or_404(MNews, pk=pk) #
    context={'mnews':mnews} #
    return render(request,'Modify/Modify_details.html', context) #