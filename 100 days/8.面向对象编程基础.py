from time import sleep
from math import sqrt

# 时钟类
class Clock(object):

    def __init__(self, h=0, m=0, s=0):
        self._h = h
        self._m = m
        self._s = s

    def run(self):
        self._s += 1
        if self._s == 60:
            self._s = 0
            self._m += 1
            if self._m == 60:
                self._m = 0
                self._h += 1
                if self._h == 24:
                    self._h = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._h, self._m, self._s)

# 位置类
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = x

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    clock = Clock(23, 59, 55)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    # main()
    p1 = Point(3, 4)
    p2 = Point()
    print(p1.distance_to(p2))