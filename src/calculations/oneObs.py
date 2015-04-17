__author__ = 'Lunding'


import stattable as st
import math

digits = 3

def S(observations):
    output = 0.0
    for x in range(len(observations)):
        output += observations[x]
    return output

def USS(observations):
    output = 0.0
    for x in range(len(observations)):
        output += math.pow(observations[x], 2)
    return output

def SSD(n, S, USS, printResult=False):
    result = (USS - (math.pow(S, 2) / n))
    if printResult:
        print("SSD: " + str(result))
    return result

def estimateMean(n, S, printResult=False):
    result = (1.0 / n) * S
    if printResult:
        print("Estimated mean: " + str(result))
    return result

def estimateVariance(n, S, USS, printResult=False):
    result = (1.0 / (n - 1.0)) * SSD(n, S, USS)
    if printResult:
        print("Estimated variance: " + str(result))
    return result

def estimateStdDev(n, S, USS, printResult=False):
    result = math.sqrt(estimateVariance(n, S, USS))
    if printResult:
        print("Estimated standard deviation: " + str(result))
    return result

###### Confidentintervals ######
def confidenceMeanKnownVariance(n, S, sigma, trace=False, printResult=True, alpha=0.05):
    mean = estimateMean(n, S)
    u = st.u(1 - alpha/2)
    resultleft = mean - (math.sqrt(sigma/n) * u)
    resultright = mean + (math.sqrt(sigma/n) * u)
    if trace:
        print("n = " + str(n) + ", u = " + str(round(u, digits)) + ", mean = " + str(round(mean, digits)) + ", sigma = " + str(round(sigma, digits)))
    if printResult:
        print("(1-alpha) confidence interval: [" + str(resultleft) + "; " + str(resultright) + "], for mean (known variance)")
    return resultleft, resultright

def confidenceMeanEstimatedVariance(n, S, USS, trace=False, printResult=True, alpha=0.05):
    mean = estimateMean(n, S)
    variance = estimateVariance(n, S, USS)
    f = n-1
    t = st.t(1-alpha/2, f)
    resultleft = mean - (math.sqrt(variance/n) * t)
    resultright = mean + (math.sqrt(variance/n) * t)
    if trace:
        print("n = " + str(n) + ", f = " + str(f) + ", t = " + str(round(t, digits)) + ", mean = " + str(round(mean, digits)) + ", variance = " + str(round(variance, digits)))
    if printResult:
        print("(1-alpha) confidence interval: [" + str(resultleft) + "; " + str(resultright) + "], for mean (unknown variance)")
    return resultleft, resultright

def confidenceVariance(n, S, USS, trace=False, printResult=True, alpha=0.05):
    variance = estimateVariance(n, S, USS)
    f = n-1
    chi2left = st.chi2(1-(alpha/2), f)
    chi2right = st.chi2((alpha/2), f)
    resultleft = (f * variance) / chi2left
    resultright = (f * variance) / chi2right
    if trace:
        print("f = " + str(f) + ", variance = " + str(round(variance, digits)) + ", ChiLeft = " + str(round(chi2left, digits)) + ", ChiRight = " + str(round(chi2right, digits)))
    if printResult:
        print("(1-alpha) confidence interval: [" + str(resultleft) + "; " + str(resultright) + "], for variance")
    return resultleft, resultright

def confidenceStdDev(n, S, USS, trace=False, printResult=True, alpha=0.05):
    resultleft, resultright = confidenceVariance(n, S, USS, trace, trace, alpha)
    resultleft = math.sqrt(resultleft)
    resultright = math.sqrt(resultright)

    if printResult:
        print("(1-alpha) confidence interval: [" + str(resultleft) + "; " + str(resultright) + "], for Std dev")
    return resultleft, resultright


###### Tests ######
def uTest(n, S, variance, mu0, trace=False, printResult=True):
    mean = estimateMean(n, S)
    uresult = (mean - mu0) / (math.sqrt((variance/n)))
    phiresult = st.Phi(math.fabs(uresult))
    pobs = 2 * (1 - phiresult)
    if trace:
        print("n = " + str(n) + ", mu0 = " + str(round(mu0, digits)) + ", mean= " + str(round(mean, digits)) + ", variance = " + str(round(variance, digits)) + ", u(x) = " + str(round(uresult, digits)) + ", PhiResult = " + str(round(phiresult, digits)))
    if printResult:
        print("pobs = " + str(round(pobs, digits)) + " for mean = " + str(mu0))
    return pobs

def tTest(n, S, USS, mu0, trace=False, printResult=True):
    f = n - 1
    mean = estimateMean(n, S)
    variance = estimateVariance(n, S, USS)
    tresult = (mean - mu0) / (math.sqrt((variance/ n)))
    Ftresult = st.Ft(math.fabs(tresult), f)
    pobs = 2 * (1 - Ftresult)
    if trace:
        print("n = " + str(n) + ", mu0 = " + str(round(mu0, digits)) + ", mean= " + str(round(mean, digits)) + ", variance = " + str(round(variance, digits)) + ", t(x) = " + str(round(tresult, digits)) + ", FtResult = " + str(round(Ftresult, digits)))
    if printResult:
        print("pobs = " + str(round(pobs, digits)) + " for mean = " + str(mu0))
    return pobs

def varianceTest(n, S, USS, sigma0, trace=False, printResult=True):
    f = n - 1
    variance = estimateVariance(n, S, USS)
    chiresult = (f * variance) / sigma0
    if chiresult < f:
        pobs = 2 * st.Fchi2(chiresult, f)
    else:
        pobs = 2 * (1 - st.Fchi2(chiresult, f))
    if trace:
        print("n = " + str(n) + ", f = " + str(f) + ", variance = " + str(round(variance, digits)) + ", chiresult = " + str(round(chiresult, digits)))
    if printResult:
        print("pobs = " + str(round(pobs, digits)) + " for variance = " + str(sigma0))
    return pobs
