#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cluster
import sys

from cluster_slave_headers import *


# Define how the slave program should set it's self up
def slave_init(net_iface, ns_ip, node_id):
        cluster.network_init(net_iface,ns_ip,node_id)
        #Hook any other initialization methods here

# BEGINNING OF SHARED FUNCTION DEFINITIONS



""" Factor search must be able to handle large numbers without
using too much RAM causing MemoryErrors. Therefore range() must not be
used """

def factor_search(beginning,end,comp_num):
        i = beginning
        factors = []
        while i <= end:
                if comp_num % i == 0:
                        #We have found a factor
                        factors.append(i)
                i += 1
        return factors

# This function must be made available to the API

slave_tasks_list['factor_search'] = factor_search




def primetest(num):
        # prime numbers are greater than 1
        if num > 1:
                j=2
                # check for factors
                while j < num:
                #CAN'T USE RANGE DUE TO MEMORY CONSTRAINTS
                #for j in range(2,num):
                        if (num % j) == 0:
                           #print(num,"is not a prime number")
                           #print(j,"times",num//j,"is",num)
                           break
                        else:
                                j+=1
                else:
                        print(num,"is a prime number")
                        return 1
       
        # if input number is less than
        # or equal to 1, it is not prime
        else:
           #print(num,"is not a prime number")
           return 0
        


def p_factor_search(beginning,end,comp_num):
        i = beginning
        factors = []
        while i <= end:
                if comp_num % i == 0:
                        #We have found a factor..is it prime?
						if (primetest(i) == 1):
							factors.append(i)
                i += 1
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
