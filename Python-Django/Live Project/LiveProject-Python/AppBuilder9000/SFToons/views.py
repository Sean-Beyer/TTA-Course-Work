from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from .forms import CharacterForm
import requests
from bs4 import BeautifulSoup as BS
import json


def toons_home(request):
    return render(request, 'SFToons/toons_home.html')

def toons_index(request):
    get_characters = Character.Characters.all()
    context = {'characters': get_characters}
    return render(request, 'SFToons/toons_index.html', context)

def add_character(request):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('toons')
    else:
        print(form.errors)
        form = CharacterForm()
    return render(request, 'SFToons/toons_create.html', {'form':form})


def details_character(request, pk):
    pk = int(pk)
    character = get_object_or_404(Character, pk=pk)
    context={'character':character}
    return render(request,'SFToons/toons_details.html', context)


def edit_character(request, pk):
    pk = int(pk)
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save()
            character.save()
            return redirect('characterDetails', pk=character.pk)
    else:
        form = CharacterForm(instance=character)
    context = {'form': form, 'pk': pk, 'character': character.Character_Name}
    return render(request, 'SFToons/toons_edit.html', context)


def delete_character(request, pk):
    pk = int(pk)
    character = Character.Characters.get(pk=pk)
    character.delete()
    return redirect('listToons')


def blog_update(request):
    source = requests.get("https://www.tabletopgamingnews.com/tag/rpg")
    print(source.status_code)
    soup = BS(source.content, 'html.parser')
    divs = soup.find_all("div", {"class": "expandablepost"}) # Posts on sites are arranged by div tags
    # images = BS.find_all("class": "expandablepostimage"})
    posts = []
    for div in divs:
        if div != None:
            # images = div.find("div", {"class": "expandablepostimage"}).get('img src')
            title = div.find("div", {"class": "expandableposttitle"}).get_text()
            link = div.find('a').get('href')
            date = div.find('div', {"class": "expandablepostdate"}).get_text()
            url = "https://www.tabletopgamingnews.com/" + link
            summary = div.find("div", {"class": "expandablesummary"}).get_text()
            post={'title':title, 'url': url, 'summary':summary, 'date': date}
            posts.append(post)
        else:
            print('no value')
    context={'posts': posts}
    return render(request, 'SFToons/toons_updates.html', context)




def sf_api(request):
    weapon_list = []

    # options = {"title": "Baton, Tactical"}
    response = requests.get('https://api.starfinder.dragonlash.com/weapons/')
    data = response.json()
    # name = request.GET.get('title')
    # item = data['results']
    # print(item[0])
    for item in data['results']:
        name = item['title']
        bulk = item['bulk']
        price = item['price']
        level = item['item_level']
        damage = item['damage']
        range = item['range']
        critical = item['critical']
        special = item['special']
        capacity = item['capacity']
        usage = item['usage']
        description = item['description']
        weapon = {'title': name, 'level': level, 'price': price, 'bulk': bulk, 'damage': damage, 'range': range, 'critical': critical, 'special': special, 'capacity': capacity, 'usage': usage, 'description': description}
        # print(json.dumps(weapon, indent = 4))
        weapon_list.append(weapon)
        if request.method == 'POST':
            choice = request.POST['title']
            weapon_list = choice
    context = {'weapon': weapon_list}
    return render(request, 'SFToons/toons_srd.html', context)


# def Items(ListView):
#     model = Items
#     context_object_name = 'item'
#     success_url = reverse_lazy
#
#
# def load_item(request):
#     name = request.GET.get('name')
#     item = Items.objects.filter(item=item).order_by('name')
#     return render(request, 'SFToons/toons_srd.html', {'item': item})