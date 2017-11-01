import os
import subprocess
from flask import Flask, render_template, request
from cryptography.fernet import Fernet

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '/Users/xinli/Desktop/webUI')
app = Flask(__name__, template_folder='/Users/xinli/Desktop/webUI/templates',
	static_folder = '/Users/xinli/Desktop/webUI/static')

def encryp(message):
	message_b=bytes(message,encoding="utf8")#str to bytes
	key = Fernet.generate_key()
	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(message_b)
	return cipher_text,key

@app.route('/')
def index(name=None):
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	name = request.form.get('name')
	password = request.form.get('password')
	combination = name + ' ' + password
	print(combination)
	encrypted_message, key_value = encryp(combination)
	print(encrypted_message)
	print(key_value)
	if not name or not password:
		return render_template('failure.html')
	return render_template('button.html')


@app.route('/execute')
def execute():
	subprocess.call('python connect.py',shell=True)
	print("done")
	return render_template('execute.html')

# @app.route('/register', methods=['POST'])
# def register():
# 	name = request.form.get('name')
# 	password = request.form.get('password')
# 	if not name or not password:
# 		return render_template('failure.html')
# 	return render_template('login.html')



if __name__ == '__main__':
	app.run(host='0.0.0.0')
	app.debug
