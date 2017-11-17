import socket
import threading
from cryptography.fernet import Fernet
# Global vars
_PORT = 9999
_LISTEN_QUEUE_SIZE = 100
BUFFER_SIZE = 2000


# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# get local machine name / ip
host = socket.gethostname()


def decryption(encrypted_msg, key):
    cipher_suite = Fernet(key)
    decry_msg = cipher_suite.decrypt(encrypted_msg)
    decry_msg = str(decry_msg, encoding="utf-8")
    return decry_msg


def send_file(clientsocket):
    file = open('file.zip', 'rb')
    file_seg = file.read(BUFFER_SIZE)
    while(file_seg):
        clientsocket.send(file_seg)
        file_seg = file.read(BUFFER_SIZE)
    file.close()


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


def execution(clientsocket):
    data = str(receive_message(clientsocket))
    real_data = data[2:len(data) - 1]
    if real_data == 'file':
        send_file(clientsocket)

    else:
        mdata = real_data.split()
        name = mdata[0]
        password = mdata[1]
        if name == '123' and password == '456':
            send_message('yes', clientsocket)

    clientsocket.close()


def listen_thread():
    # bind to the port
    serversocket.bind((host, _PORT))
    # queue up to 100 requests
    while True:
        serversocket.listen(_LISTEN_QUEUE_SIZE)
        while True:
            # establish a connection
            clientsocket, addr = serversocket.accept()
            threading.Thread(target=execution, args=(clientsocket,)).start()


def main():
    listen_thread()


if __name__ == "__main__":
    main()
