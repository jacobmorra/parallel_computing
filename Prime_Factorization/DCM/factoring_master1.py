#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cluster
import hashlib
import time
import sys
import math


def factor_list_empty(lst):
        for i in lst:
                if i:
                        return False
        return True

start_time = time.time()

#Initialize the task scheduler
CLUSTER_SIZE = 2 #Set to number of worker processes in the cluster.
cluster.round_robin_init(CLUSTER_SIZE)

composite_number = int(sys.argv[1])
print "Finding non-trivial prime factors of " + str(composite_number)


#upper_lim = math.sqrt(composite_number)
upper_lim = composite_number/2 #original



chunk_size = (upper_lim - 1)/CLUSTER_SIZE
print "Calculated chunk_size: " + str(chunk_size)
# Avoid a chunk size of zero
if chunk_size == 0:
        chunk_size = 1


#create the work list for each node
i = 2
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
    emp_nodes.append(cluster.concurrent_task('p_factor_search','t_'+str(task_count),i[0],i[len(i)-1],composite_number))

for i in range(1,task_count+1):
        cluster.wait_for_task('t_'+str(i),emp_nodes[i-1])
        factors_list.append(cluster.get_output_from_task('t_'+str(i),emp_nodes[i-1]))


print "Non trivial prime factors of " + str(composite_number) + " are..."

for i in range(0,len(factors_list)):
        for j in range(0,len(factors_list[i])):
                print factors_list[i][j]

if factor_list_empty(factors_list):
        print "...none. " + str(composite_number) + " is prime."
else:
        p = factors_list[0][len(factors_list)-1]
        q = factors_list[0][len(factors_list)-2]
        if (p*q)==composite_number:
                print "p = " + str(p)
                print "q = " + str(q)
                

delta_time = time.time() - start_time


print "Number of clients used: " + str(CLUSTER_SIZE)

print "Time taken: " + str(delta_time) + " seconds."
