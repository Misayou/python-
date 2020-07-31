import pymysql
from pachong.getData.DB.DBclass.positionitem import Positionitem
import json

try:
    # 获得连接connect(链接主机，用户名，密码，数据库名)
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', db = 'pythonpc', charset = 'utf8')

    # 获取游标
    cursor = db.cursor()

except Exception as e:
    db.rollback()  # 实现事物的回滚
    print(e)

# 再表positionItem中插入数据
def insert(positionItem):
    sql = 'insert into positionitem(positionid, positionItemName, companySize, financeStage, companyLabelList, firstType, companyPosition, salary, workYear) VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(sql,(positionItem.positionid,positionItem.positionItemName,positionItem.companySize,positionItem.financeStage,positionItem.companyLabelList,positionItem.firstType,positionItem.companyPosition,positionItem.salary,positionItem.workYear))
    db.commit()
# 测试插入数据
# position = [1, '老总', '', '','', '', '', '', '']
# insert(position)

# 查询positionItem表中的所有数据
def select(positionId):
    sql = 'select * from positionitem where positionId = %s'
    cursor.execute(sql,positionId)
    positionitems = []
    data = cursor.fetchall()
    for one in data:
        # positionitem = Positionitem(one[0], one[1], one[2],one[3], one[4], one[5], one[6], one[7], one[8], one[9])
        positionitem = {}
        positionitem['id'] = one[0]
        positionitem['positionid'] = one[1]
        positionitem['positionItemName'] = one[2]
        positionitem['companySize'] = one[3]
        positionitem['financeStage'] = one[4]
        positionitem['companyLabeList'] = one[5]
        positionitem['firstType'] = one[6]
        positionitem['companyPosition'] = one[7]
        positionitem['salary'] = one[8]
        positionitem['workYear'] = one[9]

        positionitems.append(positionitem)
    resultdata = json.dumps(positionitems, ensure_ascii=False)
    return resultdata[1:len(resultdata)-1]
# # 测试查找,，返回结果类似于这样[<DBclass.positionitem.Positionitem object at 0x000001CA5E608C08>, <DBclass.positionitem.Positionitem object at 0x000001CA5E6178C8>
# i = select(1)
# # for one in i:
# #     print(one.positionid)
# print(i)

def selectAllPosition():
    sql = 'select * from positionitem'
    cursor.execute(sql)
    positionitems = []
    data = cursor.fetchall()
    for one in data:
        # positionitem = Positionitem(one[0], one[1], one[2],one[3], one[4], one[5], one[6], one[7], one[8], one[9])
        positionitem = {}
        positionitem['id'] = one[0]
        positionitem['positionid'] = one[1]
        positionitem['positionItemName'] = one[2]
        positionitem['companySize'] = one[3]
        positionitem['financeStage'] = one[4]
        positionitem['companyLabeList'] = one[5]
        positionitem['firstType'] = one[6]
        positionitem['companyPosition'] = one[7]
        positionitem['salary'] = one[8]
        positionitem['workYear'] = one[9]
        positionitems.append(positionitem)
    resultdata = json.dumps(positionitems, ensure_ascii=False)
    return resultdata[1:len(resultdata) - 1]