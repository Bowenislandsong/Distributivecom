from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from websocket import create_connection
import threading
import time
commands = 
clients = []
class SimpleChat(WebSocket):

	def handleMessage(self):
		for client in clients:
		#if client != self:
			
			client.sendMessage(self.address[0] + u' - ' + self.data)
			
		print(self.data)

	def handleConnected(self):
		print(self.address, 'connected')
		# for client in clients:

		# 	client.sendMessage(self.address[0] + u' - connected')
		clients.append(self)


	def handleClose(self):
		clients.remove(self)
		print(self.address, 'closed')
		# for client in clients:
		# 	client.sendMessage(self.address[0] + u' - disconnected')

def main():
	#threading.Thread(target=start_server,args=()).start
	server = SimpleWebSocketServer('', 8001, SimpleChat)
	server.serveforever()

def start_server():

	server = SimpleWebSocketServer('', 8001, SimpleChat)
	server.serveforever()


if __name__=="__main__":
	main()

