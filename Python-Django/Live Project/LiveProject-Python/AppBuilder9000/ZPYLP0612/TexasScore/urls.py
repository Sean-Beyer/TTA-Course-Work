from django.urls import path
from . import views

urlpatterns = [
    path('', views.texasadmin, name='texasadmin'),
    path('Games/', views.index, name='giveGames'),
    path('AddGame/', views.create_game, name='createGame'),
    path('Games/<int:pk>/Details/', views.game_details, name='gameDetails'),
]
