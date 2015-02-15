__author__ = 'Lunding'

import utilities
import stattable as st
import math

template_path = r"templates_1_sample/"

def estimatemean(formula, n, S, USS):
    result = ""
    if (formula):
        result = utilities.loadformula("mean_estimate", "1")
    muresult = (1.0/n) * S
    sigmaresult = (1.0/(n-1.0)) * (USS - ((S*S)/n))
    with open (template_path + "template_mean_estimate.txt", "r") as template_file:
        result += template_file.read() % {
            'n': n,
            'S': S,
            'USS': USS,
            'muresult': round(muresult, 3),
            'sigmaresult': round(sigmaresult, 3)
        }
    return result

def estimatevarince(formula, n, S, USS):
    result = ""
    if (formula):
        result = utilities.loadformula("variance_estimate", "1")
    muresult = (1.0/n) * S
    sigmaresult = (1.0/(n-1.0)) * (USS - ((S*S)/n))
    with open (template_path + "template_variance_estimate.txt", "r") as template_file:
        result += template_file.read() % {
            'n': n,
            'S': S,
            'USS': USS,
            'muresult': round(muresult, 3),
            'sigmaresult': round(sigmaresult, 3)
        }
    return result

def equalvariance():
    print("not implemented")

def equalmean():
    print("not implemented")

def confidencemean(formula, alpha, n, S, USS):
    result = ""
    if formula:
        result = utilities.loadformula("confidence_mean", "1")
    muresult = (1.0/n) * S
    sigmaresult = (1.0/(n-1.0)) * (USS - ((S*S)/n))
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


def confidencevariance(formula, alpha, n, S, USS):
    result = ""
    if formula:
        result = utilities.loadformula("confidence_variance", "1")
    sigmaresult = (1.0/(n-1.0)) * (USS - ((S*S)/n))
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

def withininterval():
    print("not implemented")

# Are these needed?
def likelihood():
    print("not implemented")

def maximumlikelihood():
    print("not implemented")

def confidencelikelihood():
    print("not implemented")
