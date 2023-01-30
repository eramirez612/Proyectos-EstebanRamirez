from django.urls import path
from . import views
from .views import GeneratePdf

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/', GeneratePdf.as_view(),name='pdf'), 

]