__author__ = 'Lunding'

import scipy.stats


def chi2(alpha, dof):
    return scipy.stats.chi2.ppf(alpha, dof)

def t(alpha, dof):
    return scipy.stats.t.ppf(alpha, dof)

def Ft(value, dof):
    return scipy.stats.t.cdf(value, dof)

def u():
    return 1.96

def Ff(value, f1, f2):
    return scipy.stats.f.cdf(value, f1, f2)

