import queue

# 先进先出队列
q = queue.Queue()
for i in range(5):
  q.put(i)

print('\n---------------- 先进先出队列')
while not q.empty():
  print(q.get())

# 后进先出队列
q2 = queue.LifoQueue()
for i in range(5):
  q2.put(i)

print('\n------------------ 后进先出队列')
while not q2.empty():
  print(q2.get())

# 优先队列
class Test:

  def __init__ (self, value):
    self.val = value
    return
  # 先进先出，如果等于 2 则优先出列
  def __lt__ (self, other):
    if self.val == 2:
      return True
    return self.val < other.val

q3 = queue.PriorityQueue()
for i in range(5):
  q3.put(Test(i))

print('----------------- 优先队列，2优先')
while not q3.empty():
  print(q3.get().val)
