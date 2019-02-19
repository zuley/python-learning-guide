import string

# capwords 函数将所有单词的首字母大写。
s = 'The quick brown fox jumped over the lazy dog.'
print(string.capwords(s))

# 字符串模板
values = { 'var': '猪不乐意' }
t = string.Template("你好啊，${var}！")
print(t.substitute(values))