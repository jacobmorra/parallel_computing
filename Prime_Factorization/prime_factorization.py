#!/usr/bin/env python
# File: sum_primes.py
# Author: Vitalii Vanovschi
# Desc: This program demonstrates parallel computations with pp module
# It calculates the sum of prime numbers below a given integer in parallel
# Parallel Python Software: http://www.parallelpython.com

import math
import sys
import pp
import logging

def isPrime(i):
    k=2
    while k<i:
        #if i has a factor, not a prime
        if (i%k==0):
            return 0
        #otherwise, test more k values
        else:
            k+=1
    else:
        return 1

def pFactorSearch(start_value,end_value,composite_num):
	logging.debug('Starting')
	i=start_value
	j=end_value
	c=composite_num
        
	pFactors = []

	#while i<=j
	while i<=j:
		#print i
		#if it's a factor
		if c%i==0:
			#if it's prime.. find q s.t i*q=c, and you're done!
			if isPrime(i):
				q=c/i
				pFactors.append(i)
				pFactors.append(q)
			i=c+1 #exit the program
		else:
			i+=1 #increment by 2
#time.sleep(5)
	logging.debug('Exiting')		
	return pFactors

# tuple of all parallel python servers to connect with
ppservers = ("10.124.7.69","10.124.7.82","10.124.7.80","10.124.7.81","10.124.7.83")
#ppservers = ("127.0.0.1:60000", )

job_server = pp.Server(1, ppservers=ppservers)

print "Starting pp with", job_server.get_ncpus(), "workers"

cn = int(sys.argv[1])

a = int(math.floor(cn/10))
b = int(math.floor(2*cn/10))
c = int(math.floor(3*cn/10))
d = int(math.floor(4*cn/10))
e = int(math.floor(5*cn/10))

print a
print b

job1 = job_server.submit(pFactorSearch, (2,a-1,cn, ), (isPrime, ), ("math", "logging",))
job2 = job_server.submit(pFactorSearch, (a,b-1,cn, ), (isPrime, ), ("math", "logging",))
job3 = job_server.submit(pFactorSearch, (b,c-1,cn, ), (isPrime, ), ("math", "logging",))
job4 = job_server.submit(pFactorSearch, (c,d-1,cn, ), (isPrime, ), ("math", "logging",))
job5 = job_server.submit(pFactorSearch, (d,e-1,cn, ), (isPrime, ), ("math", "logging",))
# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will
# wait here until result is available
r1 = job1()
r2 = job2()
r3 = job3()
r4 = job4()
r5 = job5()

pFactors =[]
pFactors.append(r1)
pFactors.append(r2)
pFactors.append(r3)
pFactors.append(r4)
pFactors.append(r5)

print pFactors

job_server.print_stats()

# Parallel Python Software: http://www.parallelpython.com
