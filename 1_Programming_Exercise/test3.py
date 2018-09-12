#!/usr/bin/python3
#coding=utf-8
import zuoye
import random
import matplotlib.pyplot as plt

'''
对中心选择问题的贪婪算法的测试：
1.选取[-20,-20],[-18,-18]...[20,20]等21个点，并绘制
2.使用贪婪算法计算出中心点
3.绘制中心点，并按顺序做上标记
'''

x=[[2*i,2*i] for i in range(-10,11)]
k=5

[x0,x1] = list(zip(*x))
plt.scatter(x0,x1)

cent = zuoye.center_select(x,k)

[cent_x,cent_y] = list(zip(*cent))
plt.scatter(cent_x,cent_y,s=50,c='r')
for i in range(k):
	plt.text(cent[i][0],cent[i][1],str(i+1),fontdict={'size':24,'color':'r'})

plt.show()