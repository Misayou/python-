import pachong.DB.DBoperation.positionDBcon as positionDBcon
import pachong.DB.DBoperation.positionItemDBcon as positionItemDBcon
import pachong.DB.DBclass.position as position
import pachong.DB.DBclass.positionitem as positionitem
import requests



# 爬取数据并将数据保存到数据库中

# 爬取拉勾网的职业信息，num代表第几页，positionname代表爬取的职业名称
def get_json(url, num, positionname):
    referer = 'https://www.lagou.com/jobs/list_python%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput='
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=',
    }
    data = {
        'first': 'true',
        'pn': num,
        'kd': positionname
    }

    # 建立session连接
    s = requests.Session()
    s.get(url=referer, headers = headers, timeout = 3)
    # 获取cookie
    cookie =s.cookies

    # 利用cookie进行动态爬取
    res = requests.post(url, headers = headers, data = data, cookies = cookie, timeout = 3)
    # 解决乱码
    res.raise_for_status()
    # 设置编码格式
    res.encoding = 'utf-8'
    return res.json()

# 查询总共有多少页，大于15页的即放弃返回15页，即数据库最多保存15页
def get_page_num(count):
    page_count = count / 15
    if page_count > 15:
        return 15
    else:
        return page_count

# 查询输入的职业的id
def selectId(name):
    return positionDBcon.select(name).id

# 将需要查询的职位数据存在数据库中，如果数据库中已存在该职位则不做处理，否则存入数据库  id=None代表数据库中已有该职业信息
def Dbopreate(psname, json):
    position1 = positionDBcon.select(psname)
    id = None
    if position1 != None:
        id = None
        print("数据库已有该职业的信息")
    else:
        positionDBcon.insert(psname)
        position2 = positionDBcon.select(psname)
        id = position2.id
    return id

# 将查询到的有关于该职业的全部信息保存到数据库中
def DbInsertPosition(json, id):
    positionInfo = json['content']['positionResult']['result']
    for one in positionInfo:
        if one['city'] == None:
            one['city'] = ''
        if one['district'] == None:
            one['district'] = ''
        fuli = ''
        for i in one['companyLabelList']:
            fuli += i + " "
        companyPosition = str(one['city']+one['district'])
        positionitem1 = positionitem.Positionitem(id, one['positionName'], one['companySize'], one['financeStage'], fuli, one['firstType'], companyPosition, one['salary'], one['workYear'])
        positionItemDBcon.insert(positionitem1)

# 通过positionitem表中的positionid获取到该职业的所有相关职位
def DbSelectAll(id):
    return positionItemDBcon.select(id)

def main():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    name = 'python工程师'
    # 第一次爬取，获取到第一页
    firstpage = get_json(url, 1, name)

    # 读取第一页中的信息，读出总共有多少个职位，并返回页数
    totalcount = firstpage['content']['positionResult']['totalCount']
    pagecount = get_page_num(totalcount)
    print(pagecount)
    # 利用读取到的页数多次爬取该网站
    id = Dbopreate(name, firstpage)
    for i in range(int(pagecount)):
        page = get_json(url, i, name)
        if id == None:
            break
        else:
            DbInsertPosition(page, id)
    id1 = selectId(name)

if __name__ == '__main__':
    main()

