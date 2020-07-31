import pymysql
from DBclass.position import Position

try:
    # 获得连接connect(链接主机，用户名，密码，数据库名)
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', db = 'pythonpc', charset = 'utf8')

    # 获取游标
    cursor = db.cursor()

except Exception as e:
    db.rollback()  # 实现事物的回滚
    print(e)

def select(positionName):
    sql = 'select * from position where positionName = %s'
    cursor.execute(sql, positionName)
    data = cursor.fetchone()
    position = Position(data[0], data[1])

    # 测试查询结果
    print(type(position))
    print(position)
    print(position.positionName)
    return position

select('test')
