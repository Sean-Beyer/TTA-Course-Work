from django.urls import path

from .import views


urlpatterns = [
    path('', views.home, name='PhotoApp'),
    # path('ApiService/', views.Photo, name='Find Photoghapher'),
    # path('Bookings/', views.Time, name='Time of Day'),
    path('Genre/', views.index, name='Genre of Photography'),
    # path('Style/', views.albums, name='Photographers Albums'),               #List of Albums
    # path('Book/', views.book, name='Book a Photoghapher'),    #add photographer
    path('Album/', views.add_photo, name='PhotoAlbum'),
    path('Genre/<int:pk>/', views.Photo_Album, name='photoDetails'), #get details for a Photo
    # path('Details/<int:photo>/Edit', views.edit_photo, name='editDetails'),
    # path('Details/<int:photo>/View/', views.view_photo, name='ViewDetails'),
]