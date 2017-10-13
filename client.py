# client.py  
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name / ip
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               
sendStr="Ping\r\n"
s.send(sendStr.encode('ascii'))
# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

s.close()

print("REPLY FROM SERVER: %s" % tm.decode('ascii'))

 
