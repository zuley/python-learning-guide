print('------------------ 创建元组 ------------------')
a = (1, 2, 3)
print('创建一个元组：a = (1, 2, 3) >>>', a)

a = ()
print('创建一个空元组：a = () >>>', a)

a = (1,)
print('创建只有一个元素的元组：a = (1,) >>>', a)

print('\n------------------ 将序列转换为元组 ------------------')

b = [1, 2, 3]
print('b 序列：', b)

c = tuple(b)
print('将序列转换为元组：c = tuple(b) >>>', c)

print('\n------------------ 元组操作 ------------------')

a = (1, 2, 3)
print('a 元组：', a)
print('访问元组：a[1] >>>', a[1])
print('注意：元组中的元组不允许被修改，也不允许被删除。')
print('注意：元组中的不变是指指向不变，指向的 list 不可变，但是 list 中的元素可变。')

print('\n------------------ 元组内置函数 ------------------')

b = (1, 2, 3)
print('b 元组：', b)
print('元组个数：len(b) >>>', len(b))
print('元组最大值：max(b) >>>', max(b))
print('元组最小值：min(b) >>>', min(b))