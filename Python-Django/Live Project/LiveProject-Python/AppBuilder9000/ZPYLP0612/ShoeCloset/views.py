from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoeClosetModel
from .forms import ShoeClosetForm
from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'ShoeCloset/shoecloset_home.html')


def addShoes(request):
    form = ShoeClosetForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('TheShoeCloset')
    else:
        print(form.errors)
        form = ShoeClosetForm()
    return render(request, 'ShoeCloset/shoecloset_create.html', {'form': form})


def index(request):
    get_shoes = ShoeClosetModel.Shoes.all()
    context = {'shoes': get_shoes}
    return render(request, 'ShoeCloset/shoecloset_index.html', context)


def appbuilderhome(request):
    return render(request, 'AppBuilder9000/templates/Home/index.html')


def details_shoestyles(request, pk):
    pk = int(pk)
    shoestyles = get_object_or_404(ShoeClosetModel, pk=pk)
    context = {'shoestyles': shoestyles}
    return render(request, 'ShoeCloset/shoecloset_details.html', context)
