#coding=utf-8
#!/usr/bin/python3
import zuoye
import random
import matplotlib.pyplot as plt

'''
对K-Means算法的测试：
1.随机生成100个点，坐标范围(0,50)
2.调用K_Means()函数，k=5,max_iter=100，生成中心点
3.根据class_index将随机生成的点按不同颜色绘制
4.绘制中心点
'''
x = [[random.uniform(0,50),random.uniform(0,50)] for i in range(100)]
k = 4

[class_index,cent] = zuoye.K_Means(x,k,100)

color_sty = ['red','aqua','darkblue','chartreuse']#事先定义颜色列表

##绘制散点图
for j in range(k):
	x_index = [i for i in range(len(class_index)) if class_index[i] == j]
	x_sub = [x[i] for i in x_index]
	[x0,x1] = zip(*x_sub)
	plt.scatter(x0,x1,c=color_sty[j])
	[cent_x,cent_y] = list(zip(*cent))	
	plt.scatter(cent_x,cent_y,s=80,c='mintcream')
	plt.text(cent[j][0],cent[j][1],str(j+1),fontdict={'size':24,'color':'r'})

plt.show()