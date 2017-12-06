from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
#from websocket import create_connection
import threading
import time
import pymongo
from pymongo import MongoClient
clients = []
global counter
counter = 0

client = MongoClient('mongodb://dishantp:newuser@ds257485.mlab.com:57485/distcomp')
db=client.distcomp

def findjobs():
	user = db.users.find_one({"Uploaded file":{"$size":4}})
	if user:
		files = user['Uploaded file']
		username = user['name']
		print(username)
		db.users.update({'name':username}, {"$unset": {'Uploaded file':""}})
		return files

def searchFiles():
	filelist = []
	listOfFiles = os.listdir()
	listOfFiles.sort()
	pattern = 'file*'
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			filelist.append(entry)
	print(filelist)
	return filelist

def authentication(data):
	mdata = data.split()
	name = mdata[0]
	password = mdata[1]
	if name == '123' and password == '456':
		return 'yes'
	else :
		return 'no'


class SimpleChat(WebSocket):

	def handleMessage(self):
		fileli = ['Distribut0.zip','Distribut1.zip','Distribut2.zip']
		msg = self.data
		if(msg!='file'):
			reply = authentication(msg)
		else:
			if len(fileli) > 0 and len(fileli) > counter:
				reply = fileli[counter]
				print(reply)
				counter = counter + 1

		for client in clients:
			if client == self:
				client.sendMessage(reply)

			
		print(self.data)

	def handleConnected(self):
		print(self.address, 'connected')
		for client in clients:
			if client == self:
			 	client.sendMessage(self.address[0] + u' - connected')
		clients.append(self)


	def handleClose(self):
		clients.remove(self)
		print(self.address, 'closed')
		# for client in clients:
		# 	client.sendMessage(self.address[0] + u' - disconnected')

def main():
#	threading.Thread(target=start_server,args=()).start

	server = SimpleWebSocketServer('0.0.0.0', 9999, SimpleChat)
	server.serveforever()



if __name__=="__main__":
	main()

