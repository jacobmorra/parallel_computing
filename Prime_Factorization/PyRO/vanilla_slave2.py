#!/usr/bin/python

import Pyro4
import threading
import logging
import math

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

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

class Slave2:
    def __init__(self):
        pass
    def pFactorSearch(self,start_value,end_value,composite_num):
        logging.debug('Starting')
	i=start_value
        j=end_value
        c=composite_num
        
        pFactors = []

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
	return pFactors

b = Slave2()

daemon = Pyro4.Daemon()                # make a Pyro daemon

daemon = Pyro4.Daemon("10.124.7.73")                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(b)   # register the greeting maker as a Pyro object
ns.register("slave2", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
