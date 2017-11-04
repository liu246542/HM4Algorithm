#!/usr/bin/ python3
#coding=utf-8

'''
获取测试集图片的函数
图片保存在testpics文件夹中
'''
import numpy as np
import matplotlib.pyplot as plt

def showPic(img,index):
	frame = plt.gca()	
	frame.axes.get_yaxis().set_visible(False)	
	frame.axes.get_xaxis().set_visible(False)
	plt.axis('off')
	fig = plt.figure()

	plt.imshow(img,cmap='gray')
	fig.savefig('./testpics/' + str(index)+ '.png',dpi=20)
	plt.close()
	# plt.show()

dataInAll = np.load('./dataset/testdata.npy').astype(np.float)

# for j in range(28000):
for j in range(1000):	
	showPic(dataInAll[j].reshape(28,28),j)