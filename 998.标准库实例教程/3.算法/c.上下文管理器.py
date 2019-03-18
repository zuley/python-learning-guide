class Content:
  def __init__(self):
    print('初始化实例')
  
  def __enter__(self):
    print('进入实例')
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    print('退出实例')

with Content():
  print('这是一个上下文实例')