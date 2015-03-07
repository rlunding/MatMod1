__author__ = 'Lunding'

import math
import utilities
import stattable as st

template_path = r"templates_linear_regression/"

def templatePDF(formula, n, Sx, St, USSx, USSt, SP):
    n = n * 1.0 #n have to be treated as an decimal number
    result = ""
    if (formula):
        result = utilities.loadformula("calculation_schema", "linear_regression")
    with open (template_path + "template_calculation_schema.txt", "r") as template_file:
        result += template_file.read() % {
            'n': int(round(n,0)),
            'Sx': round(Sx, 4),
            'St': round(St, 4),
            'USSx': round(USSx, 4),
            'USSt': round(USSt, 4),
            'SP': round(SP, 4),
            'SSDx': round(SSDx(n, Sx, USSx), 4),
            'SSDt': round(SSDt(n, St, USSt), 4),
            'SPD': round(SPD(n, Sx, St, SP), 4),
            'beta': round(beta(n, Sx, St, USSt, SP), 4),
            'alpha': round(alpha(n, Sx, St, USSt, SP), 4),
            'SSD02': round(SSD02(n, Sx, St, USSx, USSt, SP), 4),
            's02sq': round(s02sq(n, Sx, St, USSx, USSt, SP), 4)
        }
    return result

def SSDx(n, Sx, USSx):
    return USSx - ((Sx * Sx) / n)

def SSDt(n, St, USSt):
    return USSt - ((St * St) / n)

def SPD(n, Sx, St, SP):
    return SP - ((Sx * St)/n)

def beta(n, Sx, St, USSt, SP):
    return SPD(n, Sx, St, SP)/SSDt(n, St, USSt)

def alpha(n, Sx, St, USSt, SP):
    return (1.0/n) * (Sx - beta(n, Sx, St, USSt, SP) * St)

def SSD02(n, Sx, St, USSx, USSt, SP):
    return SSDx(n, Sx, USSx) - (math.pow(SPD(n, Sx, St, SP), 2) / SSDt(n, St, USSt))

def s02sq(n, Sx, St, USSx, USSt, SP):
    return (1.0/(n-2.0)) * SSD02(n, Sx, St, USSx, USSt, SP)

def calculatetemplate(n, Sx, St, USSx, USSt, SP):
    print(SSDx(n, Sx, USSx))
    print(SSDt(n, St, USSt))
    print(SPD(n, Sx, St, SP))
    print(beta(n, Sx, St, USSt, SP))
    print(alpha(n, Sx, St, USSt, SP))
    print(SSD02(n, Sx, St, USSx, USSt, SP))
    print(s02sq(n, Sx, St, USSx, USSt, SP))

def fone(fi):
    result = 0
    for x in range(len(fi)):
        result += fi[x]
    return result

def FtestPDF(formula, n, k, SSDzerotwo, fone, SSDone, s1sq):
    result = ""
    if (formula):
        result = utilities.loadformula("ftest", "linear_regression")
    f02 = n - 2
    dof1 = k-2
    dof2 = n-k
    fx = ((SSDzerotwo - SSDone) / (f02 - fone)) / s1sq
    FF = st.Ff(fx, dof1, dof2)
    pobs = 1 - FF

    if pobs > 0.05:
        hypresult = r"> 0.05$ accepterer vi hypotesen"
    else:
        hypresult = r"> 0.05$ accepterer vi hypotesen"

    with open (template_path + "template_ftest.txt", "r") as template_file:
        result += template_file.read() % {
            'n': int(round(n,0)),
            'k': int(round(k,0)),
            'f02': int(round(f02,0)),
            'f1': int(round(fone, 0)),
            'SSD1': round(SSDone, 4),
            'SSD02': round(SSDzerotwo, 4),
            's1sq': round(s1sq, 4),
            'fx': round(fx, 4),
            'ff': round(FF, 4),
            'dof1': int(round(dof1, 0)),
            'dof2': int(round(dof2, 0)),
            'pobs': round(pobs, 4),
            'hypresult': hypresult
        }
    return result

#calculatetemplate(21.0, 6068.0, 525.0, 1773300.0, 13353.0, 153773.0)