__author__ = 'Lunding'

import math
import stattableOLD as st
import utilities

template_path = r"templates_tests/"

def bartlettPDF(formula, k, fi, si):
    result = ""
    if (formula):
        result = utilities.loadformula("bartlett_test", "tests")
    p = pobs(k, fi, si)
    if p > 0.05:
        hypresult = " > 0.05$ forkaster vi ikke hypotesen "
    else:
        hypresult = " < 0.05$ forkaster vi hypotesen "

    with open (template_path + "template_bartlett_test.txt", "r") as template_file:
        result += template_file.read() % {
            'k': int(round(k,0)),
            'fi': listtostr(fi),
            'si': listtostr(si),
            'n': int(round((sumf1(fi)+k),0)),
            'fone': int(round(sumf1(fi),0)),
            'SSDone': round(SSD(fi, si), 4),
            'sonesq': round(s1sq(fi, si), 4),
            'sumi': round(SUMI(fi, si), 4),
            'lnqx': round(lnQ(fi, si), 4),
            'fis': round(FIS(fi), 4),
            'C': round(C(k, fi), 4),
            'Ba': round(Ba(k, fi, si), 4),
            'pobs': round(pobs(k, fi, si), 4),
            'hypresult': hypresult,
        }
    return result

def pobs(k, fi, si):
    return 1 - st.Fchi2(Ba(k, fi, si), (k-1))

def Ba(k, fi, si):
    return lnQ(fi, si)/C(k, fi)

def lnQ(fi, si):
    return sumf1(fi) * math.log(s1sq(fi, si)) - SUMI(fi, si)

def SUMI(fi, si):
    sumi = 0.0
    for i in range(len(fi)):
        sumi += fi[i] * math.log(si[i])
    return sumi

def C(k, fi):

    return 1 + (1 / (3.0 * (k - 1.0))) * (FIS(fi) - (1 / sumf1(fi)))

def FIS(fi):
    fis = 0.0
    for x in range(len(fi)):
        fis += 1 / (fi[x] * 1.0)
    return fis

def SSD(fi, si):
    ssd = 0.0
    for i in range(len(fi)):
        ssd += fi[i] * si[i]
    return ssd
def s1sq(fi, si):
    return SSD(fi, si) / sumf1(fi)

def sumf1(fi):
    sumf = 0.0
    for i in range(len(fi)):
        sumf += fi[i] * 1.0
    return sumf


def listtostr(inputlist):
    output = ""
    for x in range(len(inputlist)):
        output += str(int(round(inputlist[x], 0))) + ", "
    output = output[:-2]
    return output

# k = 7
# fi = (2, 2, 2, 2, 2, 2, 2)
# si = (111.0, 21.0, 49.0, 56.333333, 64.333333, 84, 49.333333)
# print("-2 ln Q(x) = " + str(lnQ(fi, si)) + " sumi = " + str(SUMI(fi, si)))
# print("C = " + str(C(k, fi)) + " fis = " + str(FIS(fi)))
# print("Ba = " + str(Ba(k, fi, si)))
# print("S1 SQ = " + str(s1sq(fi, si)))
# print("f1 = " + str(sumf1(fi)))
# print("SSD1 = " + str(SSD(fi, si)))
# print("p obs(x) = " + str(pobs(k, fi, si)))