#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import time

start_time = time.time()

import cluster
import hashlib
import sys
import math

def factor_list_empty(lst):
        for i in lst:
                if i:
                        return False
        return True



iTotal = 0

#Initialize the task scheduler
CLUSTER_SIZE = 5 #Set to number of worker processes in the cluster.
cluster.round_robin_init(CLUSTER_SIZE)

n = int(sys.argv[1])
print "Finding pi with following number of iterations: " + str(n)


#upper_lim = math.sqrt(n)
upper_lim = n #original



chunk_size = int((upper_lim)/CLUSTER_SIZE)
print "Calculated chunk_size: " + str(chunk_size)
# Avoid a chunk size of zero
if chunk_size == 0:
        chunk_size = 1


#create the work list for each node
i = 0
work_list = []
while i <= (upper_lim) + 1:
        tmp_list = []
        tmp_list.append(i)
        i += chunk_size
        tmp_list.append(i)
        i += 1
        work_list.append(tmp_list)

print work_list

factors_list = []


task_count = 0
emp_nodes = []

for i in work_list:
    task_count += 1
    emp_nodes.append(cluster.concurrent_task('piCalc','t_'+str(task_count),i[0],i[len(i)-1]))

for i in range(1,task_count+1):
        cluster.wait_for_task('t_'+str(i),emp_nodes[i-1])
        factors_list.append(cluster.get_output_from_task('t_'+str(i),emp_nodes[i-1]))


#add list entries from iResults	
print factors_list

for j in factors_list:
	iTotal += j

#final determination of pi
pi=4*iTotal
pi2 = pi/n

print pi2

delta_time = time.time() - start_time


print "Number of clients used: " + str(CLUSTER_SIZE)

print "Time taken: " + str(delta_time) + " seconds."
