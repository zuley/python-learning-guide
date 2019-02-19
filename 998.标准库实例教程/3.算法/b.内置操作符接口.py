from operator import *

a = -1
b = 5
# 逻辑运算
print('\n逻辑运算\n')
print('not_(a)      :', not_(a))
print('truth(a)     :', truth(a))
print('is_(a, b)    :', is_(a, b))
print('is_not(a, b) :', is_not(a, b))


a = 1
b = 5.0

print('\n比较运算符\n')
print('a = ', a)
print('b = ', b)
for func in (lt, le, eq, ne, ge, gt):
  print('{}(a, b) : {}'.format(func.__name__, func(a, b)))


a = -1
b = 5.0
c = 2
d = 6

print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

print('\n正/负\n')
# 绝对值
print('abs(a):', abs(a))
# 负数
print('neg(a):', neg(a))
print('neg(b):', neg(b))
# 
print('pos(a):', pos(a))
print('pos(b):', pos(b))

print('\n四则运算\n')
# 加法
print('add(a, b)     :', add(a, b))
# 整数除法
print('floordiv(a, b):', floordiv(a, b))
print('floordiv(d, c):', floordiv(d, c))
print('mod(a, b)     :', mod(a, b))
print('mul(a, b)     :', mul(a, b))
print('pow(c, d)     :', pow(c, d))
print('sub(b, a)     :', sub(b, a))
print('truediv(a, b) :', truediv(a, b))
# 浮点数除法
print('truediv(d, c) :', truediv(d, c))

print('\n位运算\n')
# 按位与
print('and_(c, d)  :', and_(c, d))
# 取反
print('invert(c)   :', invert(c))
# 左移位
print('lshift(c, d):', lshift(c, d))
# 按位或
print('or_(c, d)   :', or_(c, d))
# 右移位
print('rshift(d, c):', rshift(d, c))
# 异或
print('xor(c, d)   :', xor(c, d))