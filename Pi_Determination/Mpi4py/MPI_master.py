#!/usr/bin/env python
from __future__ import division

# File: sum_primes.py
# Author: Vitalii Vanovschi
# Desc: This program demonstrates parallel computations with pp module
# It calculates the sum of prime numbers below a given integer in parallel
# Parallel Python Software: http://www.parallelpython.com
import logging
import sys
from math import sqrt
from random import *
import pp
import time

start_time = time.time()

cluster_size = 5
n = int(sys.argv[1])
sub_n = int(n/cluster_size)
iResults=[]
iTotal=0

def abab(i):
	return i
	
def piCalc(a,b):
    	logging.debug('Starting')
    	inside=0
	for i in range(a,b):
    	    x=random.random()
	    y=random.random()
	    if math.sqrt(x*x+y*y)<=1:
		inside+=1
	#print abab(5)
	logging.debug('Exiting')
	#print inside
	return inside

# tuple of all parallel python servers to connect with
ppservers = ("10.124.7.69","10.124.7.82","10.124.7.80","10.124.7.81","10.124.7.83")

job_server = pp.Server(1, ppservers=ppservers)

print "Starting pp with", job_server.get_ncpus(), "workers"

n = int(sys.argv[1])

job1 = job_server.submit(piCalc, (0,sub_n, ), (abab, ), ("math", "logging","random"))                      #"random",))
job2 = job_server.submit(piCalc, (sub_n + 1,2 * sub_n, ), (abab, ),("math", "logging","random"))           #"random",))
job3 = job_server.submit(piCalc, (2 * sub_n + 1,3 * sub_n, ), (abab, ), ("math", "logging","random"))      #"random",))
job4 = job_server.submit(piCalc, (3 * sub_n + 1,4 * sub_n, ), (abab, ), ("math", "logging","random"))      #"random",))
job5 = job_server.submit(piCalc, (4 * sub_n + 1,5 * sub_n, ), (abab, ), ("math", "logging","random"))      #"random",))

# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will
# wait here until result is available
r1 = job1()
r2 = job2()
r3 = job3()
r4 = job4()
r5 = job5()

print r1

iResults.append(r1)
iResults.append(r2)
iResults.append(r3)
iResults.append(r4)
iResults.append(r5)

#print iResults

#add list entries from iResults	
for j in iResults:
	iTotal += j
	
#print iTotal


#final determination of pi
pi=4*iTotal
pi2 = pi/n

print pi2

job_server.print_stats()

# Parallel Python Software: http://www.parallelpython.com
delta_time = time.time() - start_time


print "Time taken: " + str(delta_time) + " seconds."
