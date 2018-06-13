list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 索引操作
print('------------------ 索引操作 ------------------')
print('列表：', list)
print('输出索引 list[1]', list[1])
print('反向输出 list[-1]:', list[-1])

# 分片操作
print('------------------ 分片操作 ------------------')
print('取第二和第三个元素 list[1:3]', list[1:3])
print('取倒数第三和倒数第二的元素 list[-3:-1]', list[-3:-1])
print('取倒数三个元素 list[-3:]', list[-3:])
print('取前三个元素 list[:3]', list[:3])
print('取整个数组 list[:]', list[:])
print('隔三取一 list[::3]', list[::3])
print('从序列尾部开始提取第四个到第一个 list[3:0:-1]', list[3:0:-1])

# 序列操作
print('------------------ 序列操作 ------------------')

a = [1, 2, 3]
b = [3, 4, 5]

print('a 序列：', a)
print('b 序列：', b)
print('序列相加 a + b', a+b)

print('序列相乘 "hello" * 5 =', 'hello'*5)
print('序列相乘 [7] * 5 =', [7]*5)

str = 'hello, world'
print('字符串序列 str =', str)
print('检测 w 是否在字符串中 "w" in str =', 'w' in str)
print('str 长度 len(str) =', len(str))
print('a序列最大值 max(a) =', max(a))
print('a序列最小值 min(a) =', min(a))

a[1] = 5
print('元素赋值 a[1] = 5 >>>', a)
a.append(4)
print('增加元素 a.append(4) >>>', a)
del a[0]
print('删除元素 del a[0] >>>', a)
a[0:1] = [2, 2]
print('分片赋值 a[0:1] = [2,2] >>>', a)

print('------------------ 列表方法 ------------------')
c = [1, 2, 3, 4, 5]
print('c 序列：', c)
c.append(5)
print('append 添加元素：c.append(5) >>>', c)
print('count 元素计数：c.count(5) >>>', c.count(5))
c.extend([2,2])
print('extend 扩展列表：c.extend([2,2]) >>>', c)
print('index 查询元素第一次出现的位置 c.index(5) >>>', c.index(5))
c.insert(1, [7,7,7])
print('insert 插入列表 c.insert(1,[7,7,7]) >>>', c)
c.pop(1)
print('pop 移除元素，默认最后一个元素：c.pop(1)', c)