#!/usr/bin python3
#coding=utf-8

import numpy as np
import os
import csv
from genData import readRawData

def logsig(x):
	return 1/(1+np.exp(-x))

if not(os.path.exists('./rawData/tlabel.npy') and os.path.exists('./rawData/tdata.npy')):
	readRawData('./rawData/t10k-images-idx3-ubyte','d','tdata.npy')
	readRawData('./rawData/t10k-labels-idx1-ubyte','l','tlabel.npy')

w1 = np.load('./network/w1.npy')
b1 = np.load('./network/b1.npy')
w2 = np.load('./network/w2.npy')
b2 = np.load('./network/b2.npy')

dataInAll = np.load('./rawData/tdata.npy').astype(np.float)
dataOuAll = np.load('./rawData/tlabel.npy').astype(np.int)
dataReg = dataInAll.T/256
showList = []

count = 0
for j in range(len(dataOuAll)):
	dataIn = dataReg[:,j:j+1]
	hiddenOut = logsig((np.dot(w1,dataIn).transpose() + b1.transpose() )).transpose()
	networkOut = logsig((np.dot(w2,hiddenOut).transpose() + b2.transpose())).transpose()

	outList = list(networkOut)
	outRes = outList.index(max(outList))
	showList.append(outRes)
	if(outRes == dataOuAll[j]):		count+=1

print(count)
print(count/len(dataOuAll))
# for index,item in enumerate(showList):
# 	print('序号{:<2}：{:}:{}'.format(index,item,dataOuAll[index]))