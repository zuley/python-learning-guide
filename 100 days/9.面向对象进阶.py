class Person(object):

    __slots__ = ('_name', '_age', 'x')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 装饰器 get
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.age

    # 装饰器 set
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

    # 静态方法
    @staticmethod
    def xxx():
        print('我只是静态方法')

def main():
    person = Person('朱', 15)
    person.play()
    # person.age = 22
    person.play()
    print(person.name)
    # person.name = '猪不乐意'
    person.x = 'xx'
    Person.xxx()

if __name__ == '__main__':
    main()