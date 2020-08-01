from django.shortcuts import render
import os
import json
# Create your views here.
from pachong.getDataInfo import get_json_data
import os
# os.chdir("jingtai/json")
# json_obj = get_json_data()
import pachong.getData.get_data as get_data
json_obj = get_data.DbSelectAllPosition()


def info_show(request):

    # os.chdir("../../")

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
    from .xp_modules import getPositionSalaryDic, sortSalary, areaPosition
    salary = getPositionSalaryDic()
    salaryDic = salary[0]
    positionSalaryDic = salary[1]
    city = areaPosition(positionSalaryDic)
    cityList = city[0]
    cityNum = city[1]
    # salaryDicTemp = salaryDic
    # sortSalaryDic = sortSalary(salaryDicTemp)
    return render(request, "salaryPic.html", {'num': salaryDic["num"], "cityList": cityList, "cityNum": cityNum})

def member1(request):
    return render(request, "member-list.html", {"all_position": json_obj})

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


