# -*- coding: utf-8 -*-
__author__ = 'Lunding'

import utilities
import onesample
import twosamples as ts
import bartlett
import linearregression as lr

alpha = 0.05
n = 12
S = 73.0
USS = 503.12

opgave11 = onesample.estimatemeanPDF(True, n, S, USS) + onesample.estimatevarincePDF(True, n, S, USS)
opgave12 =   onesample.confidencevariancePDF(True, alpha, n, S, USS) \
            + onesample.confidencesdPDF(True, alpha, n, S, USS) \
            + onesample.confidencemeanPDF(True, alpha, n, S, USS)

opgave13 = utilities.createexercise("Undersøg om middelværdien af vægttabet er 6.5 kg", onesample.ttestPDF(True, n, S, USS, 6.5))
opgave14 = utilities.createexercise("Undersøg om middelværdien af vægttabet er 6.5 kg", onesample.utestPDF(True, n, S, 6.5, 5))

k = 7
fi = (2, 2, 2, 2, 2, 2, 2)
si = (111.0, 21.0, 49.0, 56.333333, 64.333333, 84, 49.333333)

opgave21 = utilities.createexercise("Goer dit", bartlett.bartlettPDF(True, k, fi, si))

n = 21
Sx = 6068
St = 525
USSx = 1773300
USSt = 13353
SP = 153773

opgave22 = utilities.createexercise("Goer dat", lr.templatePDF(True, n, Sx, St, USSx, USSt, SP))

SSD1 = 870
s1sq = 62.14286
SSD02 = lr.SSD02(n, Sx, St, USSx, USSt, SP)
fone =  lr.fone(fi)


opgave23 = utilities.createexercise("Se om den er en lineær reg.", lr.FtestPDF(True, n, k, SSD02, fone, SSD1, s1sq))


n1 = 10
n2 = 7
S1 = 71.7
S2 = 44.7
USS1 = 515.83
USS2 = 286.25
f1 = n1 - 1
f2 = n2 - 1
s1sq = ts.estimateVariance(n1, S1, USS1)
s2sq = ts.estimateVariance(n2, S2, USS2)
x1 = ts.estimateMean(n1, S1)
x2 = ts.estimateMean(n2, S2)

opgave31 = utilities.createexercise("Estimer middelværdi og varians", ts.estimateMean(n1, S1) + ts.estimateVariance(n1, S1, USS1))
opgave32 = utilities.createexercise("Undersøg om variansen er ens", ts.equalvariancePDF(f1, f2, s1sq, s2sq));
opgave33 = utilities.createexercise("Undersøg om middelværdi er ens, varians forskellig", ts.equalmeandifferentvariancePDF(f1, f2, x1, x2, s1sq, s2sq))


somm14 = utilities.createexercise("Ens varians", bartlett.bartlettPDF(True, 3, (7, 7, 6), ()))

utilities.createLatexPDF("Afl",utilities.createdocument(
    utilities.createsection("Opgave 1",
        utilities.createexercise("Estimer middelvaeriden og variansen.", opgave11) +
        utilities.createexercise("Find et 95 procent konfidens interval for middelvaerdien, spedningen og variansen", opgave12) +
        opgave13 + opgave14) +
    utilities.createsection("Opgave 2",
                            opgave21 + opgave22 + opgave23) +
    utilities.createsection("Opgave 3 - 2 Rækker",
                            opgave31 + opgave32 + opgave33)
))

