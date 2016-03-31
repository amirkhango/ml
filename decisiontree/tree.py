from math import log
def createDataSet():
    dataSet =[ [1,1,'yes'],
                [1,1,'yes'],
                [1,0,'no'],
                [0,1,'no'],
                [0,1,'no']
            ]
    labels = ['no surfacing','flippers']
    return dataSet,labels
def calcShannonEnt(DataSet):
    nSamples = len(DataSet)
    labelCounts = {}
    for featVec in DataSet:
        label = featVec[-1]
        if label in labelCounts.keys():
            labelCounts[label] += 1
        else:
            labelCounts[label] = 1
    shannonEnt = 0
    for key in labelCounts:
        prob =float( labelCounts[key]) / nSamples
        info = (-1)*log(prob,2) 
        shannonEnt += prob * info
    return shannonEnt
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

