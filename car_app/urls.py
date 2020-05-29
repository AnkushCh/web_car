"""car_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from car_app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('products', views.products, name='product'),
    path('store', views.store, name='store'),
    path('reviews', views.loc, name='location'),
    path('codeofethics', views.loc, name='location'),
    path('repairservice', views.loc, name='location'),
    path('customerservice', views.loc, name='location'),
    path('tires', views.loc, name='location'),
    path('contactus', views.loc, name='location'),
    path('generalmaintance', views.loc, name='location'),
    path('buytires', views.loc, name='location'),
    path('buytires', views.loc, name='location'),
    path('buytires', views.loc, name='location'),

]
