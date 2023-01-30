from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('model', views.select_model, name='model')
]
