#!/usr/bin/env python
#import sys

#print "hello"

#print sys.argv[1]*3
#print sys.argv[2]*6

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

#create a proxy for remote object slave3
c = Pyro4.Proxy("PYRONAME:slave3") 

#create a proxy for remote object slave4
d = Pyro4.Proxy("PYRONAME:slave4")

#create a proxy for remote object slave5
e = Pyro4.Proxy("PYRONAME:slave5") 


#composite number to factor
comp_num = int(sys.argv[1])

#######################################################################################################
#dummy functions for proper syntax into threading.Thread()
def abc():
	pFactors.append(a.pFactorSearch(2,(comp_num/10)-1, comp_num))
	
def ghi():
	pFactors.append(b.pFactorSearch((comp_num/10),(2*comp_num/10)-1, comp_num))

def jkl():
	pFactors.append(c.pFactorSearch((2*comp_num/10),(3*comp_num/10)-1, comp_num))
	
def mno():
	pFactors.append(d.pFactorSearch((3*comp_num/10),(4*comp_num/10)-1, comp_num))

def pqr():
	pFactors.append(e.pFactorSearch((4*comp_num/10),(5*comp_num/10)-1, comp_num))
	
######################################################################################################

t1 = threading.Thread(name='thr1', target=abc)
t2 = threading.Thread(name='thr2', target=ghi)
t3 = threading.Thread(name='thr3', target=jkl)
t4 = threading.Thread(name='thr4', target=mno)
t5 = threading.Thread(name='thr5', target=pqr)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

runTime = time.time() - startTime

#cleaning up the pFactors list
#####################################################
pFactors =filter(None,pFactors) #remove empty parts from list
pFactors2 = str(pFactors)
a,b = pFactors2.split()
a = a.translate(None, '[],')
b = b.translate(None, '[],')
#########################################################


from pylab import *

pos = arange(3)+.5 

barh(pos,(3,5,2), align='center', color='#b8ff5c')

yticks(pos,('a','b','c'))

xlabel('sdfdff')
ylabel('sdfdf')

title('esresr')
grid(True)
show()



#print "Factors: p = " + a + ".. q = " + b + " ||      Runtime: " + str(runTime)



