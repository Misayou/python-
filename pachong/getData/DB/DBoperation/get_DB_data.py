import pymysql
import json
import pymysql

# 获取连接
con = pymysql.connect(host='localhost', user='root', password='root', db='pythonpc', charset='utf8')
# 获取游标
cur = con.cursor()
# 执行sql
cur.execute("select * from positionitem")
# 结果集
rs = cur.fetchall()
obj = []
# print()
# 循环输出结果
for one in rs:
    # one 代表的是一条数据，有多个字段，按如下格式打印
    result = {
        'companyShortName': one[0],
        'companySize': one[3],
        'area': one[7],
        'positionName': one[0],
        'firstType': one[6],
        'secondType': one[0],
        'jobNature': one[0],
        'education': one[0],
        'workYear': one[9],
        'salary': one[8],
        'time': one[0]
    }
    obj.append(result)
    # print(result['area'])
# print(obj)
# jsondatar=json.dumps(obj,ensure_ascii=False)
#去除首尾的中括号
# json_obj = jsondatar[1:len(jsondatar)-1]
# print(json_obj)
