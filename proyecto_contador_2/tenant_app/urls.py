"""proyecto_contador_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from tenant_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('lista/', views.TrabajadorList, name='lista'),
    path('lista-liquidacion/<int:id>/', views.LiquidacionList, name='lista-liquidacion'),
    path('lista-liquidaciones/', views.LiquidacionesList, name='lista-liquidaciones'),
    path('nuevo-trabajador/', views.nuevo_trabajador, name='nuevo-trabajador'),
    path('eliminar-trabajador/<int:id>', views.eliminarTrabajadores, name='eliminar-trabajador'),
    path('trabajador/<int:id>', views.detalle_trabajador, name='trabajador'),
    path('nueva-liquidacion/<int:id>', views.nueva_liquidacion, name='nueva-liquidacion'),
    path('datos-liquidacion/<int:id>', views.datos_liquidacion, name= 'datos-liquidacion'),
    path('pdf/<int:id>', views.liquidacion, name='pdf'),
]
