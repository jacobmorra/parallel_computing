#Vanilla Factoring vs. Factoring with Lescisin's API

##Vanilla Factoring

####Associated Files: vanilla_master1.py, vanilla_slave1.py, vanilla_slave2.py

Prime Factors are found for the purpose of finding keys p and q (such that p*q=n) for the RSA Algorithm.

Python Remote Objects (Pyro4) is used to divide tasks in parallel among a Pi Cluster. See [Pyro4](https://pythonhosted.org/Pyro4/)

##Factoring with Lescisin's API

####Associated Files: factoring_master1.py, factoring_slave1.py, factoring_slave2.py

The same task is accomplished using pre-defined remote object methods with minimal overhead (in testing, a 5-10% run time overhead was observed).

####Runtime Environment
*Raspbian Jessie v4.4
*Pyro4 v4.45
