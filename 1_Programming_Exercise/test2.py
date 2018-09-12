#!/usr/bin/python3
#coding=utf-8
import zuoye

'''
Test for sorted greedy balance algorithm
'''
manum = 4
jobInd = list(range(1,14))
jobTim = [1]*12 + [4]

[makespan,assigns,accumulators] = zuoye.sorted_balancd(manum,jobInd,jobTim)

print('Machine number: ' + str(manum) + '\r\n' + \
      'Job indecs: ' + str(jobInd) + '\r\n' + \
      'Job time: ' + str(jobTim) + '\r\n' + \
      'Total time: ' + str(makespan) + '\r\n' + \
      'Assignment: ' + str(assigns) + '\r\n' + \
      'Time for each machine: ' + str(accumulators))