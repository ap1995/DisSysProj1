
import socket   #for sockets
import sys      #to enable exit feature

#socket.socket(socket. Address Family, TYPE)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET- for IPv4, SOCK_STREAM used for TCP, for UDP use SOCK_DGRAM
    
except socket.error as msg:
    print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit();
 
print ('Socket Created')

host= 'www.google.com'

try:
    remote_ip= socket.gethostbyname( host )
except socket.gaierror:
    #could not resolve
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
print ('Ip address of ' + host + ' is ' + remote_ip) 

s.connect((remote_ip , 80))
 
print ('Socket Connected to ' + host + ' on ip ' + remote_ip)

message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(message.encode()) #send the message to server
except socket.error:
    #Send failed
    print ('Send failed')
    sys.exit()
 
print ('Message send successfully')
 
#Now receive data
reply = s.recv(4096) #recieve data from the socket.
 
print (reply)


