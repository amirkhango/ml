import kNN
from array import array

datingDataMat,datingLabels= kNN.file2matrix('datingTestSet2.txt')

import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2], 15.0 * array(datingLabels) , 15.0 * array(datingLabels))
#ax.scatter(datingDataMat[:,1],datingDataMat[:,2], 15.0 * array(datingLabels) , 15.0 * array(datingLabels))
plt.show()
