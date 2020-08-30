from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='modify'),
    path('AddToCollection/', views.add_news, name='createMNews'),
    path('index', views.index, name='viewindex'),
    path('<int:pk>/Details/', views.details_mnews, name='MNewDetails'),
]