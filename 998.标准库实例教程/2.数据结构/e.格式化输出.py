# 格式化输出数据结构，用于美化打印
from pprint import pformat, pprint
import logging

logging.basicConfig(
  level=logging.DEBUG,
  format='%(levelname)-8s %(message)s'
)

data = [
  (1, {'a', 'b', 'c', 'd'}),
  (2, {'a', 'b', 'c', 'd'}),
  (3, {'a', 'b', 'c', 'd'}),
  (4, {'a', 'b', 'c', 'd'}),
  (5, {'a', 'b', 'c', 'd'})
]

pprint(data)

logging.debug('打印数据')

s = pformat(data)

for line in s.splitlines():
    logging.debug(line.rstrip())