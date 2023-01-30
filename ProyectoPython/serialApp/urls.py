from django.urls import path
from . import views
from .views import GenerarPDF

urlpatterns = [
    path('persona/', views.personadata),
    path('pdf/', GenerarPDF.as_view(),name='pdf'), 
    path('', views.index, name='index'),
    path('proyectos/', views.listadoproyectos),
    path('agregarproyecto/', views.agregarproyecto),
    path('eliminarProyecto/<int:id>', views.eliminarProyecto),
    path('actualizarProyecto/<int:id>', views.actualizarProyecto),
]
