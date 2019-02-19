import re

key = '猪'
text = '你好啊，猪不乐意'

# 在文本中使用查找模式
match = re.search(key, text)
s = match.start()
e = match.end()

print('查找 "{}"\n在 "{}"\n从 {} 到 {}'.format(
  match.re.pattern,
  match.string,
  s,
  e
))

# 多重匹配
text = 'abababbababbababab'
key = 'ab'
print('\n ----------------------------- 多重匹配，返回字符串 \n')
for match in re.findall(key, text):
  print('查找 "{}"'.format(match))

print('\n ----------------------------- 多重匹配，返回迭代器 \n')
for match in re.finditer(key, text):
  print('查找 "{}"，从 "{}" 到 "{}"'.format(
    match.re.pattern,
    match.start(),
    match.end()
  ))

def test_patterns(text, patterns):
    # 匹配文本中的每一种模式，并输出结果
    for pattern, desc in patterns:
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return

if __name__ == '__main__':
  test_patterns('abbaaabbbbaaaaa',
    [('ab', "'a' followed by 'b'"),]
  )