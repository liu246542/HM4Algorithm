#!/usr/local/bin python3
#codint=utf-8

import matplotlib.pyplot as plt
from matplotlib import animation
import copy

def general_method(machine_num,job_index,job_time):
  # init
  makespan = 0
  assigns = [list() for i in range(machine_num)]
  accumulators = [0] * machine_num
  temp_accumulators = [0] * machine_num

  # assign each job to minimal load machine
  for i in job_index:
    for item in range(machine_num):
      temp_accumulators[item] += job_time[item][i]
    min_index = temp_accumulators.index(min(temp_accumulators))

    assigns[min_index].append('J' + str(i+1))
    accumulators[min_index] += job_time[min_index][i]
    temp_accumulators = copy.copy(accumulators)
  makespan = max(accumulators)
  return makespan,assigns,accumulators

if __name__ == '__main__':
  machine_num = 3
  job_index = list(range(10))
  job_index.reverse()
  job_time = []
  job_time.append(list(range(2,21,2)))
  job_time.append(list(range(2,21,2)))
  job_time.append(list(range(1,11)))
  print(general_method(machine_num,job_index,job_time))