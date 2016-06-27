from mpi4py import MPI
import logging
import sys

comm = MPI.COMM_WORLD
name=MPI.Get_processor_name()
#print("hello world")
#print(("name:",name,"my rank is",comm.rank))

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
    logging.debug('Exiting')		
    return pFactors

pFactors = []
comp_num = int(sys.argv[1])

if (comm.rank==0):
	pFactors.append(pFactorSearch(2,(comp_num/10)-1, comp_num))
elif (comm.rank==1):
#	print "rank 1"
	pFactors.append(pFactorSearch((comp_num/10),(2*comp_num/10)-1, comp_num))
elif (comm.rank==1):
#	print "rank 2"
	pFactors.append(pFactorSearch((2*comp_num/10),(3*comp_num/10)-1, comp_num))
elif (comm.rank==1):
#	print "rank 3"
	pFactors.append(pFactorSearch((3*comp_num/10),(4*comp_num/10)-1, comp_num))
else:
#	print "rank 4"
	pFactors.append(pFactorSearch((4*comp_num/10),(5*comp_num/10)-1, comp_num))

print "#######################################################################################"	
print comm.rank
print pFactors
print "#######################################################################################"	
