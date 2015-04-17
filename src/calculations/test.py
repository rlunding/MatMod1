__author__ = 'Lunding'

import oneObs as oo
import nObs as no
import fractileDiagram as fd
import stattable as st
import math
n = 23
S = 231.47
USS = 2329.9201

# print("Opgave 1")
# mean = oo.estimateMean(n, S, True)
# variance = oo.estimateVariance(n, S, USS, True)
# stdDev = oo.estimateStdDev(n, S, USS, True)
# low, high = oo.confidenceMeanKnownVariance(n, S, variance, True)
# low, high = oo.confidenceMeanEstimatedVariance(n, S, USS, True)
# left, right = oo.confidenceVariance(n, S, USS, True)
# left, right = oo.confidenceStdDev(n, S, USS)


# oo.uTest(n, S, variance, 25, True)
# oo.tTest(n, S, USS, 25, True)
# oo.varianceTest(n, S, USS, 8.4, True)

# print("\n\n")
print("Beregningsskema")
values = ((41, 162.593, 657.028740), (41, 175.014, 763.754248))
no.calculationSchema(values)
print("F-test, for ens varians")
no.F2test2(40, 40, 0.4171, 0.3059)
print("Konfidens interval forskellen af middelvaerdierne")
no.confidenceMeanEqualVariance(41, 41, 3.9657, 4.2686, 0.3615)
print("Ens middelvaerdi")
no.commonMeanTestSameVariance(41, 41, 3.9657, 4.2686, 0.3615)

print("\n\n")
no.F2test2(31, 31, 6.500467, 7.827502)
print((31 * 6.500467+ 31* 7.827502)/(31+31))
print("\n\n")
print(((448.160431-444.167058)/(63-62))/7.163985)
print(1-st.Ff((((448.160431-444.167058)/(63-62))/7.163985), 1, 62))
print("\n\n")
print(((452.342458-448.1604)/(64-63))/7.113658)
print(1-st.Ff((((452.342458-448.1604)/(64-63))/7.113658), 1, 63))
print("\n\n")
x = (1.04323 - 1) / math.sqrt(7.067851/3972.930270)
pobs = 2 * (1 - st.Ft(math.fabs(x),63))
print(x)
print(pobs)

print((1+1)/math.sqrt(2))
print(2 * (1 - st.Phi((1+1)/math.sqrt(2))))
# observations = [2.2, 3.6, 3.8, 4.4, 4.9, 5.9, 6.9, 7.5, 7.5, 7.7, 8.9, 9.7]
# fd.calculateSchema(observations)
# observations = [2.2]
# fd.calculateSchema(observations, 12)

# no.Ftest(3.0, 23.0, 231.47, 2329.5027, 0.02087)