__author__ = 'Lunding'

import math
import stattable as st

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

def makeTest(k, fi, si, printResult=True):
    print("f1 = " + str(sumf1(fi)))
    print("SSD1 = " + str(SSD(fi, si)))
    print("s1^2 = " + str(s1sq(fi, si)))
    print("-2 ln Q(x) = " + str(lnQ(fi, si)))
    print("C = " + str(C(k, fi)))
    print("Ba = " + str(Ba(k, fi, si)))
    print("pobs(x) = " + str(pobs(k, fi, si)))

k = 3
fi = (7, 7, 6)
si = (0.01954, 0.02080, 0.02250)
