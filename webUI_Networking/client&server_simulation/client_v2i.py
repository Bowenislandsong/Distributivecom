import os, fnmatch
import socket
import threading
from cryptography.fernet import Fernet
# Global vars
_PORT1 = 1111 
_PORT = 9999
_LISTEN_QUEUE_SIZE = 100
BUFFER_SIZE = 2000

# create a socket object
cosocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cosocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get local machine name / ip
host = socket.gethostname()
#host1 = '18.216.9.67'


def send_message(message, s):
    sendStr = str(message)
    s.send(sendStr.encode('ascii'))


def receive_message(s):
    data = s.recv(BUFFER_SIZE)
    return data

def send_file(s):
    file = open('received.zip', 'rb')
    file_seg = file.read(BUFFER_SIZE)
    while(file_seg):
        s.send(file_seg)
        file_seg = file.read(BUFFER_SIZE)
    file.close()


def receive_file(s):
    file_seg = s.recv(BUFFER_SIZE)
    if file_seg:
        file = open('received.zip', 'wb')
        while(file_seg):
            file.write(file_seg)
            file_seg = s.recv(BUFFER_SIZE)
        file.close()
    else:
        print('No file received.')
        s.close()



def init_connection(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s



def authentication(real_data, clientsocket):
    s = init_connection(host,_PORT1)
    send_message(real_data, s)
    data = str(receive_message(s))
    s.close()
    real_data = data[2:len(data) - 1]
    print(real_data)
    if real_data == 'yes':
        send_message('yes', clientsocket)
    else:
        send_message('no', clientsocket)


def hello():
    #   subprocess.call('python connect.py',shell=True)
    s = init_connection(host, _PORT1)
    send_message('file', s)
    receive_file(s)
    s.close()
    s = init_connection(host, _PORT1)
    send_file(s)
    s.close()


def execution(clientsocket):
    # initialize a counter for file transfer
    old_data = receive_message(clientsocket)
    data=str(old_data)
    real_data = data[2:len(data) - 1]
    print(real_data)
    if real_data == 'file':
        hello()
    else:
        authentication(real_data,clientsocket)
    clientsocket.close()


def listen_thread():
    # bind to the port
    cosocket.bind((host, _PORT))
    # queue up to 100 requests
    while True:
        cosocket.listen(_LISTEN_QUEUE_SIZE)
        while True:
            # establish a connection
            clientsocket, addr = cosocket.accept()
            execution(clientsocket)


def main():
    listen_thread()


if __name__ == "__main__":
    main()