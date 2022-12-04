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
            matr[i][j] = matr1[i][j] * matr2[i][j]
    return matr


def add_matr_matr(matr1, matr2):
    for i in range(len(matr1)):
        for j in range(len(matr1[i])):
            matr[i][j] = matr1[i][j] + matr2[i][j]
    return matr


def subtr_matr_matr(matr1, matr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            matr[i][j] = matr1[i][j] - matr2[i][j]
    return matr