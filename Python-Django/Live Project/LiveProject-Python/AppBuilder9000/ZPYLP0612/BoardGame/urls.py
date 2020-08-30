from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='bg_home'),
    path('addGame', views.addGame, name='bg_addGame'),
    path('collection', views.viewCollection, name='bg_viewCollection'),
    path('<int:pk>/detail', views.viewDetail, name='bg_viewDetail'),
    path('<int:pk>/edit', views.editDetail, name='bg_editDetail'),
    path('<int:pk>/delete', views.deleteDetail, name='bg_deleteDetail'),
    path('search/', views.search, name='bg_search'),
    path('<int:id>/addHot/', views.addHot, name='bg_addHot'),
    path('news/', views.news, name='bg_news'),
    ]
