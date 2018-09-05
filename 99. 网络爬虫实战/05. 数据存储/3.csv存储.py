import csv

# 以列表的方式依次写入
with open('test.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

# 以字典的方式，按 key 写入
with open('test.csv', 'a') as file:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # 写入头部字段，如果存在，则不写
    # writer.writeheader()
    writer.writerow({
        'id': 'test',
        'name': '猪不乐意2',
        'age': '233哈哈哈'
    })

# 读取文件
with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)