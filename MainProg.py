import config

c1 = config.client1
c2 = config.client2
c3 = config.client3
c4 = config.client4

# Make all connections, will be added to config file later
c1.startServer
c2.startServer
c1.startClient(c2.port)
c2.startClient(c1.port)
