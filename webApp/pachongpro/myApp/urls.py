from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/info_show.html', views.info_show),
    path('add', views.add),
    path('delete', views.delete),
    path('update', views.update),
    path('salaryPic', views.salaryPic),

    path('index/', views.index),
    path('index/login.html', views.login),
    path('index/welcome.html', views.welcome),
    path('index/member-list.html', views.member1),
    path('index/member-list1.html', views.member2),
    path('index/echarts1.html', views.echarts1),
    path('index/echarts2.html', views.echarts2),
    path('index/echarts3.html', views.echarts3),
    path('index/echarts4.html', views.echarts4),
    path('index/echarts5.html', views.echarts5),
    path('index/echarts6.html', views.echarts6),
    # path('salaryPic/', views.salaryPic),
]
