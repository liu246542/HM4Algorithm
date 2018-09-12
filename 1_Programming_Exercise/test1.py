#coding=utf-8
#!/usr/bin/python3
import zuoye

'''
Test for greedy balance algorithm：
'''
manum = 4
jobInd = list(range(1,14))
jobTim = [1]*12
jobTim.append(4)

[makespan,assigns,accumulators] = zuoye.greedy_balance(manum,jobInd,jobTim)

print('Machine number: ' + str(manum) + '\r\n' + \
	    'Job indecs: ' + str(jobInd) + '\r\n' + \
	    'Job time: ' + str(jobTim) + '\r\n' + \
	    'Total time: ' + str(makespan) + '\r\n' + \
	    'Assignment: ' + str(assigns) + '\r\n' + \
	    'Time for each machine: ' + str(accumulators))
