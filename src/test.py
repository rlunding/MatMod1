__author__ = 'Lunding'

# http://stackoverflow.com/questions/8085520/generating-pdf-latex-with-python-script

import os
import subprocess
import shlex

path = os.getcwd()
template_path = r"templates/"
filename = "result"
filepath =  path + "/"+filename+".tex"
name = "Rasmus"
studyid = "201303519"
section = "Aflevering 1"
content1 = ""

n = 12.0
S = 73.0
USS = 503.12
muresult = (1.0/n) * S
sigmaresult = (1.0/(n-1.0)) * (USS - ((S*S)/n))

with open (template_path + "template_mu_sigma_estimate.txt", "r") as template_file:
    content1 = template_file.read() % {
        'n' : n,
        'S' : S,
        'USS' : USS,
        'muresult' : round(muresult, 3),
        'sigmaresult' : round(sigmaresult, 3)
    }


with open (template_path + "template_document.txt", "r") as template_file:
    content = template_file.read() % {
        'name' : name,
        'studyid' : studyid,
        'section1' : section,
        'content1' : content1}

print(content)

with open(filename+".tex", 'w') as f:
    f.write(content)

proc = subprocess.Popen(shlex.split('pdflatex '+filename+'.tex'))
proc.communicate()

os.unlink(filename+".tex")
os.unlink(filename+".aux")
os.unlink(filename+".log")
os.unlink(filename+".out")

print("Complete")