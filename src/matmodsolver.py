__author__ = 'Lunding'


import os
import utilities

path = os.getcwd()
template_path = r"templates/"
filename = "aflevering"
filepath =  path + "/"+filename+".tex"
name = "Rasmus"
studyid = "201303519"
sectionheader = "1 Opgave"
sectioncontent = ""
text = r"Angiv estimat og 95\%-konfidensinterval for middelvaerdien og variansen af vaegttabet."
n = 12
S = 73.0
USS = 503.12
muresult = (1.0/n) * S
sigmaresult = (1.0/(n-1.0)) * (USS - ((S*S)/n))
f = n - 1
alpha = 0.05

## estimate
with open (template_path + "template_mu_sigma_estimate.txt", "r") as template_file:
    exercisecontent = template_file.read() % {
        'n': n,
        'S': S,
        'USS': USS,
        'muresult': round(muresult, 3),
        'sigmaresult': round(sigmaresult, 3)
    }

with open (template_path + "template_exercise.txt", "r") as template_file:
    sectioncontent = template_file.read() % {
        'text': r"Angiv estimat for middelvaerdien og variansen af vaegttabet.",
        'content': exercisecontent
    }

## confidence
with open (template_path + "template_confidence_mu_sigma.txt", "r") as template_file:
    exercisecontent = template_file.read() % {
        'n': n,
        'f': f,
        'x': round(muresult, 3),
        'sigmaresult': round(sigmaresult, 3),
        'alphavalue': alpha
    }

with open (template_path + "template_exercise.txt", "r") as template_file:
    sectioncontent += template_file.read() % {
        'text': r"Angiv 95\%-konfidensinterval for middelvaerdien og variansen af vaegttabet.",
        'content': exercisecontent
    }

with open (template_path + "template_section.txt", "r") as template_file:
    content = template_file.read() % {
        'id': sectionheader,
        'content': sectioncontent
    }

with open (template_path + "template_document.txt", "r") as template_file:
    document = template_file.read() % {
        'name': name,
        'studyid': studyid,
        'content': content}

utilities.createLatexPDF(filename, document)

print("Complete\n")