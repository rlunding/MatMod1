# -*- coding: utf-8 -*-
__author__ = 'Lunding'

import stattableOLD as st
import onesample as os
import math

template_path = r"templates_2_sample/"
decimals = 3

def estimateMean(n, S):
    return os.estimatemean(n, S)

def estimateVariance(n, S, USS):
    return os.estimatevarince(n, S, USS)

def estimateCommonMean():
    return ""

def estimateCommonVariance(f1, f2, s1sq, s2sq):
    return (f1 * s1sq + f2 * s2sq) / (f1 + f2)

def estimatemeanPDF():
    print("not implemented")

def estimatevarincePDF():
    print("not implemented")

def equalvariancePDF(f1, f2, s1sq, s2sq):
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
    result = ""
    Fresult = smax / smin
    pobs = 2 * (1 - st.Ff(Fresult, fmax, fmin))

    pobsresult = r"Da $p_{obs}(x) = " + str(round(pobs, decimals))
    if pobs > 0.05:
        include = r"\iftrue";
        pobsresult += r" > 0.05$ forkaster vi \textbf{ikke} hypotesen. Vi er dermed i en ny model; nemlig:" \
                  r" $M_{1} = X_{ij} \sim N(\mu_{i},\sigma^{2}), \quad j = 1, \dots n_{i}, i = 1,2$.\\"
    else:
        pobsresult += r" < 0.05$ \textbf{forkaster} vi hypotesen. Vi der dermed stadig i $M_{0}$.\\"
        include = r"\iffalse";

    with open (template_path + "template_equal_variance_test.txt", "r") as template_file:
        result += template_file.read() % {
            'fmax': fmax,
            'fmin': fmin,
            'smax': round(smax, decimals),
            'smin': round(smin, decimals),
            'Fresult': round(Fresult, decimals),
            'pobs': round(pobs, decimals),
            'fone': (f1 + f2),
            'sigmaone': round(estimateCommonVariance(f1, f2, s1sq, s2sq), decimals),
            'pobsresult': pobsresult,
            'include': include,
        }
    return result

def equalmeandifferentvariancePDF(f1, f2, x1, x2, s1sq, s2sq):
    result = ""
    Tresult = (x1 - x2) / (math.sqrt((s1sq / (f1 + 1)) + (s2sq / (f2 + 1))))
    fbar = (math.pow(((s1sq / (f1 + 1)) + (s2sq / (f2 + 1))), 2)) / (( (math.pow((s1sq/(f1+1)), 2))/(f1) ) + ( (math.pow((s2sq / (f1+1)) , 2))/(f2) ))
    tabelresult = st.Ft(math.fabs(Tresult), fbar)
    pobs = 2 * (1 - tabelresult)

    pobsresult = r"Da $p_{obs}(x) = " + str(round(pobs, decimals))
    if pobs > 0.05:
        include = r"\iftrue";
        pobsresult += r" > 0.05$ forkaster vi \textbf{ikke} hypotesen. Vi er dermed i en ny model; nemlig:" \
                  r" $M_{1} = X_{ij} \sim N(\mu,\sigma_{i}^{2}), \quad j = 1, \dots n_{i}, i = 1,2$.\\"
    else:
        pobsresult += r" < 0.05$ \textbf{forkaster} vi hypotesen. Vi der dermed stadig i $M_{0}$.\\"
        include = r"\iffalse";

    with open (template_path + "template_equal_mean_test_different_variance.txt", "r") as template_file:
        result += template_file.read() % {
            'x1': round(x1, decimals),
            'x2': round(x2, decimals),
            'f1': f1,
            'f2': f2,
            'n1': f1 + 1,
            'n2': f2 + 1,
            's1sq': round(s1sq, decimals),
            's2sq': round(s2sq, decimals),
            'Tresult': round(Tresult, decimals),
            'pobs': round(pobs, decimals),
            'pobsresult': pobsresult,
            'fbar': round(fbar, decimals),
            'tabelresult': round(tabelresult, decimals),
            'include': include,
        }
    return result

def confidencemean():
    print("not implemented")

def confidencevariance():
    print("not implemented")

def likelihood():
    print("not implemented")

def maximumlikelihood():
    print("not implemented")

def confidencelikelihood():
    print("not implemented")