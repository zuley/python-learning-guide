from openpyxl import load_workbook, Workbook
from openpyxl.utils import get_column_letter, column_index_from_string
import time

# 获取文件
doc = load_workbook('应收历史回款统计表-2.xlsx', data_only=True)

# 计算开始索引和结束索引
start_index = column_index_from_string('G') - 1
end_index = column_index_from_string('AH') - 1

# 客户名称索引
name_index = column_index_from_string('D') - 1

# 打开工作表
a_sheet = doc['历史应收周转表']

huikuanTitle = [
    '1月内回款',
    '2月内回款',
    '3月内回款',
    '4月内回款',
    '5月内回款',
    '6月内回款',
    '7月内回款',
    '8月内回款',
    '9月内回款',
    '10月内回款',
    '11月内回款',
    '12月内回款',
    '13月内回款'
]

# 过滤数据表
nameFilter = [
    '国药控股吉林医疗器械有限公司',
    '龙山县人民医院',
    '泊头市医院'
]


# 函数：获取日期列表
def getDateTitle ():
    sList = list(a_sheet.rows)[1]
    arr = {}
    for index in range(start_index, end_index, 2):
        arr[index] = sList[index].value
    return arr

# 函数：计算回款
def getHuikuan (add, reduce, name):
    data = []
    # 全部增加数
    allAdd = 0
    # 遍历增加，以每一个增加为一行数据
    for index, item in enumerate(add):
        if name in nameFilter: break
        allAdd += item['add']
        # 全部减少数
        allReduce = 0
        # 状态
        status = False
        # 定义数据行
        row = {}
        # 设置名称
        row['name'] = name
        # 当前增加的日期
        nowYear = item['date'].year
        nowMonth = item['date'].month
        row['date'] = '%s年%s月' % (nowYear, nowMonth)
        # 当期增加
        row['add'] = item['add']
        # 遍历减少，计算回款
        for rindex, reduceItem in enumerate(reduce):
            allReduce += reduceItem['reduce']
            # 回款日期
            rYear = reduceItem['date'].year
            rMonth = reduceItem['date'].month
            # 计算回款间隔
            if rYear > nowYear:
                num = 12 - nowMonth + rMonth
            else:
                num = rMonth - nowMonth
                if num < 0 or rYear < nowYear: num = 0
            for n in range(0, num):
                if huikuanTitle[n] not in row:
                    row[huikuanTitle[n]] = 0
            # 回款差额
            nChae = allReduce - allAdd
            if name == '北镇市中医院':
                print('距离几个月', num, item['date'], reduceItem['date'])
                print('回款差额', round(1 + nChae/item['add'], 6))
            # 当减少数大于增加数的时候，回款率为1，此循环结束
            if nChae >= 0:
                row[huikuanTitle[num]] = 1
                break
            elif nChae < 0 and nChae + item['add'] < 0:
                nHuikuanlv = 0
                row[huikuanTitle[num]] = nHuikuanlv
            else:
                nHuikuanlv = round(1 + nChae/item['add'], 6)
                row[huikuanTitle[num]] = nHuikuanlv
        data.append(row)
        if name == '北镇市中医院':
            print('北镇市中医院')
            for item in add: print(item)
            print('-')
            for item in reduce: print(item)
            print(row)
    return data


dateTitle = getDateTitle()
newSheet = []

for row in list(a_sheet.rows)[3:137]:
    # 客户名称
    name = row[name_index].value
    # 存储本期增加的资金列表
    nowDateAdd = []
    nowDateReduceNum = []
    # 遍历行
    for index in range(start_index, end_index, 2):
        # 取得本期增加
        addNum = row[index].value
        if addNum == '-' or not addNum:
            addNum = 0
        # 如果大于0则组合数据
        if addNum > 0:
            nowDateAdd.append({
                'date': dateTitle[index],
                'add': addNum
            })
        # 取得本期减少
        reduceNum = row[index + 1].value
        if reduceNum == '-' or not reduceNum:
            reduceNum = 0
        if reduceNum > 0:
            nowDateReduceNum.append({
                'date': dateTitle[index],
                'reduce': reduceNum
            })
    # 计算回款
    newSheet += getHuikuan(nowDateAdd, nowDateReduceNum, name)

newXlsx = Workbook()
newXlsxS1 = newXlsx.active
newXlsxS1.title = '回款率统计表'

# 写表头
newXlsxS1['A1'] = '客户名称'
newXlsxS1['B1'] = '时间'
newXlsxS1['C1'] = '新增'

for index, item in enumerate(huikuanTitle):
    newXlsxS1.cell(row=1, column=index+4, value=item)

# 写数据
for index, row in enumerate(newSheet):
    # print(row)
    for j, column in enumerate(row):
        newXlsxS1.cell(row=index+2, column=j+1, value=row[column])

newXlsx.save(filename='回款率统计表.xlsx')


# 函数：获取之前的本期减少