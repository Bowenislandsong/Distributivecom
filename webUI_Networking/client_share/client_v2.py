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
from ftplib import FTP
from zipfile import *

BUFFER_SIZE = 65536
SOCKET_TIMEOUT = 15

ADDRESS = "ws://localhost:8001/"

def uploadFile(filename):
    ftp = FTP('18.216.9.67')     # connect to host, default port
    print(ftp.login())
    print(ftp.cwd('/incoming/uploading/'))
    ftp.set_pasv(False)
    print(ftp.retrlines('LIST'))
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

def downloadFile(filename):
    ftp = FTP('18.216.9.67')     # connect to host, default port
    print(ftp.login())
    print(ftp.cwd('/outgoing/'))
    ftp.set_pasv(False)
    files = []
    ftp.retrlines('LIST',files.append)
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()
    ftp.quit()


def send_message(message, s):
    sendStr = str(message)
    s.send(sendStr.encode('ascii'))


def receive_message(s):
    data = s.recv()
    return data


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
    prevList = os.listdir()
    path=os.getcwd()
    cmd = 'docker run -it -v ' +path +':client_share con'
    
    while True:
        if(glob.glob('ml.py')):
            p1=subprocess.Popen(['docker'],['build'],['-t'],['con .'])
            p1.wait()
            p2=subprocess.Popen(cmd)
            p2.wait()
            break
    currList = os.listdir()
    diffList = list(set(currList).symmetric_difference(set(prevList)))
    zip_archive = ZipFile( "result_"+data,"w",ZIP_DEFLATED)
    for filename in diffList:
        zip_archive.write(filename)
    zip_archive.close()
    return "result_"+data

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
    print(data)
    if data == 'yes':
        return render_template('button.html')
    else:
        return render_template('failure.html')

@app.route('/execute')
def hello(name=None):
    global s
    send_message('file', s)
    data = s.recv()
    print(data)
    downloadFile(data)
    with ZipFile(data, 'r') as zip:
        zip.extractall();
    resultfile = scan(data)
    uploadFile(resultfile)
    send_message(resultfile,s)
    return render_template('execute.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.debug