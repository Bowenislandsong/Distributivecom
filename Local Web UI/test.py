#import subprocess

import urllib.error
import urllib.request

def internet_on():
    try:
        urllib.request.urlopen('https://www.facebook.com', timeout=1)
        return True
    except urllib.error.URLError as err: 
    	return False

if __name__ == '__main__':
	if(internet_on()==True):
		print('on')
	else:
		print('off')

#subprocess.call('python hello.py', shell=True)

import socket
REMOTE_SERVER = "www.google.com"
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
print(is_connected())