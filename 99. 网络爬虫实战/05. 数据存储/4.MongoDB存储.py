import pymongo

# 连接数据库服务器
client = pymongo.MongoClient(host='localhost', port=27017)
# 指定数据库
db = client.test
# 指定数据表
collection = db.tests

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = [
    {
        'id': '20170202',
        'name': 'Mike',
        'age': 21,
        'gender': 'male'
    },
    {
        'id': '20170103',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }
]
# 插入一条数据
result = collection.insert_one(student)
print(result)

# 插入多条数据
result = collection.insert_many(student2)
print(result)

# 查询一条记录
result = collection.find_one({ 'name': 'Mike' })
print(result)

# 查询多条记录
result = collection.find({ 'name': 'Mike' })
print(result)

# 更新记录
result = collection.find_one({ 'name': 'Mike' })
result['age'] = 100
result = collection.update({ 'name': 'Mike' }, result)
print(result)

# 删除

result = collection.remove({ 'name': 'Mike' })
print(result)