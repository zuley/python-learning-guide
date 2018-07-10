import re

content = 'Hello 1234567 World_This is a Regex Demo'

result = re.match('^Hello\s(\d+)\sWorld', content)

print('输出完整匹配结果：', result.group())
print('输出第一个被()包围的匹配结果：', result.group(1))

s = 'Hello 123 456 World_This is a Regex Demo'

b = re.match('^Hello.*Demo$', s)

print(b.group())