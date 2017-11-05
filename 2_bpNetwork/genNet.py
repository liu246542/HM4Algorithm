#!/usr/bin python3
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import os
import csv

'''
定义BP神经网络训练函数
输入：
=======================================
	dataInAll  输入的所有数据
	dataOutAll 输入对应的输出数据
	maxepochs  最大迭代次数
	errorfinal 允许最小误差
	learnrate  学习率
	indim      输入层神经元个数
	outdim     输出层神经元个数
	hiddenunit 隐层神经元个数
	samnum     需要训练的样本个数
=======================================
输出：
训练后的保存在w1.npy,w2.npy,b1.npy,b2.npy四个文件中
'''

def bpNetwork(dataInAll,dataOutAll,maxepochs,errorfinal,learnrate,indim,outdim,hiddenunit,samnum):
	dataInAll = (dataInAll.T/256)
	dataOutAll = dataOutAll.T
	
	w1 = 0.2*np.random.rand(hiddenunit,indim)-0.1
	b1 = 0.2*np.random.rand(hiddenunit,1)-0.1
	w2 = 0.2*np.random.rand(outdim,hiddenunit)-0.1
	b2 = 0.2*np.random.rand(outdim,1)-0.1

	errhistory = [float('inf') for x in range(maxepochs)]

	#针对总迭代次数的for循环
	for k in range(maxepochs):
		#针对每一个样本的for循环
		for j in range(samnum):
			dataIn = dataInAll[:,j:j+1]

			dataOut = np.zeros(outdim)
			dataOut[int(dataOutAll[j])] = 1
			dataOut = dataOut.reshape(10,1)

			hiddenOut = logsig((np.dot(w1,dataIn).transpose() + b1.transpose() )).transpose()			
			networkOut = logsig((np.dot(w2,hiddenOut).transpose() + b2.transpose())).transpose()
			
			err = dataOut - networkOut
			sse = sum(sum(err**2))
			errhistory[k] = sse if errhistory[k]>sse else errhistory[k]
		
			delta2 = err * networkOut * (1-networkOut)
			delta1 = np.dot(w2.transpose(),delta2)*hiddenOut*(1-hiddenOut)
			dw2 = np.dot(delta2,hiddenOut.transpose())
			db2 = np.dot(delta2,np.ones((1,1)))

			dw1 = np.dot(delta1,dataIn.transpose())
			db1 = np.dot(delta1,np.ones((1,1)))

			w2 += learnrate*dw2
			b2 += learnrate*db2
			w1 += learnrate*dw1
			b1 += learnrate*db1
		if errhistory[k] < errorfinal:
			break

	np.save('./network/w1.npy',w1)
	np.save('./network/b1.npy',b1)
	np.save('./network/w2.npy',w2)
	np.save('./network/b2.npy',b2)
	np.save('./network/err.npy',errhistory)

#定义激活函数
def logsig(x):
	return 1/(1+np.exp(-x))