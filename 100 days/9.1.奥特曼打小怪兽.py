from abc import ABCMeta, abstractmethod
from random import randint, randrange
from time import sleep

class Fighter(object, metaclass=ABCMeta):

    """战斗者"""

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法
        :param name: 名字
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return  self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻击
        :param other: 被攻击对象
        :return:
        """
        pass

class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        """普攻"""
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """必杀技"""
        if self._mp >= 50:
            self._mp -= 50
            other.hp -= 100
            return True
        else:
            self.attack(other)
            return  False

    def magic_attack(self, others):
        """魔法攻击"""
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(20, 30)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        num = randint(1, 10)
        self._mp += num
        return num

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值：%d\n' % self._hp + \
            '魔法值：%d\n' % self._mp


class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    """判断是否有小怪兽活着"""
    for monster in monsters:
        if monster.alive:
            return True
    return False


def select_alive_one(monsters):
    """选择一个小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('猪乐意', 1000, 120)
    m1 = Monster('小猪宝宝', 500)
    m2 = Monster('小狗宝宝', 200)
    m3 = Monster('精英小猪', 800)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        sleep(3)
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if (skill <= 6):
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <=9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)

        display_info(u, ms)
        fight_round += 1

    print('\n========战斗结束!========\n')
    if u.alive:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == "__main__":
    main()