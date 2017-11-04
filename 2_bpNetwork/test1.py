#!/usr/bin python3
#coding=utf-8

import numpy as np
import os
import csv
import matplotlib.pyplot as plt

def logsig(x):
	return 1/(1+np.exp(-x))

def readCsv(filename):
	dataList = []
	with open(filename,'r') as f:
		for sigLine in csv.reader(f):
			dataList.append(sigLine)
	if dataList[0][0] == 'label':
		dataList.remove(dataList[0])
		dataArr = np.array(dataList).astype(np.float)		
		np.save('./dataset/label.npy',dataArr[:,0])
		np.save('./dataset/trandata.npy',dataArr[:,1:])
	else :
		dataList.remove(dataList[0])
		dataArr = np.array(dataList).astype(np.float)
		np.save('./dataset/testdata.npy',dataArr)
	

if not(os.path.exists('./dataset/testdata.npy')):	
	readCsv('./dataset/test.csv')

w1 = np.load('./network/w1.npy')
b1 = np.load('./network/b1.npy')
w2 = np.load('./network/w2.npy')
b2 = np.load('./network/b2.npy')

dataInAll = np.load('./dataset/testdata.npy').astype(np.float)
dataReg = dataInAll.T/256
showList = []

for j in range(20):
	dataIn = dataReg[:,j:j+1]
	hiddenOut = logsig((np.dot(w1,dataIn).transpose() + b1.transpose() )).transpose()
	networkOut = logsig((np.dot(w2,hiddenOut).transpose() + b2.transpose())).transpose()

	outList = list(networkOut)
	showList.append(outList.index(max(outList)))

for index,item in enumerate(showList):
	print('序号{:<2}：{:}'.format(index,item))