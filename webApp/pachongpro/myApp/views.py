from django.shortcuts import render
import os
# Create your views here.
# from pachong.getDataInfo import get_json_data
# import os
# os.chdir("jingtai/json")
# json_obj = get_json_data()
from pachong.getData import get_data
json_obj = get_data.DbSelectAllPosition()

def info_show(request):
    os.chdir("../../")
    return render(request, "info_show.html", {"all_position": json_obj})


def index(request):
    return render(request, "index.html")



def add(request):
    positionitem = {'positionName': request.GET['4name'], 'companySize': request.GET['2name'],
                    'firstType': request.GET['5name'], 'salary': request.GET['10name'],
                    'workYear': request.GET['9name'], 'city': request.GET['3name'], 'district': '',
                    'education': request.GET['8name'], 'companyFullName': request.GET['1name'],
                    'jobNature': request.GET['7name'], 'createTime': request.GET['11name'],
                    'secondType': request.GET['6name']}
    json_obj.append(positionitem)
    return render(request, "member-list.html", {"all_position": json_obj})


def delete(request):
    json_obj.remove(request.GET["positionitem"])
    return render(request, "member-list.html", {"all_position": json_obj})


def update(request):
    return render(request, "info_show.html", {"all_position": json_obj})


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


def education(request):
    return render(request, "education.html")


def welfare(request):
    return render(request, "welfare_wordCloud.html")


def echarts5(request):
    return render(request, "echarts5.html")


def echarts6(request):
    return render(request, "echarts6.html")


def select(request):
    name = request.GET['position_name']
    company = request.GET['company']
    area = request.GET['area']
    obj = []
    for one in json_obj:
        if name in one["positionName"] and company in one["companyFullName"] and area in one["city"]+one["district"]:
            obj.append(one)
    return render(request, "member-list.html", {"all_position": obj})
