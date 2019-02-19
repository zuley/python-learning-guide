import textwrap

sample_text = '''
  The textwrap module can be used to format text for output in
  situations where pretty-printing is desired.  It offers
  programmatic functionality similar to the paragraph wrapping
  or filling features found in many text editors.
'''

# 移除已有的缩进
sample_text = textwrap.dedent(sample_text)

print('\n------------------------------------- 移除已有的缩进\n')
print(textwrap.fill(sample_text))
# 每段都添加前缀 >
print('\n------------------------------------- 每段都添加前缀 >\n')
print(textwrap.indent(sample_text, '> '))

def should_indent (line):
  return len(line.strip()) % 2 == 0 and len(line.strip()) != 0
# 偶数行添加前缀
print(textwrap.indent(sample_text, '偶数行: ', predicate=should_indent))

# 摘要输出
print(textwrap.shorten(sample_text, 50, placeholder=' ...'))