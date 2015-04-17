__author__ = 'Lunding'

import stattable as st


def calculateSchema(observations, n=None):
    if n is None:
        n = len(observations)
    observations.sort()
    sizeOfObservations = len(observations)
    count = 0
    a = 1
    sumA = 0
    outputValues = []
    while count < sizeOfObservations:
        y = observations[count]
        if count + 1 < sizeOfObservations and y == observations[count+1]:
            a +=1
            count += 1
            continue
        k = sumA + a
        p = (sumA + k) / (2.0 * n)
        u = st.PhiInverse(p)
        outputValues.append((y, a, k, p, u))
        sumA += a
        a = 1
        count += 1
    printSchema(outputValues)

def printSchema(inputValues):
    for i in range(len(inputValues)):
        strline = ""
        for j in range(len(inputValues[i])):
            strline += format(round(inputValues[i][j], 2), '.2f') + "\t\t"
        print(strline)