import math


def add3D(a, b):
    x = a[0] + b[0]
    y = a[1] + b[1]
    z = a[2] + b[2]
    return [x, y, z]


def sub3D(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]
    return [x, y, z]


def length3D(a):           #длина вектора 3D
    return math.sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)


def normal3D(a):  # нормализация вектора
    L = length3D(a)
    x = a[0] / L
    y = a[1] / L
    z = a[2] / L
    return [x, y, z]


def dot3D(a, b):           #скалярное прроизведение векторов
    scal = a[0] * b[0] + a[1] * b[1] + b[2] * [2]
    return scal


def cos3D(a, b):          #косинус угла между двумя трехмерными векторами
    up = dot3D(a, b)
    down = length3D(a) * length3D(b)
    return up / down


def multiplievtosc3D(a, mn):
    x = a[0] * mn
    y = a[1] * mn
    z = a[2] * mn
    return [x, y, z]