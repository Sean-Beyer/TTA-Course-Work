from django.urls import path
from . import views


# URL Patterns

urlpatterns = [
    path('', views.home, name='GreatestComedies'),                      #Home page
    path('AddComedy/', views.add_comedy, name='addComedy'),              #add new Comedy
    path('Comedies/', views.index, name='listComedy'),                   #index of Comedy
    path('Comedies/<int:pk>/Details/', views.details_comedy, name='comedyDetails'),  # get details for a comedy
]
