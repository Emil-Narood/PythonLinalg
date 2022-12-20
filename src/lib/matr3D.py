#https://pastebin.com/8bBywF96




def mult_matr_sc(matr, sc):
    i = 0
    j = 0
    for i in range (len(matr)):
        for j in range(len(matr[i])):
            matr[i][j] = matr[i][j] * sc
    return matr


def mult_matr_matr(matr1, matr2):
    i = 0
    j = 0
    for i in range (len(matr1)):
        for j in range(len(matr1[i])):
            matr1[i][j] = matr1[i][j] * matr2[i][j]
    return matr1


def add_matr_matr(matr1, matr2):
    for i in range(len(matr1)):
        for j in range(len(matr1[i])):
            matr1[i][j] = matr1[i][j] + matr2[i][j]
    return matr1


def subtr_matr_matr(matr1, matr2):
    for i in range(len(matr1)):
        for j in range(len(matr1[i])):
            matr1[i][j] = matr1[i][j] - matr2[i][j]
    return matr1

def matr3DDet(matr):
    Det = matr[0][0] * matr[1][1] * matr[2][2] + \
    matr[0][1] * matr[1][2] * matr[2][0] + \
    matr[1][0] * matr[0][2] * matr[2][1] - \
    matr[2][0] * matr[1][1] * matr[0][2] - \
    matr[1][0] * matr[0][1] * matr[2][2] - \
    matr[2][1] * matr[0][0] * matr[1][2]
    return Det


def matr3Dtransp(matr):
    a21 = matr[1][0]
    a31 = matr[2][0]
    a32 = matr[2][1]
    matr[1][0] = matr[1][2]
    matr[2][0] = matr[0][2]
    matr[2][1] = matr[0][1]
    matr[1][2] = a21
    matr[0][2] = a31
    matr[0][1] = a32
    return matr