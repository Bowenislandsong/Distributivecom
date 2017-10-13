#Send back to user (know when task is done)(M->client)Cloud

# -Check if all the result is back from slave 
# -Discard impossible task and log it
# -Present brief report
# -Log with detail
# -Zip the result

# check if client conputer is online
# no - email notifying client open up consel to manually downlaod 
# yes - send it back

import os 
import socket
import sys
import logging
from thread import *


dir_path = os.path.dirname(os.path.realpath(__file__))
#cwd = os.getcwd() # get the path of current fodler



os.system("scp foo.bar joe@srvr.net:/path/to/foo.bar")



HOST = ''   
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Receving Data...\n') 

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = 'Message Received at the server!\n'
        print data
        if not data:
            break

        conn.sendall(reply)

    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread
    start_new_thread(clientthread ,(conn,))

s.close()
