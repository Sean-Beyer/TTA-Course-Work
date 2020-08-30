from django.urls import path
from . import views

urlpatterns = [
    path('', views.toons_home, name='toons'),
    path('Roster/', views.toons_index, name='listToons'),
    path('AddToCharacter/', views.add_character, name='createCharacter'),
    path('Roster/<int:pk>/Details/', views.details_character, name='characterDetails'),
    path('Roster/<int:pk>/Edit/', views.edit_character, name="characterEdit"),
    path('Roster/<int:pk>/Edit/Delete/', views.delete_character, name="characterDelete"),
    path('BlogPosts/', views.blog_update, name='gameUpdates'),
    path('SFSRD/', views.sf_api, name='characterOptions'),
    # path('SFSRD/<int:pk>/', views.Items, name='item_list'),
    # path('ajax/load-item/', views.load_item, name='ajax_load_item')
]