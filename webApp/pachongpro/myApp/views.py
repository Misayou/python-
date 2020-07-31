from django.shortcuts import render
import os
import json
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

