import socket                                         
import time
import json
import time
import threading
import math
#Global vars
_PORT = 9999
_LISTEN_QUEUE_SIZE=100
nlist={} #node list
BUFFER_SIZE = 65536

def init_server():
	pass

# def reply(addr,reply_str, clientsocket):
# 	rdata={}
# 	rdata['ip']=addr
# 	rdata['time']=time.ctime(time.time())
# 	jsonData=json.dumps(rdata)
# 	clientsocket.send(reply_str.encode('ascii'))


def listen_thread():
	# create a socket object
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	# get local machine name / ip
	host = socket.gethostname()                           
	# bind to the port
	serversocket.bind((host, _PORT))                                  

	# queue up to 100 requests
	serversocket.listen(_LISTEN_QUEUE_SIZE)
                                    

	while True:
	    # establish a connection
	    clientsocket,addr = serversocket.accept()   

	    print("Got a connection from %s" % str(addr[0]))
	    reply_str = "Success" + "\r\n"
	    f = open('result.zip','wb')
	    l = clientsocket.recv(BUFFER_SIZE)
	    i = 0
	    while (l):
	    	f.write(l)
	    	i += 1
	    	print(i)
	    	l = clientsocket.recv(BUFFER_SIZE)
	    f.close()
	    # reply(addr,reply_str)
	    # f.write(l)
	    # reply(addr,reply_str, clientsocket)

	    clientsocket.close()
	
	# serversocket.close()

def main():
    t1 = threading.Thread(target=listen_thread)
    t1.start()
    t1.join()
    print("EXITING")

if __name__ == "__main__":
    main()