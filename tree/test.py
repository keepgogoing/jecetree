from numpy import *
import operator
#
# def classify0(inX,dataSet,labels,key):
#     dataSetSize = dataSet.shape[0]
#     resultDataSet = tile(inX,(dataSetSize,1))-dataSet
#     resultData = resultDataSet**2
#     result = resultData**0.5
#     sortResult = result.argsort()
#     resultLabels={}
#     for i in range(key):
#         lab = labels(sortResult[i])
#         resultLabels[lab]=resultLabels.get(lab,0)+1
#     finalResult = sorted(resultLabels.items(),key=operator.itemgetter(1),reverse=True)
#     return finalResult
#
#