import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('新的    位置    内容')
print('----    ----   ----------')

l = []
# 遍历元数据
for i in values:
  # 取得可以插入的位置
  pos = bisect.bisect_left(l, i)
  # 插入数据到 l 序列中
  bisect.insort_left(l, i)
  print('{:4}    {:4}  '.format(i, pos), l)