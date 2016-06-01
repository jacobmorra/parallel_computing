#!/usr/bin/env python
#import sys

#print "hello"

#print sys.argv[1]*3
#print sys.argv[2]*6

#########################################################################################     PART 1 
import sys
import Pyro4
import time
import threading

startTime = time.time()
pFactors = []


#All 5 Pis should be connected regardless of desired cluster_size

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
cluster_size = int(sys.argv[2]) #desired size of pi cluster

#########################################################################################     PART 2 

if cluster_size == 1:
	pFactors.append(a.pFactorSearch(2,(comp_num/2)-1, comp_num))
	
elif cluster_size == 2:
	#dummy functions for proper syntax into threading.Thread()
	def abc():
		pFactors.append(a.pFactorSearch(2,(comp_num/4)-1, comp_num))
		
	def ghi():
		pFactors.append(b.pFactorSearch((comp_num/4),(2*comp_num/4)-1, comp_num))
	############################################

	t1 = threading.Thread(name='thr1', target=abc)
	t2 = threading.Thread(name='thr2', target=ghi)
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()

elif cluster_size == 3:
	#dummy functions for proper syntax into threading.Thread()
	def abc():
		pFactors.append(a.pFactorSearch(2,(comp_num/6)-1, comp_num))
		
	def ghi():
		pFactors.append(b.pFactorSearch((comp_num/6),(2*comp_num/6)-1, comp_num))

	def jkl():
		pFactors.append(c.pFactorSearch((2*comp_num/6),(3*comp_num/6)-1, comp_num))	
	############################################

	t1 = threading.Thread(name='thr1', target=abc)
	t2 = threading.Thread(name='thr2', target=ghi)
	t3 = threading.Thread(name='thr3', target=jkl)
	
	t1.start()
	t2.start()
	t3.start()
	
	t1.join()
	t2.join()
	t3.join()
	
elif cluster_size == 4:
	#dummy functions for proper syntax into threading.Thread()
	def abc():
		pFactors.append(a.pFactorSearch(2,(comp_num/8)-1, comp_num))
		
	def ghi():
		pFactors.append(b.pFactorSearch((comp_num/8),(2*comp_num/8)-1, comp_num))

	def jkl():
		pFactors.append(c.pFactorSearch((2*comp_num/8),(3*comp_num/8)-1, comp_num))
		
	def mno():
		pFactors.append(d.pFactorSearch((3*comp_num/8),(4*comp_num/8)-1, comp_num))
		
	############################################

	t1 = threading.Thread(name='thr1', target=abc)
	t2 = threading.Thread(name='thr2', target=ghi)
	t3 = threading.Thread(name='thr3', target=jkl)
	t4 = threading.Thread(name='thr4', target=mno)

	t1.start()
	t2.start()
	t3.start()
	t4.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()

elif cluster_size == 5:

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
		
	############################################

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

else:
	print "Can only accept cluster size of 1 to 5"


runTime = time.time() - startTime




#########################################################################################     PART 3 


#cleaning up the pFactors list
#####################################################
pFactors =filter(None,pFactors) #remove empty parts from list
pFactors2 = str(pFactors)
a,b = pFactors2.split()
a = a.translate(None, '[],')
b = b.translate(None, '[],')
#########################################################


# from pylab import *

# pos = arange(3)+.5 

# barh(pos,(3,5,2), align='center', color='#b8ff5c')

# yticks(pos,('a','b','c'))

# xlabel('sdfdff')
# ylabel('sdfdf')

# title('esresr')
# grid(True)
# show()


import matplotlib
matplotlib.use( 'Agg' )
import pylab

pylab.plot([1,2,3])
pylab.savefig('img.png')


print "Factors: p = " + a + ".. q = " + b + " ||      Runtime: " + str(runTime)



