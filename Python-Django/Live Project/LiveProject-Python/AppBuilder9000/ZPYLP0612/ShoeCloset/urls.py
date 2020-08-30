from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='ShoeCloset'),
    path('TheShoeCloset', views.index, name='TheShoeCloset'),
    path('addShoes', views.addShoes, name='addShoes'),
    path('TheShoeCloset/<int:pk>/Details', views.details_shoestyles, name='details'),

]
