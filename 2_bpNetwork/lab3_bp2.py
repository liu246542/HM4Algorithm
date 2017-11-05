#!/usr/bin python3
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import os

from genNet import bpNetwork
from genData import readRawData

if __name__ == '__main__':

	if not(os.path.exists('./rawData/label.npy') and os.path.exists('./rawData/trandata.npy')):
		readRawData('./rawData/train-images-idx3-ubyte','d','trandata.npy')
		readRawData('./rawData/train-labels-idx1-ubyte','l','label.npy')
	
	#读取数据
	tranOu = np.load('./rawData/label.npy')
	tranIn = np.load('./rawData/trandata.npy')
	
	maxepochs = 10
	learnrate = 0.035
	errorfinal = 0.65*10**(-3)
	samnum = 60000
	indim = 784
	outdim = 10
	hiddenunit = 85
	
	bpNetwork(tranIn,tranOu,maxepochs,errorfinal,learnrate,indim,outdim,hiddenunit,samnum)