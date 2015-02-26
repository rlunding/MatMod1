__author__ = 'Lunding'

import scipy.stats
import math

def chi2(alpha, dof):
    return scipy.stats.chi2.ppf(alpha, dof)

def t(alpha, dof):
    return scipy.stats.t.ppf(alpha, dof)

def Ft(value, dof):
    return scipy.stats.t.cdf(value, dof)

def u(alpha):
    return scipy.stats.norm.ppf(alpha)
    #return 1.96

def Phi(value):
    return scipy.stats.norm.cdf(value)

def PhiInverse(value):
    return scipy.stats.norm.ppf(value)

def Ff(value, f1, f2):
    return scipy.stats.f.cdf(value, f1, f2)

def Fchi2(value, dof):
    return scipy.stats.chi2.cdf(value, dof)
