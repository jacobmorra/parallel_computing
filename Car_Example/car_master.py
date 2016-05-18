import Pyro4

#Create a proxy object for each defined remote car object
proxy_car1 = Pyro4.Proxy("PYRONAME:car1")    
proxy_car2 = Pyro4.Proxy("PYRONAME:car2")    

#Call remote object methods for each defined object
print(proxy_car1.honk())
print(proxy_car2.honk())


