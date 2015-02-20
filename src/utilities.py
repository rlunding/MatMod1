__author__ = 'Lunding'

import os
import subprocess
import shlex
import variables

template_path = variables.template_path

def loadformula(formula, obs):
    with open ("formulas_" + obs + "/formula_" + formula + ".txt", "r") as template_file:
        return template_file.read()


def createexercise(header, content):
    with open (template_path + "template_exercise.txt", "r") as template_file:
        exercise = template_file.read() % {
            'text': header,
            'content': content
        }
    return exercise

def createsection(header, content):
    with open (template_path + "template_section.txt", "r") as template_file:
        section = template_file.read() % {
            'id': header,
            'content': content
            }
    return section

def createdocument(content):
    with open (template_path + "template_document.txt", "r") as template_file:
        document = template_file.read() % {
            'name': variables.name,
            'studyid': variables.studyid,
            'content': content}
    return document

def createLatexPDF(filename, document):
    print(document)

    with open(filename+".tex", 'w') as f:
        f.write(document)

    proc = subprocess.Popen(shlex.split('pdflatex '+filename+'.tex'))
    proc.communicate()

    os.unlink(filename+".tex")
    os.unlink(filename+".aux")
    os.unlink(filename+".log")
    os.unlink(filename+".out")