__author__ = 'Lunding'

import stattable as st
import math

def Fntestn(k, n, S, row5, s1sq, printResult=True):
    SSD2 = row5 - ((S * S) / n)
    s2sq = SSD2 / (k - 1)
    F = s2sq / s1sq
    pobs = 1 - st.Ff(F, k-1, n-k)
    if printResult:
        print("SSD2 = " + str(SSD2))
        print("s2sq = " + str(s2sq))
        print("F = " + str(F))
        print("pobs = " + str(pobs))
    return pobs

def F2test2(f1, f2, s1sq, s2sq, printResult=True):
    if s1sq > s2sq:
        fmax = f1
        fmin = f2
        smax = s1sq
        smin = s2sq
    else:
        fmax = f2
        fmin = f1
        smax = s2sq
        smin = s1sq
    Fresult = smax / smin
    pobs = 2 * (1 - st.Ff(Fresult, fmax, fmin))
    if printResult:
        print("F = " + str(Fresult))
        print("pobs(x) = " + str(pobs))
    return pobs

def commonMeanTestSameVariance(n1, n2, x1, x2, s1sq, printResult=True):
    f1 = n1 + n2 - 2.0
    Tresult = (x1 - x2) / (math.sqrt(s1sq * ((1.0/n1) + (1.0/n2))))
    tabelresult = st.Ft(math.fabs(Tresult), f1)
    pobs = 2.0 * (1.0 - tabelresult)
    if printResult:
        print("t(x) = " + str(Tresult))
        print("Ft(f) (t(x)) = " + str(tabelresult))
        print("pobs(x) = " + str(pobs))
    return pobs

def commonMeanTestDifferentVariance(n1, n2, x1, x2, s1sq, s2sq, printResult=True):
    f1 = n1 - 1
    f2 = n2 - 1
    Tresult = (x1 - x2) / (math.sqrt((s1sq / (f1)) + (s2sq / (f2))))
    fbarresult = fbar(n1, n2, s1sq, s2sq)
    tabelresult = st.Ft(math.fabs(Tresult), fbar)
    pobs = 2 * (1 - tabelresult)
    if printResult:
        print("t(x) = " + Tresult)
        print("fbar = " + fbarresult)
        print("Ft(f) (t(x)) = " + tabelresult)
        print("pobs(x) = " + pobs)
    return pobs

def calculationSchema(inputValues, printResult=True):
    outputValues = []
    totalN = 0
    totalS = 0
    totalUSS = 0
    totalRow5 = 0
    totalSSD = 0
    totalF = 0
    for i in range(len(inputValues)):
        if len(inputValues[i]) == 3:
            n = inputValues[i][0]
            S = inputValues[i][1]
            USS = inputValues[i][2]
            row5 = math.pow(S, 2) / n
            SSD = USS - math.pow(S, 2) / n
            f = n - 1.0
            variance = SSD / f
            mean = S / n
            outputValues.append(((i+1), n, S, USS, row5, SSD, f, variance, mean))

            totalN += n
            totalS += S
            totalUSS += USS
            totalRow5 += row5
            totalSSD += SSD
            totalF += f

    s1sq = totalSSD / totalF
    commonMean = totalS / totalN
    outputValues.append((0, totalN, totalS, totalUSS, totalRow5, totalSSD, totalF, s1sq, commonMean))

    if printResult:
        printCalculationSchema(outputValues)

zeroDecimalColumns = (1, 2, 7)

def printCalculationSchema(inputValues):
    for i in range(len(inputValues)):
        strline = ""
        for j in range(len(inputValues[i])):
            if (j + 1) in zeroDecimalColumns:
                strline += format(round(inputValues[i][j], 0), '.0f') + "\t\t"
            else:
                strline += format(round(inputValues[i][j], 4), '.4f') + "\t\t"
        print(strline)

def confidenceMeanEqualVariance(n1, n2, x1, x2, s1sq, printResult=True, alpha=0.05):
    f1 = n1 + n2 - 2.0
    stderr = math.sqrt(s1sq * ((1.0/n1) + (1.0/n2))) * st.t((1-alpha/2), f1)
    lower = x1 - x2 - stderr
    upper = x1 - x2 + stderr
    if printResult:
        print("stderr = " +str(stderr))
        print("[" + str(lower) + "; " + str(upper) + "]")
    return lower, upper

def confidenceMeanDifferentVariance(n1, n2, x1, x2, s1sq, s2sq, printResult=True, alpha=0.05):
    f1 = fbar(n1, n2, s1sq, s2sq)
    stderr = math.sqrt(((s1sq/n1) + (s2sq/n2))) * st.t((1-alpha/2), f1)
    lower = x1 - x2 - stderr
    upper = x1 - x2 + stderr
    if printResult:
        print("[" + lower + "; " + upper)
    return lower, upper



def fbar(n1, n2, s1sq, s2sq):
    f1 = n1 - 1
    f2 = n2 - 1
    return (math.pow(((s1sq / (n1)) + (s2sq / (n1))), 2)) / (( (math.pow((s1sq/(n1)), 2))/(f1) ) + ( (math.pow((s2sq / (n1)) , 2))/(f2) ))