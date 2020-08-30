
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import requests
from .models import Hikes
from .forms import HikeForm
# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as BS #necessary for datascraping
# Create your views here.


def index(request):
    get_hikes = Hikes.Hikes.all()      #Gets all the current hike from the database
    context = {'hikes': get_hikes}      #Creates a dictionary object of all the hikes for the template
    return render(request, 'HikingApp/Hiking_index.html', context)


def home(request):
    return render(request, 'HikingApp/Hiking_home.html')


def add_hike(request):
    form = HikeForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/hike to the database
        return redirect('listHikes')                #Redirects to the index page, which is named '' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = HikeForm()
    #Creates a new blank form
    return render(request, 'HikingApp/Hiking_create.html', {'form': form})


def details_hike(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    hike = get_object_or_404(Hikes, pk=pk)   #Gets single instance of the Hike from the database
    context = {'hike': hike}                   #Creates dictionary object to pass the hike object
    return render(request, 'HikingApp/Hiking_details.html', context)


def edit_hike(request, pk):
    pk = int(pk)
    hike = get_object_or_404(Hikes, pk=pk)
    if request.method == 'POST':
        form = HikeForm(request.POST, instance=hike)
        if form.is_valid():
            hike = form.save()
            hike.save()
            return redirect('hikeDetails', pk=hike.pk)
        else:
            print(form.errors)
            form = HikeForm(instance=hike)
    else:
        form = HikeForm(instance=hike)
        context = {'form': form, 'pk': pk}
        return render(request, 'HikingApp/Hiking_Edit.html', context)


def delete_hike(request, pk):
    pk = int(pk)
    hike = get_object_or_404(Hikes, pk=pk)
    if request.method == 'POST':
        hike.delete()
        return redirect('listHikes')
    context = {'hike': hike, 'pk': pk}
    return render(request, 'HikingApp/Hiking_delete.html', context)


def all_hikes(request):
    source = requests.get("https://www.alltrails.com/us")  # Get https://www.alltrails.com/us as an html document
    print(source.status_code)
    soup = BS(source.content, 'html.parser')
    nodes = soup.find_all("div", class_="styles-module__trailCard___2oHiP")
    topHikes = []
    for node in nodes:
        title = node.find('a', class_="xlate-none styles-module__link___12BPT").get_text()#get title of hikes
        link = node.find('a', class_="xlate-none styles-module__link___12BPT").get('href') #get link to that hike
        url = "https://www.alltrails.com" + link #url to hike
        hike ={'title': title, 'url': url}
        topHikes.append(hike)
    context = {'topHikes': topHikes}
    return render(request, 'HikingApp/all_trails.html', context)
