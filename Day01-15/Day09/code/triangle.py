"""
实例方法和类方法的应用

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._perimeter = None
        self._area = None

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._a + self._b + self._c
        return self._perimeter

    def area(self):
        if self._area is None:
            p = self.perimeter() / 2
            self._area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return self._area


if __name__ == '__main__':
    a, b, c = map(float, input('请输入三条边: ').split())
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print('周长:', tri.perimeter())
        print('面积:', tri.area())
    else:
        print('不能构成三角形.')
