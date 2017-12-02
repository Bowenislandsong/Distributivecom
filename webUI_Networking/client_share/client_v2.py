# client.py

import os
import subprocess
from flask import Flask, render_template, request
import socket
import sys
from zipfile import *
import glob
import subprocess
from websocket import create_connection

BUFFER_SIZE = 65536
SOCKET_TIMEOUT = 15
# create a socket object
# get local machine name / ip
ADDRESS = "ws://localhost:8001/"

def join_swarm():
    pass

def leave_swarm():
    pass


def send_message(message, s):
    sendStr = str(message)
    s.send(sendStr.encode('ascii'))


def receive_message(s):
    data = s.recv()
    return data


# flask initialization
project_root = os.path.dirname(__file__)
app = Flask(
    __name__,
    template_folder='/home/hari/Workspace/Distributivecom/webUI_Networking/templates',
    static_folder='/home/hari/Workspace/Distributivecom/webUI_Networking/static')


def send_file(s):
    file = open('result.zip', 'rb')
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


def aquire_user_info():
    name = str(request.form.get('txtuser'))
    password = str(request.form.get('txtpass'))
    if not name or not password:
        return render_template('failure.html')
    total_info = name + ' ' + password
    return total_info


def init_connection(address):
    s = create_connection(address)
    s.settimeout(SOCKET_TIMEOUT)
    return s

def scan():
    while True:
        if(glob.glob('ml.py')):
            subprocess.call('docker build -t con .',shell = True)
            subprocess.call('docker run -it -v ~/Desktop/client_share:/client_share con' , shell = True)
            break

@app.route('/')
def login(name=None):
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def authentication():
    info = aquire_user_info()
    global s 
    s = create_connection(ADDRESS)
    s.settimeout(SOCKET_TIMEOUT)
    s.send(info)
    data = s.recv()
    #real_data = data[2:len(data) - 1]
    print(data)
    if data == 'yes':
        return render_template('button.html')
    else:
        return render_template('failure.html')

@app.route('/execute')
def hello(name=None):
    #   subprocess.call('python connect.py',shell=True)
    #s = init_connection(ADDRESS)
    global s
    send_message('file', s)
    data = s.recv()
    print(data)
    #receive_file(s)
    #s.close()
    #with ZipFile('received.zip', 'r') as zip:
    #    zip.extractall();
    #scan()
    #s = init_connection(host, port)
    #send_file(s)
    #s.close()
    return render_template('execute.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.debug