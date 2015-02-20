# -*- coding: utf-8 -*-
__author__ = 'Lunding'

def calculatetemplate(n, Sx, St, USSx, USSt, SP):
    n = n * 1.0 #n have to be treated as an decimal number
    SSDx = USSx - ((Sx * Sx) / n)
    SSDt = USSt - ((St * St) / n)
    SPD = SP - ((Sx * St)/n)
    beta = SPD/SSDt
    alpha = (1/n) * (Sx - beta * St)
    SSD02 = SSDx - ((SPD * SPD) / SSDt)
    s02sq = (1/(n-2)) * SSD02

    print(SSDx)
    print(SSDt)
    print(SPD)
    print(beta)
    print(alpha)
    print(SSD02)
    print(s02sq)

calculatetemplate(21, 6068, 525, 1773300, 13353, 153773)