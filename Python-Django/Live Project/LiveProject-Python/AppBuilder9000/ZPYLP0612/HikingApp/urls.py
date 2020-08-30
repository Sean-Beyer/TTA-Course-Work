from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hiking'),
    path('AddHike/', views.add_hike, name='createHike'),
    path('myHikes/', views.index, name='listHikes'),
    path('myHikes/<int:pk>/Details/', views.details_hike, name='hikeDetails'),
    path('myHikes/<int:pk>/Edit/', views.edit_hike, name='editHike'),
    path('myHikes/<int:pk>/Edit/Delete', views.delete_hike, name='deleteHike'),
    path('AllTrails/', views.all_hikes, name='AllTrails'),
]