import math


def add2D(a, b):  # сложение двухмерных векторов
    x = a[0] + b[0]
    y = a[1] + b[1]
    return [x, y]


def sub2D(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return [x, y]


def length2D(a):  # длина вектора 2D
    return math.sqrt(a[0] ** 2 + a[1] ** 2)


def multiplievtov2D(a, b):  # скалярное прроизведение векторов
    return a[0] * b[0] + a[1] * b[1]


def scal_mult_2D(a, mn):
    x = a[0] * mn
    y = a[1] * mn
    return [x, y]


def cos2D(a, b):  # косинус угла между двумя двухмерными векторамb
    up = multiplievtov2D(a, b)
    down = length2D(a) * length2D(b)
    cos_a = up / down
    return cos_a


def normal2D(a):           #нормализация вектора
    L = length2D(a)
    x = a[0] / L
    y = a[1] / L
    return [x, y]