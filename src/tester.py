__author__ = 'Lunding'

import utilities
import onesample


utilities.createLatexPDF("Afl",utilities.createdocument(utilities
    .createsection("Opgave 1",
        utilities.createexercise("Estimer middelvaeriden og variansen.", onesample.estimatemean(True, 12, 73.0, 503.12) + onesample.estimatevarince(True, 12, 73.0, 503.12))
        + utilities.createexercise("Find et 95 procent konfidens interval for middelvaerdien og variansen",
                                   onesample.confidencevariance(True, 0.05, 12, 73.0, 503.12) +
                                    onesample.confidencemean(True, 0.05, 12, 73.0, 503.12)))
                         ))
