import socket                                         
import time
import json
import time
import threading
#Global vars
_PORT = 9999
_LISTEN_QUEUE_SIZE=100
nlist={} #node list
BUFFER_SIZE = 1024

def init_server():
	pass


def listen_thread():
	# create a socket object
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	# get local machine name / ip
	host = socket.gethostname()                           
	# bind to the port
	serversocket.bind((host, _PORT))                                  

	# queue up to 100 requests
	serversocket.listen(_LISTEN_QUEUE_SIZE)

	#encrypted_message = serversocket.recv(BUFFER_SIZE)

	# print(encrypted_message)                                         

	while True:
	    # establish a connection
	    clientsocket,addr = serversocket.accept()      

	    print("Got a connection from %s" % str(addr[0]))
	    reply_str = "Success" + "\r\n"
	    rdata={}
	    rdata['ip']=addr
	    rdata['time']=time.ctime(time.time())
	    jsonData=json.dumps(rdata)
	    clientsocket.send(reply_str.encode('ascii'))
	    clientsocket.close()

def main():
    t1 = threading.Thread(target=listen_thread)
    t1.start()
    t1.join()
    print("EXITING")

if __name__ == "__main__":
    main()