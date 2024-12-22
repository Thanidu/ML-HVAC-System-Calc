from django.urls import path
from . import views

urlpatterns = [
  #path('', views.index, name='index'),  # Home page
    path('', views.chiller_input, name='chiller_input'),  # URL for the input form
]