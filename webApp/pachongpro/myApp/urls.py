from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index/info_show', views.info_show),
    path('add', views.add),
    path('delete', views.delete),
    path('update', views.update),
    path('salaryPic', views.salaryPic),
    path('index/echarts1.html', views.echarts1),
    path('index/echarts2.html', views.echarts2),
]
