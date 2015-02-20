__author__ = 'Lunding'

import utilities
import onesample
import bartlett

alpha = 0.05
n = 12
S = 73.0
USS = 503.12

k = 7
fi = (2, 2, 2, 2, 2, 2, 2)
si = (111.0, 21.0, 49.0, 56.333333, 64.333333, 84, 49.333333)

utilities.createLatexPDF("Afl",utilities.createdocument(
    utilities.createsection("Opgave 1",
        utilities.createexercise("Estimer middelvaeriden og variansen.",
                                 onesample.estimatemean(True, n, S, USS) +
                                 onesample.estimatevarince(True, n, S, USS)) +
        utilities.createexercise("Find et 95 procent konfidens interval for middelvaerdien, spedningen og variansen",
                                   onesample.confidencevariance(True, alpha, n, S, USS) +
                                   onesample.confidencesd(True, alpha, n, S, USS) +
                                    onesample.confidencemean(True, alpha, n, S, USS))) +
    utilities.createsection("Opgave 2", utilities.createexercise("Goer dit", bartlett.bartlettPDF(True, k, fi, si)))
))
