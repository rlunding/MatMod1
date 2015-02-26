from __future__ import division
__author__ = 'Lunding'

import utilities
import stattable as st
import math

template_path = r"templates_1_sample/"

def estimatemean(n, S):
    return (1.0/n) * S

def estimatemeanPDF(formula, n, S, USS):
    result = ""
    if (formula):
        result = utilities.loadformula("mean_estimate", "1_sample")
    with open (template_path + "template_mean_estimate.txt", "r") as template_file:
        result += template_file.read() % {
            'n': n,
            'S': S,
            'USS': USS,
            'muresult': round(estimatemean(n, S), 3),
            'sigmaresult': round(estimatevarince(n, S, USS), 3)
        }
    return result

def estimatevarince(n, S, USS):
    return (1.0/(n-1.0)) * (USS - ((S*S)/n))

def estimatevarincePDF(formula, n, S, USS):
    result = ""
    if (formula):
        result = utilities.loadformula("variance_estimate", "1_sample")
    with open (template_path + "template_variance_estimate.txt", "r") as template_file:
        result += template_file.read() % {
            'n': n,
            'S': S,
            'USS': USS,
            'muresult': round(estimatemean(n, S), 3),
            'sigmaresult': round(estimatevarince(n, S, USS), 3)
        }
    return result

def utest(formula, n, S, mu0, sigma):
    result = ""
    if (formula):
        result = utilities.loadformula("utest", "1_sample")
    mu = estimatemean(n, S)
    uresult = (mu - mu0) / (math.sqrt((sigma/n)))
    phiresult = st.Phi(math.fabs(uresult))
    pobs = 2 * (1 - phiresult)
    with open (template_path + "template_utest.txt", "r") as template_file:
        result += template_file.read() % {
            'n': n,
            'muresult': round(mu, 3),
            'sigma': round(sigma, 3),
            'muzero': round(mu0, 3),
            'uresult': round(uresult, 3),
            'phiresult': round(phiresult, 3),
            'pobs': round(pobs, 3),
        }
    result += r"Da $p_{obs}(x) = " + str(round(pobs, 3))
    if pobs > 0.05:
        result += r" > 0.05$ forkaster vi \textbf{ikke} hypotesen.\\"
    else:
        result += r" < 0.05$ \textbf{forkaster} vi hypotesen.\\"
    return result

def ttest(formula, n, S, USS, mu0):
    result = ""
    if (formula):
        result = utilities.loadformula("ttest", "1_sample")
    f = n-1
    mu = estimatemean(n, S)
    sigmaresult = estimatevarince(n, S, USS)
    tresult = (mu - mu0) / (math.sqrt((sigmaresult/n)))
    Ftresult = st.Ft(math.fabs(tresult), f)
    pobs = 2 * (1 - Ftresult)
    with open (template_path + "template_ttest.txt", "r") as template_file:
        result += template_file.read() % {
            'n': n,
            'f': f,
            'muresult': round(mu, 3),
            'sigmaresult': round(sigmaresult, 3),
            'muzero': round(mu0, 3),
            'tresult': round(tresult, 3),
            'Ftresult': round(Ftresult, 3),
            'pobs': round(pobs, 3),
        }
    result += r"Da $p_{obs}(x) = " + str(round(pobs, 3))
    if pobs > 0.05:
        result += r" > 0.05$ forkaster vi \textbf{ikke} hypotesen.\\"
    else:
        result += r" < 0.05$ \textbf{forkaster} vi hypotesen.\\"
    return result



def confidencemeanPDF(formula, alpha, n, S, USS):
    result = ""
    if formula:
        result = utilities.loadformula("confidence_mean", "1_sample")
    muresult = estimatemean(n, S)
    sigmaresult = estimatevarince(n, S, USS)
    dof = n-1
    t = st.t(1-alpha/2, dof)
    resulthigh = muresult - (math.sqrt(sigmaresult/n)*t)
    resultlow = muresult + (math.sqrt(sigmaresult/n)*t)
    with open (template_path + "template_confidence_mean.txt", "r") as template_file:
        result += template_file.read() % {
            'alpha': alpha,
            'muresult': round(muresult,3),
            'sigmaresult': round(sigmaresult,3),
            'n': n,
            'dof': dof,
            't': round(t, 3),
            'resulthigh': round(resulthigh, 3),
            'resultlow': round(resultlow, 3)
        }
    return result

def confidencevariancePDF(formula, alpha, n, S, USS):
    result = ""
    if formula:
        result = utilities.loadformula("confidence_variance", "1_sample")
    sigmaresult = estimatevarince(n, S, USS)
    dof = n-1
    chi2high = st.chi2(1-(alpha/2), dof)
    chi2low = st.chi2((alpha/2), dof)
    resulthigh = (dof * sigmaresult) / chi2high
    resultlow = (dof * sigmaresult) / chi2low
    with open (template_path + "template_confidence_variance.txt", "r") as template_file:
        result += template_file.read() % {
            'alpha': alpha,
            'sigmaresult': round(sigmaresult,3),
            'dof': dof,
            'chi2high': round(chi2high, 3),
            'chi2low': round(chi2low, 3),
            'resulthigh': round(resulthigh, 3),
            'resultlow': round(resultlow, 3)
        }
    return result

def confidencesdPDF(formula, alpha, n, S, USS):
    result = ""
    if formula:
        result = utilities.loadformula("confidence_sd", "1_sample")
    sigmaresult = estimatevarince(n, S, USS)
    dof = n-1
    chi2high = st.chi2(1-(alpha/2), dof)
    chi2low = st.chi2((alpha/2), dof)
    resulthigh = math.sqrt((dof * sigmaresult) / chi2high)
    resultlow = math.sqrt((dof * sigmaresult) / chi2low)
    with open (template_path + "template_confidence_sd.txt", "r") as template_file:
        result += template_file.read() % {
            'alpha': alpha,
            'sigmaresult': round(sigmaresult,3),
            'dof': dof,
            'chi2high': round(chi2high, 3),
            'chi2low': round(chi2low, 3),
            'resulthigh': round(resulthigh, 3),
            'resultlow': round(resultlow, 3)
        }

    return result


def withininterval():
    print("not implemented")

# Are these needed?
def likelihood():
    print("not implemented")

def maximumlikelihood():
    print("not implemented")

def confidencelikelihood():
    print("not implemented")
