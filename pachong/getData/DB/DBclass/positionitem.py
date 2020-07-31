class Positionitem:
    id = None
    positionid = None           # 执谓id，与position表id对应
    positionItemName = ''       # 工作名称
    companySize = ''            # 公司规模
    financeStage = ''           # 公司经济状况
    companyLabelList = ''        # 公司福利
    firstType = ''              # 需要什么类型的员工
    companyPosition = ''        # 公司地点  ，由json中的city和district拼接而成
    salary = ''                 # 薪水
    workYear = ''               # 需要工作经验

    def __init__(self, id, positionid, positionItemName, companySize, financeStage, companyLabeList, firstType, companyPosition, salary, workYear):
        self.id = id
        self.positionid = positionid
        self.positionItemName = positionItemName
        self.companySize = companySize
        self.financeStage = financeStage
        self.companyLabelList = companyLabeList
        self.firstType = firstType
        self.companyPosition = companyPosition
        self.salary = salary
        self.workYear = workYear



    def __str__(self):
        return str(self.positionid) + "," + self.positionItemName + "," + self.companySize + "," + self.financeStage + "," + self.companyLabelList + "," + self.firstType + "," + self.companyPosition + "," + self.salary + "," + self.workYear
