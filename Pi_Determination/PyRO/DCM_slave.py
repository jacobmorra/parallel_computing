#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cluster
import sys
import logging
import Pyro4
from random import *
from math import sqrt
from cluster_slave_headers import *

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

					
# Define how the slave program should set it's self up
def slave_init(net_iface, ns_ip, node_id):
        cluster.network_init(net_iface,ns_ip,node_id)
        #Hook any other initialization methods here

# BEGINNING OF SHARED FUNCTION DEFINITIONS

def piCalc(a,b):
    	logging.debug('Starting')
    	inside=0
	for i in range(a,b):
    	    x=random()
	    y=random()
	    if sqrt(x*x+y*y)<=1:
		inside+=1
	logging.debug('Exiting')
	print inside
	return inside

# This function must be made available to the API

slave_tasks_list['piCalc'] = piCalc


# END OF SHARED FUNCTION DEFINITION
