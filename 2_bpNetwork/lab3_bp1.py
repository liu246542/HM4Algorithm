#!/usr/bin/python3
#conding = utf-8

import numpy as np
import matplotlib.pyplot as plt
import os

from genNet import bpNetwork
from genData import readCsv

if __name__ == '__main__':

	if not(os.path.exists('./dataset/label.npy') and os.path.exists('./dataset/trandata.npy')):
		readCsv('./dataset/train.csv')
	
	#读取数据
	tranOu = np.load('./dataset/label.npy')
	tranIn = np.load('./dataset/trandata.npy')
	
	maxepochs = 50
	learnrate = 0.035
	errorfinal = 0.65*10**(-3)
	samnum = 42000
	indim = 784
	outdim = 10
	hiddenunit = 30
	
	bpNetwork(tranIn,tranOu,maxepochs,errorfinal,learnrate,indim,outdim,hiddenunit,samnum)