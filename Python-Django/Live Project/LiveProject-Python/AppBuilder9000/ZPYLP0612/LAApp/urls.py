from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='LAApp'),
    path('Collection/', views.index, name='listAuthors'),
    path('AddToCollection/', views.add_author, name='createAuthor'),
    path('Collection/<int:pk>/Details/', views.details_author, name='authorDetails'),
    path('Collection/<int:pk>/Edit/', views.edit_author, name="editAuthors"),
    path('Collection/<int:pk>/ConfirmDelete', views.delete, name="confirm"),
    path('PublishedWorks/DataScrape', views.data_Scrape, name="scrape"),
    path('OpenLibrary/API', views.OpenLib_API, name="olAPI")
]