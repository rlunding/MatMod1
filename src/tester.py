# -*- coding: utf-8 -*-
__author__ = 'Lunding'

import utilities
import onesample
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

opgave13 = utilities.createexercise("Undersøg om middelværdien af vægttabet er 6.5 kg", onesample.ttest(True, n, S, USS, 6.5))
opgave14 = utilities.createexercise("Undersøg om middelværdien af vægttabet er 6.5 kg", onesample.utest(True, n, S, 6.5, 5))

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

utilities.createLatexPDF("Afl",utilities.createdocument(
    utilities.createsection("Opgave 1",
        utilities.createexercise("Estimer middelvaeriden og variansen.", opgave11) +
        utilities.createexercise("Find et 95 procent konfidens interval for middelvaerdien, spedningen og variansen", opgave12) +
        opgave13 + opgave14) +
    utilities.createsection("Opgave 2",
                            opgave21 + opgave22)
))
