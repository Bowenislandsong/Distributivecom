# client.py  

import os
import subprocess
from flask import Flask, render_template, request
import socket
import sys
from cryptography.fernet import Fernet

BUFFER_SIZE = 1024
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name / ip
host = socket.gethostname()
port = 9999 

def encryption(message):
	message_b=bytes(message,encoding="utf8")#str to bytes
	key = Fernet.generate_key()
	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(message_b)
	return cipher_text,key

def send_message(encryptedMessage,s):                              
	sendStr=str(encryptedMessage)
	s.send(sendStr.encode('ascii'))


# flask initialization
project_root = os.path.dirname(__file__)
app = Flask(__name__, template_folder='/Users/yangzhiyi/Desktop/webUI_1/templates',
	static_folder = '/Users/yangzhiyi/Desktop/webUI_1/static')

def send_file(s):
	file=open('file.zip','rb')
	file_seg=file.read(BUFFER_SIZE)
	while(file_seg):
		s.send(file_seg)
		file_seg=file.read(BUFFER_SIZE)
	file.close()

def receive_file(s):
	file=open('file1.zip','wb')
	file_seg=s.recv(BUFFER_SIZE)
	while(file_seg):
		file.write(file_seg)
		file_seg=s.recv(BUFFER_SIZE)
	file.close()


@app.route('/')
def login(name=None):
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def authentication():
	s.connect((host, port))
	message = '1'
	send_message(message,s)
	receive_file(s)
	s.close()
	return render_template('button.html')

@app.route('/execute')
def hello(name=None):
	subprocess.call('python connect.py',shell=True)
	return render_template('execute.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	app.debug

