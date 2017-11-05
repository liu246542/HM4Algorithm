#!/usr/bin python3
#coding=utf-8

import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from genData import readCsv


def logsig(x):
	return 1/(1+np.exp(-x))

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