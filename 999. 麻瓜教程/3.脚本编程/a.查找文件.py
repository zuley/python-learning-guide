import os
# 设置路径，当前是相对路径
path = './../1.爬虫实战'
# 以序列的方式取得该路径的下的文件列表
files = os.listdir(path)
# 遍历文件并过滤
for f in files:
  # 检测 当前 文件名中同时包含 github 和 器.py 的文件
  if 'github' in f and f.endswith('器.py'):
    print(f)