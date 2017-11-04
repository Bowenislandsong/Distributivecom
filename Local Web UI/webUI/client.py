# client.py  

import os
import subprocess
from flask import Flask, render_template, request
import socket
from cryptography.fernet import Fernet

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

	port = 9999

	# connection to hostname on the port.
	s.connect((host, port))                               
	sendStr=str(encryptedMessage)
	s.send(sendStr.encode('ascii'))
	# Receive no more than 1024 bytes
	tm = s.recv(1024)                                     

	s.close()

	print("REPLY FROM SERVER: %s" % tm.decode('ascii'))

# flask initialization
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '/Users/xinli/Desktop/webUI')
app = Flask(__name__, template_folder='/Users/xinli/Desktop/webUI/templates',
	static_folder = '/Users/xinli/Desktop/webUI/static')

@app.route('/')
def index(name=None):
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	name = str(request.form.get('name'))
	password = str(request.form.get('password'))
	combination = name + ' ' + password
	print(combination)
	encrypted_message, key_value = encryption(combination)
	print(encrypted_message)
	print(key_value)
	if not name or not password:
		return render_template('failure.html')
	message_to_send = str(encrypted_message) + '__' + str(key_value)
	send_message(message_to_send)
	return render_template('button.html')

@app.route('/execute')
def hello(name=None):
	subprocess.call('python connect.py',shell=True)
	return render_template('execute.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	app.debug



 
