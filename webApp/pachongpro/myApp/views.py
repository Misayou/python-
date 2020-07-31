from django.shortcuts import render
import os
# Create your views here.
from pachong.getDataInfo import get_json_data
import os
os.chdir("jingtai/json")
json_obj = get_json_data()

def info_show(request):

    os.chdir("../../")
    return render(request, "info_show.html", {"all_position": json_obj})


def index(request):
    return render(request, "index.html")



def add(request):
    return render(request, "info_show.html", {"all_position": json_obj})


def delete(request):
    return render(request, "info_show.html", {"all_position": json_obj})


def update(request):
    return render(request, "info_show.html", {"all_position": json_obj})

def salaryPic(request):
    from .xp_modules import getPositionSalaryDic
    salaryDic = getPositionSalaryDic()
    return render(request, "salaryPic.html", {'num': salaryDic["num"]})

def member1(request):
    return render(request, "member-list.html")

def member2(request):
    return render(request, "member-list1.html")

def welcome(request):
    return render(request, "welcome.html")

def login(request):
    return render(request, "login.html")


def echarts1(request):
    return render(request, "echarts1.html")


def echarts2(request):
    return render(request, "echarts2.html")


def echarts3(request):
    return render(request, "echarts3.html")


def echarts4(request):
    return render(request, "echarts4.html")


def echarts5(request):
    return render(request, "echarts5.html")


def echarts6(request):
    return render(request, "echarts6.html")


