from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .forms import ContactForm
from .forms import SearchForm
from  .models import  CreateContact
import requests                     #necessary for datascraping
from bs4 import BeautifulSoup as BS #necessary for datascraping
import json




def post_new(request, pk):
    pk = int(pk)
    contact = get_object_or_404(CreateContact, pk=pk)
    form = ContactForm(request.POST or None , instance=contact)
    if form.is_valid():
        print(form)
        form.save()
        return redirect('listNames')
    return render(request, 'BasketballApp/BasketballApp_edit.html', {'form': form}, {'contact': contact})

def createRecord(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form)
        form.save()
        return redirect('create')
    else:
        print(form.errors)
        print("Form not saved")
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'BasketballApp/BasketballApp_create.html', context)


def home(request):
    return render(request, 'BasketballApp/BasketballApp_home.html')

def matches(request):
    return render(request, 'BasketballApp/BasketballApp_searchGame.html')

def gameSchedule(request):
    return render(request, 'BasketballApp/BasketballApp_gameSchedule.html')

def detailsPage(request):
    return render(request, 'BasketballApp/BasketballApp_details.html')

def deletePage(request):
    return render(request, 'BasketballApp/BasketballApp_delete.html')

def index(request):
    get_contact = CreateContact.CreateContacts.all()
    context = {'CreateContact': get_contact}
    return render(request, 'BasketballApp/BasketballApp_index.html', context)

def details_contact(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    contact = get_object_or_404(CreateContact, pk=pk)   #Gets single instance of the jersey from the database
    context={'contact':contact}                   #Creates dictionary object to pass the jersey object
    return render(request,'BasketballApp/BasketballApp_details.html', context)


def confirmed(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('BasketballApp/BasketballApp_create.html')
        else:
            return redirect('BasketballApp/BasketballApp_create.html')

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(CreateContact, pk=pk)
    print(pk)
    print(item)
    if request.method == 'POST':
        item.delete()
        return redirect('schedule')
    else:
        print("Form not saved")
    context = {'item': item,}
    return render(request, "BasketballApp/BasketballApp_delete.html", context)



#View function for data scraping the MLS website for current news stories
def nba_news(request):
    source = requests.get("https://www.cbssports.com/nba/")
    print(source.status_code)
    soup = BS(source.content, 'html.parser')
    nodes = soup.find_all(class_="article-list-pack-title col-4")
    articles = []
    for node in nodes:
        title = node.find('a').get_text()
        link = node.find('a').get('href')
        url = "https://www.cbssports.com" + link
        article = {'title': title, 'url': url}
        articles.append(article)
        context = {'articles': articles}
    return render(request, 'BasketballApp/BasketballApp_gameSchedule.html', context)

def nba_schedule(request):
    source = requests.get("https://www.barstoolsports.com")  # Get MLSSoccer.com/news as an html document
    print(source.status_code)
    soup = BS(source.content, 'html.parser')
    nodes = soup.find_all(class_="jsx-3558248627 storyCard__content")
    schedules = []
    for node in nodes:
        title = node.find('a').get_text()
        link = node.find('a').get('href')
        url = "https://www.barstoolsports.com" + link
        schedule = {'title': title, 'url': url}
        schedules.append(schedule)
        contexts = {'schedules': schedules}
    return render(request, 'BasketballApp/BasketballApp_gameTime.html', contexts)


def get_stats(request):
    form = SearchForm(request.POST or None)
    text = form['search']
    if form.is_valid():
        text = form.cleaned_data['search']
    print(form)
    url = "https://free-nba.p.rapidapi.com/players"

    querystring = {"page": "0", "per_page": "25", "search": text}

    headers = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': "28434cc292mshafa3b7b60da8d59p1c9445jsn13e32d3d719f"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    obj = json.loads(response.text)
    print(json.dumps(obj, indent=4))



    return render(request, 'BasketballApp/BasketballApp_space.html', {'form': form, 'text': text, 'obj': obj})
