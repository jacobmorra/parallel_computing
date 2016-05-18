import Pyro4

#this class has a honk method for printing a unique message
class MyCar:
    def __init__(self):
	pass
    def honk(self):
        return "HONK!!! HONK!!!"

car1 = MyCar()                         #create a new MyCar instance

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(car1)            # register the greeting maker as a Pyro object
ns.register("car1", uri)               # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
