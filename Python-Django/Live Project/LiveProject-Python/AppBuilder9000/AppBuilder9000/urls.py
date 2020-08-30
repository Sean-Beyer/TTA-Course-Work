"""AppBuilder9000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('SoccerApp/', include('SoccerApp.urls')),  # sign url path for my app
    path('BasketballApp/', include('BasketballApp.urls')),
    path('SpendUs/', include('SpendUsApp.urls')), # added path to Spend US App
    path('SFToons/', include('SFToons.urls')),
    path('EarningsApp', include('EarningsApp.urls')),
]
#urlpatterns +=staticfiles_urlpatterns()
