from itertools import *

# 合并迭代器
print('-------------------------合并迭代器函数 chain')
for i in chain([1, 2, 3], ['a', 'b', 'c']):
  print(i, end='  ')

# 动态合并迭代器（不知道有几个迭代器作为输入）
def make_iterables_to_chain ():
  yield [1, 2, 3]
  yield ['a', 'b', 'c']

print('\n-------------------------动态合并迭代器函数')
for i in chain.from_iterable(make_iterables_to_chain()):
  print(i, end='  ')

# 同时遍历迭代器，返回元素组成的元组。
print('\n-------------------------同时遍历迭代器')
for i in zip([3, 2, 1], ['a', 'b', 'c'], ['x', 'y', 'z']):
  print(i)

# 部分迭代，可设置开始，结束，步长
for i in islice(range(100), 5, 10, 2):
  print(i, end="  ")

# 同时返回多个独立的迭代器
r = islice(count(), 5)
i1, i2 = tee(r)
print('\n-------------------------返回多个迭代器')
print('i1:', list(i1))
print('i2:', list(i2))

# 变换输入
def times_two (x):
  return 2 * x
r = [1, 2, 3]
r2 = map(times_two, r)
print('\n-------------------------变换输入')
print(list(r), list(r2))

# 连续整数迭代器
print('\n-------------------------连续整数迭代器')
for i in zip(count(1), ['a', 'b', 'c']):
  print(i)

# 无限循环迭代器
print('\n-------------------------无限循环迭代器')
for i in zip(range(7), cycle(['a', 'b', 'c'])):
  print(i)

print('\n-------------------------重复输出迭代器')
for i in repeat('猪不乐意', 5):
  print(i)

# 将 0 - 4 的整数乘以二
print('\n-------------------------将 0 - 4 的整数乘以二')
for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
  print('{:d} * {:d} = {:d}'.format(*i))

# 过滤：首次为假之后返回之前的所有元素
print('\n-------------------------首次为假之后所有元素')
for i in dropwhile(lambda x: x < 1, [-1, 0, 1, 2, -2]):
  print(i)

print('\n-------------------------首次为假前的所有元素')
for i in takewhile(lambda x: x < 1, [-1, 0, 1, 2, -2]):
  print(i)

# 内建过滤函数，filter，只包含使测试函数为真的所有元素。
print('\n-------------------------过滤 filter，只包含使测试函数为真的所有元素。')
for i in filter(lambda x: x < 1, [-1, 0, 1, 2, -2]):
  print(i)

# 内建过滤函数，filterfalse，只包含使测试函数为假的所有元素。
print('\n-------------------------过滤 filterfalse，只包含使测试函数为真的所有元素。')
for i in filterfalse(lambda x: x < 1, [-1, 0, 1, 2, -2]):
  print(i)

# 使用序列中的布尔值，决定元素的取舍
print('\n-------------------------使用序列中的布尔值过滤序列')
every_third = cycle([False, False, True])
data = range(1, 10)
for i in compress(data, every_third):
  print(i)

# 数据分组，根据相邻的 key 分组，所以一般结合排序使用。
data = [
  { '姓名': '猪乐意', '性别': '男', '年龄': '29'},
  { '姓名': '猪乐意2', '性别': '男', '年龄': '28'},
  { '姓名': '猪不乐意', '性别': '女', '年龄': '28'},
  { '姓名': '乐意', '性别': '女', '年龄': '29'},
  { '姓名': '乐乐', '性别': '男', '年龄': '29'}
]
for i in groupby(data, lambda d: d['年龄'] ):
  print(list(i[1]))

# 联结输入，可以得到序列的累加和
print('\n-------------------------联结输入')
print(list(accumulate(range(5))))
print(list(accumulate('abcde')))

# 联结输入，使用参数改变策略
def f (a, b):
  return a * b

print(list(accumulate(range(1, 5), f)))

# 取代多个序列嵌套
FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

a = chain(range(2, 11), FACE_CARDS)
DECK = list(product(a, SUITS))

for card in DECK:
  print('{:>2}{}'.format(*card), end="  ")
  if card[1] == SUITS[-1]:
    print()