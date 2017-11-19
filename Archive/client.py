# client.py  
import socket
import time
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
tm = s.recv(100)                                     
#time.sleep(2)
#tm1 = s.recv(6)
s.close()

print("REPLY FROM SERVER: %s %s", tm.decode('ascii') )

 
