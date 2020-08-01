class Positionitem:
    id = None
    positionid = None           # 职位id，与position表id对应
    positionName = ''           # 工作名称
    companySize = ''            # 公司规模
    financeStage = ''           # 公司经济状况
    companyLabelList = ''       # 公司福利
    firstType = ''              # 需要什么类型的员工
    companyPosition = ''        # 公司地点  ，由json中的city和district拼接而成
    salary = ''                 # 薪水
    workYear = ''               # 需要工作经验
    city = ''                   # 工作城市
    district = ''               # 工作区域
    education = ''              # 学历
    companyFullName = ''        # 公司名称
    jobNature = ''              # 全职还是兼职
    createTime = ''             # 发布时间
    secondType = ''

    def __init__(self, id, positionid, positionName, companySize, financeStage, companyLabeList, firstType, companyPosition, salary, workYear, city, district, education, companyFullName, jobNature, createTime, secondType):
        self.id = id
        self.positionid = positionid
        self.positionName = positionName
        self.companySize = companySize
        self.financeStage = financeStage
        self.companyLabelList = companyLabeList
        self.firstType = firstType
        self.companyPosition = companyPosition
        self.salary = salary
        self.workYear = workYear
        self.city = city
        self.district = district
        self.education = education
        self.companyFullName =companyFullName
        self.jobNature = jobNature
        self.createTime = createTime
        self.secondType = secondType


    def __str__(self):
        return str(self.id) + "," + str(self.positionid) + "," + self.positionName + "," + self.companySize + "," + self.financeStage + "," + self.companyLabelList + "," + self.firstType + "," + self.companyPosition + "," + self.salary + "," + self.workYear + "," +self.city+","+self.district+","+self.education+","+self.companyFullName+","+self.jobNature+","+self.createTime+","+self.secondType
