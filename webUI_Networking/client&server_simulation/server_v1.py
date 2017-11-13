import socket                                         

#Global vars
_PORT = 9999
_LISTEN_QUEUE_SIZE=100
nlist={} #node list
BUFFER_SIZE = 2000

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# get local machine name / ip
host = socket.gethostname()


def send_file(clientsocket):
	file=open('file.zip','rb')
	file_seg=file.read(BUFFER_SIZE)
	while(file_seg):
		clientsocket.send(file_seg)
		file_seg=file.read(BUFFER_SIZE)
	file.close()


def receive_file(clientsocket):
	file=open('file1.zip','wb')
	file_seg=clientsocket.recv(BUFFER_SIZE)
	while(file_seg):
		file.write(file_seg)
		file_seg=clientsocket.recv(BUFFER_SIZE)
	file.close()	

def receive_message(clientsocket):
	data=clientsocket.recv(BUFFER_SIZE)
	return data

def listen_thread():                          
	# bind to the port
	serversocket.bind((host, _PORT))                                  
	# queue up to 100 requests
	serversocket.listen(_LISTEN_QUEUE_SIZE)
                                    
	while True:
	    # establish a connection
	    clientsocket,addr = serversocket.accept()
	    data=receive_message(clientsocket)
	    print(data)
	    if data=='1':
	    	send_file(clientsocket)

	    clientsocket.close()
	

def main():
	listen_thread()

if __name__ == "__main__":
    main()