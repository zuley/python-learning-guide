# Enum 可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
from enum import Enum, unique

@unique
class Gender(Enum):
  Male = 0
  Female = 1

class Student(object):
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
  print('测试通过!')
else:
  print('测试失败!')