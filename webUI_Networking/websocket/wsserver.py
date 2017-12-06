from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
#from websocket import create_connection
import threading
import time
import pymongo
from pymongo import MongoClient
import bcrypt
clients = []
global counter
global have_job
counter = 0
client = MongoClient('mongodb://dishantp:newuser@ds257485.mlab.com:57485/distcomp')
db=client.distcomp

def findjobs():
    user = db.users.find_one({"Uploaded file":{"$size":4}})
    if user:
        files = user['Uploaded file']
        username = user['name']
        db.users.update({'name':username}, {"$unset": {'Uploaded file':""}})
        return files

def auth(username, password):
    flag = False
    user = db.users.find_one({"name": username})
    if user:
        if bcrypt.hashpw(password.encode('utf-8'), user['password']) == user['password']:
            flag = True
        else:
            flag = False
    return flag

def searchFiles():
    filelist = []
    listOfFiles = os.listdir()
    listOfFiles.sort()
    pattern = 'file*'
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            filelist.append(entry)
    return filelist

def authentication(data):
    mdata = data.split()
    name = mdata[0]
    password = mdata[1]
    if auth(name,password):
        return 'yes'
    else:
        return 'no'
    # if name == '123' and password == '456':
    #   return 'yes'
    # else :
    #   return 'no'


class SimpleChat(WebSocket):

    def handleMessage(self):
        global counter
        global have_job

        fileli = ['dishantp_Distribut0.zip','dishantp_Distribut1.zip','dishantp_Distribut2.zip']
        # if(have_job==0):
        #     fileli = findjobs()
        #     if(fileli!='None'):
        #         have_job=1
        #     else:
        #         have_job=0
        # print(fileli)
        msg = self.data
        if(msg!='file'):
            reply = authentication(msg)
        else:
            if len(fileli) > 0 and len(fileli) > counter:
                reply = fileli[counter]
                print(reply)
                counter = counter + 1
            # else:
            #     fileli = findjobs()
            #     counter=0
            #     if(fileli!='None'):
            #         have_job=1
            #     else:
            #         have_job=0
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
        #   client.sendMessage(self.address[0] + u' - disconnected')

def main():
#   threading.Thread(target=start_server,args=()).start
    global have_job
    have_job=0
    server = SimpleWebSocketServer('0.0.0.0', 9999, SimpleChat)
    server.serveforever()



if __name__=="__main__":
    main()