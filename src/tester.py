__author__ = 'Lunding'

import utilities
import onesample
import bartlett
import linearregression as lr

alpha = 0.05
n = 12
S = 73.0
USS = 503.12

opgave1 = onesample.estimatemean(True, n, S, USS) + onesample.estimatevarince(True, n, S, USS)
opgave2 =   onesample.confidencevariance(True, alpha, n, S, USS) \
            + onesample.confidencesd(True, alpha, n, S, USS) \
            + onesample.confidencemean(True, alpha, n, S, USS)
k = 7
fi = (2, 2, 2, 2, 2, 2, 2)
si = (111.0, 21.0, 49.0, 56.333333, 64.333333, 84, 49.333333)

opgave3 = utilities.createexercise("Goer dit", bartlett.bartlettPDF(True, k, fi, si))

n = 21
Sx = 6068
St = 525
USSx = 1773300
USSt = 13353
SP = 153773

opgave4 = utilities.createexercise("Goer dat", lr.templatePDF(True, n, Sx, St, USSx, USSt, SP))

utilities.createLatexPDF("Afl",utilities.createdocument(
    utilities.createsection("Opgave 1",
        utilities.createexercise("Estimer middelvaeriden og variansen.", opgave1) +
        utilities.createexercise("Find et 95 procent konfidens interval for middelvaerdien, spedningen og variansen", opgave2)) +
    utilities.createsection("Opgave 2",
                            opgave3 + opgave4)
))
