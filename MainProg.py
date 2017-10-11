import config

c1 = config.client1
c2 = config.client2
c3 = config.client3
c4 = config.client4

# client1 = client.Client()
# client1.hostname = 'Ash'
# client1.port = 12345
# client1.processID =1
#
# client2 = client.Client()
# client2.hostname = 'Pooja'
# client2.port = 56789
# client2.processID =2

c1.connection(c2)
# c2.connection(c1)
