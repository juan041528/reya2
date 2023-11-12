"""
URL configuration for reya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="index"),
    path('crear/', views.crear, name="Crear"),
    path('comida1/', views.comida1, name="comida1"),
    path('comida2/', views.comida2, name="comida2"),
    path('comida3/', views.comida3, name="comida3"),
    path('prueba/', views.prueba),
    path('perfil/', views.perfil, name="perfil"),
    
    path('menu/', views.menu, name="logged"),
    
]