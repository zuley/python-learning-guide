print('\n------------------ 字符串格式化 ------------------')

print('字符串格式化通过 % 实现')
print('格式化字符串：%s' % '我是字符串')
print('格式化整数：%d' % 3)
print('格式化浮点数 %f' % 3.1234)
print('格式化两位浮点数 %.2f' % 3.1234)
print('字段宽度：%10s' % 'abc')
print('字段精度：%.2f' % 3.1234)
print('字段宽度和精度 %10.2f' % 3.1234)
print('简单转换元组：%s' % ('呵呵'))
print('0符号填充： %010.2f' % 12)
print('-符号对齐： %-10.2f' % 12)
print('空白符号对齐整数：% d' % 12)
print('空白符号对齐整数：% d' % -12)
print('+符号强制显示正负数：%+d' % 12)
print('+符号强制显示正负数：%+d' % -12)

print('\n------------------ 字符串方法 ------------------')

a = 'hello world'
print('a 字符串：', a)
print('find 简单查找：a.find("o") >>>', a.find("o"))
print('find 提供起点：a.find("o", 5) >>>', a.find('o', 5))
print('find 提供起点和终点：a.find("o", 5, len(a)) >>>', a.find('o', 5, len(a)))

print('join 将序列连接为字符串："+".join(["1", "2", "3"].) >>>', '+'.join(['1', '2', '3']))
print('注意：join 方法只能连接字符串。')
print('注意：join 方法符号在前，序列在后')

print('lower 大写转换为小写："DO IT NOW".lower() >>>', 'DO IT NOW'.lower())

print('upper 小写转换为大写："do it now".upper() >>>', 'do it now'.upper())

print('swapcase 大小写转换："do IT now".swapcase() >>>', 'do IT now'.swapcase())

print('\nreplace 字符串替换')
s = 'hello world'
print('s 字符串：', s)
print('简单替换：s.replace("o", "z") >>>', s.replace('o', 'z'))
print('替换次数不超过1次：s.replace("o", "z", 1) >>>', s.replace('o', 'z', 1))

print('\nsplit 字符串分割："hello world".split(" ") >>>', 'hello world'.split(' '))

print('strip 移除头尾指定字符串："--abc---".strip("-") >>>', '---abc---'.strip('-'))

a = 'abc'
b = '246'
# 创建翻译表
c = str.maketrans(a, b)
print('translate 使用翻译表替换："a+b+c".translate(c) >>>', 'a+b+c'.translate(c))

print('注意格式化的时候百分号需要两个才能输出：%d%%' % 123)