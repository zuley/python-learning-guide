def strInit ():
    str1 = 'hello，world'
    # 计算字符串的长度
    print('字符串的长度：', len(str1))
    # 获得首字母大写的拷贝
    print('获得首字母大写的拷贝：', str1.capitalize())
    # 获得字符串大写后的拷贝
    print('获得字符串大写后的拷贝', str1.upper())
    # 从字符串中查找指定字符的位置
    print('从字符串中查找指定字符的位置', str1.find('or'))
    print('从字符串中查找指定字符的位置', str1.find('shit'))
    # 检查字符串是否以指定的字符串开头
    print('检查字符串是否以指定的字符串开头', str1.startswith('he'))
    # 检查字符串是否以指定的字符串结尾
    print('检查字符串是否以指定的字符串结尾', str1.endswith('rld'))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print('将字符串以指定的宽度居中并在两侧填充指定的字符', str1.center(50, '~'))
    print('将字符串以指定的宽度靠右放置左侧填充指定的字符', str1.rjust(50, '~'))
    # 从字符串中取出指定位置的字符(下标运算)
    print('从字符串中取出指定位置的字符(下标运算)', str1[2])
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print('切片', str1[2:5])
    print('切片', str1[2:])
    print('切片', str1[:5])
    print('切片', str1[2::2])
    print('切片', str1[::2])
    print('切片', str1[::-1])
    print('切片', str1[-3:-1])
    # 检查字符串是否由数字组成
    print('检查', str1.isdigit())
    print('检查', str1.isalpha())
    print('检查', str1.isalnum())
    # 去除收尾空格
    str2 = ' 123456 '
    print('去除首尾空格', str2.strip())


strInit()