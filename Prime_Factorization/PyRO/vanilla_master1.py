import sys
import Pyro4
import time
import threading

startTime = time.time()
pFactors = []

#This program set up for 1 Pi Cluster!



#create a proxy for remote object slave1
a = Pyro4.Proxy("PYRONAME:slave1") 

#create a proxy for remote object slave2
b = Pyro4.Proxy("PYRONAME:slave2")

#composite number to factor
comp_num = int(sys.argv[1])

#######################################################################################################
#dummy functions for proper syntax into threading.Thread()
def abc():
	pFactors.append(a.pFactorSearch(2,(comp_num/4)-1, comp_num))
	
def ghi():
	pFactors.append(b.pFactorSearch((comp_num/4),(comp_num/2)-1, comp_num))	
######################################################################################################

t1 = threading.Thread(name='thr1', target=abc)
t2 = threading.Thread(name='thr2', target=ghi)

t1.start()
t2.start()

t1.join()
t2.join()

runTime = time.time() - startTime

print pFactors

print "Runtime is ", runTime
















