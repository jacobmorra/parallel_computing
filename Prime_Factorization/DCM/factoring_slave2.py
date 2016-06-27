#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cluster
import sys
import logging

from cluster_slave_headers import *

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

					
# Define how the slave program should set it's self up
def slave_init(net_iface, ns_ip, node_id):
        cluster.network_init(net_iface,ns_ip,node_id)
        #Hook any other initialization methods here

# BEGINNING OF SHARED FUNCTION DEFINITIONS


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

def p_factor_search(beginning,end,comp_num):
        logging.debug('Starting')
		i = beginning
        j=end
        c=comp_num
		
		factors = []
        
		while i<=j:
            #print i
            #if it's a factor
            if c%i==0:
                #if it's prime.. find q s.t i*q=c, and you're done!
                if isPrime(i):
                    q=c/i
                    pFactors.append(i)
                    pFactors.append(q)
                i=c+1 #reset i to be out of range, close loop   
            else:
                i+=1
        logging.debug('Exiting')
	return factors

# This function must be made available to the API

slave_tasks_list['p_factor_search'] = p_factor_search		




# def p_factor_search(beginning,end,comp_num):
        # #if 2 is not a factor, skip
        # if comp_num % 2 !=0:
                # i = beginning
                # factors = []
                # while i <= end:
                        # #Here we are skipping all multiples of 2
                        # if i%2!=0:
                                # if comp_num % i == 0:
                                        # #We have found a factor..is it prime?
                                        # if (primetest(i) == 1):
                                                # factors.append(i)
                                # i+=1
                        # else:
                                # i += 1
                # return factors

        # #else, don't skip factors of 2
        # else:
                # i = beginning
                # factors = []
                # while i <= end:
                        # if comp_num % i == 0:
                                # #We have found a factor..is it prime?
                                # if (primetest(i) == 1):
                                        # factors.append(i)
                        # i += 1
                # return factors
        
# # This function must be made available to the API

# slave_tasks_list['p_factor_search'] = p_factor_search

# END OF SHARED FUNCTION DEFINITION
