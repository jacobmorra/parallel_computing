import Pyro4

#this class has a honk method for printing a unique message
class MyCar:
    def __init__(self):
	pass
    def honk(self):
        return "HONK!!! HONK!!!"

car2 = MyCar()                         #create a new MyCar instance

daemon = Pyro4.Daemon("10.124.7.73")   # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(car2)            # register the greeting maker as a Pyro object
ns.register("car2", uri)               # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
