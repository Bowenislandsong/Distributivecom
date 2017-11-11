# client.py  

import os
import subprocess
from flask import Flask, render_template, request
import socket
import sys
import math
from cryptography.fernet import Fernet
BUFFER_SIZE = 65536

def encryption(message):
	message_b=bytes(message,encoding="utf8")#str to bytes
	key = Fernet.generate_key()
	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(message_b)
	return cipher_text,key

def send_message(encryptedMessage):
	# create a socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	# get local machine name / ip
	host = socket.gethostname()   
	# host = '155.41.92.21'                        

	port = 9999

	# connection to hostname on the port.
	s.connect((host, port))                               
	sendStr=str(encryptedMessage)
	s.send(sendStr.encode('ascii'))
	# Receive no more than 1024 bytes
	tm = s.recv(BUFFER_SIZE)                                     

	s.close()

	print("REPLY FROM SERVER: %s" % tm.decode('ascii'))

# flask initialization
project_root = os.path.dirname(__file__)
app = Flask(__name__, template_folder='/Users/xinli/Desktop/webUI/templates',
	static_folder = '/Users/xinli/Desktop/webUI/static')

@app.route('/')
def login(name=None):
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def authentication():
	name = str(request.form.get('txtuser'))
	password = str(request.form.get('txtpass'))
	combination = name + ' ' + password
	print(combination)
	encrypted_message, key_value = encryption(combination)
	print(encrypted_message)
	print(key_value)
	# create a socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	# get local machine name / ip
	host = socket.gethostname()   
	# host = '155.41.92.21'                        
	port = 9999
	# connection to hostname on the port.
	s.connect((host, port))                                                            
	f = open('test.zip','rb')
	i = 0
	l = f.read(BUFFER_SIZE)
	while (l):
		i += 1
		print(i)
		s.send(l)
		# Receive no more than 1024 bytes    
		l = f.read(BUFFER_SIZE)
	f.close()
	s.shutdown(socket.SHUT_WR)
	s.close()
	# send_file(l)
	if not name or not password:
		return render_template('failure.html')
	return render_template('button.html')

@app.route('/execute')
def hello(name=None):
	subprocess.call('python connect.py',shell=True)
	return render_template('execute.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	app.debug

