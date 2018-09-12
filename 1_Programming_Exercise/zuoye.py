#!/usr/bin/python3
#conding=utf-8
import random

########################################################################
'''
Greedy Balance Algorithm for Loading Balancing Problem.
Input:
machine_num : machine number,int
job_index   : job index,list
job_time    : job time,list

output:
maskspan    : total time，int
assigns     : jobs in each machine，list
accumulators: time in each machine，list
'''
def greedy_balance(machine_num,job_index,job_time):
	# init
	makespan = 0
	assigns = [list() for i in range(machine_num)]
	accumulators = [0] * machine_num

	# assign each job to minimal load machine
	for i in range(len(job_index)):
		min_index = accumulators.index(min(accumulators))
		assigns[min_index].append(job_index[i])
		accumulators[min_index] += job_time[i]

	makespan = max(accumulators)
	return makespan,assigns,accumulators
########################################################################
'''
Sorted Balance Algorithm for Loading Balancing Problem.
Input:
machine_num : machine number, int
job_index   : job index, list
job_time    : job time, list

Output:
maskspan    : total time, int
assigns     : jobs in each machine, list
accumulators: time in each machine, list
'''
def sorted_balancd(machine_num,job_index,job_time):
	[job_index,job_time] = zip(*sorted(zip(job_index,job_time),key=lambda x:x[1], reverse=True))
	makespan,assigns,accumulators = greedy_balance(machine_num,job_index,job_time)
	return makespan,assigns,accumulators

########################################################################
'''
Greedy Algorithm for Center Slection Problem.
输入：
x    :  二维列表，x坐标和y坐标构成每一个元素,list
k    :  中心点的数量，int

输出：
cent : 二维列表，记录k个中心点的坐标,list
'''
def center_select(x,k):
	cent = [x.pop(0)]
	for i in range(1,k):
		dist = []
		for sigPoint in x:
			dist.append(count_dist(cent,sigPoint))
		min_dist = list(map(min,dist))
		max_min_dist = min_dist.index(max(min_dist))
		cent.append(x.pop(max_min_dist))
	return cent

def count_dist(sourPoint,destPoint):
	#此函数是用于计算二维空间一系列的点(sourPoint)到某一个点(destPoint)的距离序列
	distList = []
	for sinPoint in sourPoint:
		distList.append(((sinPoint[0] - destPoint[0])**2 + (sinPoint[0] - destPoint[0])**2)**0.5)
	return distList

########################################################################
'''
K-Means Clustering Algorithm
输入：
x            :  二维列表，x坐标和y坐标构成每一个元素,list
k            :  中心点的数量，int
max_iter     :  迭代的次数
输出：
class_index  :  记录距离每个点最近的中心点的列表下标,list,每个值的范围是0～k-1
cent         :  二维列表，记录k个中心点的坐标,list
'''
def K_Means(x,k,max_iter):
	cent = random.sample(x,k)
	for i in range(max_iter):
		dist = []
		for sigPoint in x:
			dist.append(count_dist(cent,sigPoint))
		class_index = list(map(lambda a: a.index(min(a)),dist))

		for j in range(k):
			x_index = [i for i in range(len(class_index)) if class_index[i] == j]
			x_sub = [x[i] for i in x_index]
			[x_sum,y_sum] = list(map(sum,(list(zip(*x_sub)))))
			cent[j] = [x_sum/len(x_index),y_sum/len(x_index)]
	return class_index,cent

########################################################################