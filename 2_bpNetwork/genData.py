#!/usr/bin python3
#coding=utf-8

import csv
import struct
import numpy as np

'''
读取csv数据的函数
'''
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

'''
读取二进制数据的函数
filename -> 代表文件名
flag     -> 数据集类型，'l'代表标签，'d'代表数据
saveFile -> 需要保存为的文件名
'''
def readRawData(filename,flag,saveFile):
	labBuf = open(filename,'rb').read()
	index = 0
	if flag == 'l':
		magNum,itemNum = struct.unpack_from('>II',labBuf,index)
		index += struct.calcsize('>II')
		labList = struct.unpack_from('>' + str(itemNum) + 'B',labBuf,index)
		# return np.array(labList)
		np.save('./rawData/' + saveFile,np.array(labList))
	elif flag == 'd':
		magNum,itemNum,imgrows,imgcols = struct.unpack_from('>IIII',labBuf,index)
		index += struct.calcsize('>IIII')
		pixMul = str(imgrows * imgcols*itemNum)
		dataList = struct.unpack_from('>' + pixMul + 'B',labBuf,index)
		dataList = np.array(dataList)
		dataList = dataList.reshape(itemNum,imgrows*imgcols)
		# return dataList
		np.save('./rawData/' + saveFile,dataList)
	else :
		return 0