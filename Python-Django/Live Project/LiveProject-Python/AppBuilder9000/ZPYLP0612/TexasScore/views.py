from django.shortcuts import render, redirect, get_object_or_404
from .models import TexasGame
from .forms import TexasForm

# Create your views here.
from .models import TexasGame


def texasadmin(request):
    return render(request, 'TexasScore/TexasScore_home.html')


def index(request):
    get_games = TexasGame.TexasGames.all()
    context = {'games': get_games}
    return render(request, 'TexasScore/TexasScore_index.html', context)


def create_game(request):
    form = TexasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('giveGames')
    else:
        print(form.errors)
        form = TexasForm()
    return render(request, 'TexasScore/TexasScore_create.html', {'form': form})


def game_details(request, pk):
    pk = int(pk)
    game = get_object_or_404(TexasGame, pk=pk)
    context={'game': game}
    return render(request, 'TexasScore/TexasScore_details.html', context)
