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

def aquire_user_info():
	name = str(request.form.get('txtuser'))
	password = str(request.form.get('txtpass'))
	if not name or not password:
		return render_template('failure.html')
	# encrypted_message_name, key_value_name = encryption(name)
	# encrypted_message_pw, key_value_pw = encryption(password)
	# message_to_send_name= '$'+str(encrypted_message_name) + ' ' + str(key_value_name)
	# message_to_send_pw= '?'+str(encrypted_message_pw) + ' ' + str(key_value_pw)
	return name,password

def init_connection(host,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s

@app.route('/')
def login(name=None):
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def authentication():
	(name,pw)=aquire_user_info()
	s=init_connection(host,port)
	send_message(name,s)
	s.close()
	s=init_connection(host,port)
	send_message(pw,s)
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

