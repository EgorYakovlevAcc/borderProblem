# -*- coding: utf-8 -*-
import numpy as np
import math


def f_x(a, x):
    return math.exp(a*x)


def f_x_t (a, x):
    return a*math.exp(a*x)


def a(k):
    return 0.5 + 0.5 * k




'main body'
'''
hx - шаг сетки вдоль x
ht - шаг сетки вдоль t
n - число узлов
*********
input
*********
u1 - 
u2 - 
u3 - 
*********
output
*********
u1 - 
u2 - 
'''


def calc (hx, ht, n):
    arr_x = np.array([0])
    u1 = np.array([0])
    u2 = np.array([0])
    u3 = np.array([0])

    for i in range(1, n):
        x = (i - 1) * hx
        arr_x = np.append(arr_x, x)
        u1 = np.append(u1, f_x(a,x))
        u2 = np.append(u2, (u1[-1] + ht * f_x_t(a, x)))

    'проверка условия Куранта'
    al = ht/hx
    if al > 1:
        print ('Нарушено условие Куранта')
    else:
        bl = al ** 2
        al = 2 * (1 - bl)

        for i in range (2, n):
            u3 = al * u2[i] + bl * (u2[i + 1] + u2[i - 1]) - ul[m]

        for i in range (2, n):
            u1[i] = u2[i]
            u2[i] = u3[i]

    t = t + t * ht
    return u1, u2


hx = 0.1
ht = 0.05
n = 11
a = 1.5


calc(hx, ht, n)