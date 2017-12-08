import os, fnmatch
import socket
import threading
import queue
import time
from cryptography.fernet import Fernet
# Global vars
_PORT = 9999
_LISTEN_QUEUE_SIZE = 100
BUFFER_SIZE = 65536
q = queue.Queue()
p = queue.Queue()
q.put(0)
p.put(0)
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# get local machine name / ip
host = socket.gethostname()
#FILEPATH = '/Users/yangzhiyi/Desktop/webUI_1/simulation'


def decryption(encrypted_msg, key):
    cipher_suite = Fernet(key)
    decry_msg = cipher_suite.decrypt(encrypted_msg)
    decry_msg = str(decry_msg, encoding="utf-8")
    return decry_msg

def send_file(clientsocket,q,filelist):
    # print(filelist)
    # print('test')
    # if not q.empty():
    counter = q.get()

    # print(counter)
    if len(filelist) > 0 and len(filelist) > counter:
        filename = filelist[counter]
        file = open(filename, 'rb')
        file_seg = file.read(BUFFER_SIZE)
        while(file_seg):
            clientsocket.send(file_seg)
            file_seg = file.read(BUFFER_SIZE)
        file.close()
        counter = counter + 1
        q.put(counter)
    else:
        print('No such file')
        q.put(counter)



def receive_file(clientsocket):
    file = open('file1.zip', 'wb')
    file_seg = clientsocket.recv(BUFFER_SIZE)
    while(file_seg):
        file.write(file_seg)
        file_seg = clientsocket.recv(BUFFER_SIZE)
    file.close()


def send_message(message, clientsocket):
    sendStr = str(message)
    clientsocket.send(sendStr.encode('ascii'))


def receive_message(clientsocket):
    data = clientsocket.recv(BUFFER_SIZE)
    return data


def split_data(data):
    real_data = data[1:len(data)]
    d_split = real_data.split()
    content = d_split[0]
    key = d_split[1]
    content = bytes(content, encoding="utf8")
    key = bytes(key, encoding="utf8")
    return content, key


def execution(clientsocket,q,filelist,p):
    # initialize a counter for file transfer
    old_data = receive_message(clientsocket)
    data=str(old_data)
    print(str(data[2:4]))
    try:
        real_data = data[2:len(data) - 1]
        if real_data == 'file':
            print(real_data)
            send_file(clientsocket,q,filelist)
        elif (str(data[2:4]) == 'PK'):
            print('111111111111')
            cout = p.get()
            fname = 'result_server' + str(cout) + '.zip'
            file = open(fname, 'wb')
            file.write(old_data)
            file.close()
            cout = cout + 1
            p.put(cout)
        else:
            mdata = real_data.split()
            name = mdata[0]
            password = mdata[1]
            if name == '123' and password == '456':
                time.sleep(10)
                send_message('yes', clientsocket)
    except:
        print('different os may cause the error')

    clientsocket.close()
    return 0


def listen_thread():
    filelist = []
    listOfFiles = os.listdir()
    listOfFiles.sort()
    pattern = 'file*'
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            filelist.append(entry)
    print(filelist)
    # bind to the port
    serversocket.bind((host, _PORT))
    # queue up to 100 requests
    while True:
        serversocket.listen(_LISTEN_QUEUE_SIZE)
        while True:
            # establish a connection
            clientsocket, addr = serversocket.accept()
            threading.Thread(target=execution, args=(clientsocket,q,filelist,p)).start()


def main():
    listen_thread()


if __name__ == "__main__":
    main()
