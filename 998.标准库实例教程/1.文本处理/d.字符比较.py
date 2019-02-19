import difflib

text1 = """你是猪吗，
我是猪。
你不是。
"""
text1_lines = text1.splitlines()

text2 = """你是猪吗，
我不是猪。
你是。
"""
text2_lines = text2.splitlines()

d = difflib.Differ()

diff = d.compare(text1_lines, text2_lines)

print('\n'.join(diff))