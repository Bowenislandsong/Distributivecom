# client.py

import os
import subprocess
from flask import Flask, render_template, request
import socket
import sys
from cryptography.fernet import Fernet

BUFFER_SIZE = 1024
# create a socket object
# get local machine name / ip
host = socket.gethostname()
port = 9999


def encryption(message):
    message_b = bytes(message, encoding="utf8")  # str to bytes
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(message_b)
    return cipher_text, key


def send_message(message, s):
    sendStr = str(message)
    s.send(sendStr.encode('ascii'))


def receive_message(s):
    data = s.recv(BUFFER_SIZE)
    return data


# flask initialization
project_root = os.path.dirname(__file__)
app = Flask(
    __name__,
    template_folder='/Users/yangzhiyi/Desktop/webUI_1/templates',
    static_folder='/Users/yangzhiyi/Desktop/webUI_1/static')


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


def aquire_user_info():
    name = str(request.form.get('txtuser'))
    password = str(request.form.get('txtpass'))
    if not name or not password:
        return render_template('failure.html')
    total_info = name + ' ' + password
    return total_info


def init_connection(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


@app.route('/')
def login(name=None):
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def authentication():
    info = aquire_user_info()
    s = init_connection(host, port)
    send_message(info, s)
    data = str(receive_message(s))
    s.close()
    real_data = data[2:len(data) - 1]
    if real_data == 'yes':
        return render_template('button.html')
    else:
        return render_template('failure.html')


@app.route('/execute')
def hello(name=None):
    #   subprocess.call('python connect.py',shell=True)
    s = init_connection(host, port)
    send_message('file', s)
    receive_file(s)
    s.close()
    s = init_connection(host, port)
    send_file(s)
    s.close()
    return render_template('execute.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.debug
