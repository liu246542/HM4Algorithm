#coding=utf-8
#!/usr/bin/python3
import zuoye

'''
对负载平衡的贪婪算法的测试：
'''
manum = 3#机器数量
jobInd = [1,2,3,4,5,6,7]#任务序列
jobTim = [1,2,3,4,5,6,7]#任务时间

[makespan,assigns,accumulators] = zuoye.greedy_balance(manum,jobInd,jobTim)

# makespan,assigns,accumulators = zuoye1.sorted_balancd(manum,jobInd,jotTim)

print('机器数量：' + str(manum) + '\r\n' + \
	    '任务序列：' + str(jobInd) + '\r\n' + \
	    '任务时间：' + str(jobTim) + '\r\n' + \
	    '总时间：' + str(makespan) + '\r\n' + \
	    '任务分配：' + str(assigns) + '\r\n' + \
	    '每台机器的时间：' + str(accumulators))