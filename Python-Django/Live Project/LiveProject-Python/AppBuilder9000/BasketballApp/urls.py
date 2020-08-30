from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='basketball'),  #home page
    path('deletePage/', views.deletePage, name='deletePage'),
    path('create/', views.createRecord, name='create'),  # specific league page for matches
    path('schedule/', views.gameSchedule, name='schedule'),  # specific league page for matches
    path('allData/', views.index, name='listNames'),  # specific league page for matches
    path('allData/<int:pk>/details/', views.details_contact, name='details'),  # get details for a single jersey
    path('detailshome/', views.detailsPage, name='detailshome'),  # specific league page for matches
    path('allData/<int:pk>/details/deletePage/', views.delete, name='delete'),
    path('allData/<int:pk>/details/post_new/', views.post_new, name='post_new'),
    path('NBAnews/', views.nba_news, name='NBAnews'),
    path('NBAnews/NBAschedule/', views.nba_schedule, name='NBAschedule'),
    path('viewss/', views.get_stats, name='viewss'),

]


