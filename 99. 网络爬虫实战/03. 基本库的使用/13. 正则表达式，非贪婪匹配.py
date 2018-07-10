import re

content = 'Hello 1234567 World_This is a Regex Demo'

# 非贪婪匹配是尽可能少的匹配
# .* 加一个问号即 非贪婪匹配 .*?
result = re.match('^He.*?(\d+).*?Demo$', content)

print(result.group(1))