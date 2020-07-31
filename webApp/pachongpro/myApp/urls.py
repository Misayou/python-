from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('info_show', views.info_show),
    path('add', views.add),
    path('delete', views.delete),
    path('update', views.update)
]
