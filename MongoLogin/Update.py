import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/distcomp')
db=client.distcomp
def updateDB(username,ip,port,types,start_time,isAlive,file_path):
	client = MongoClient('mongodb://localhost:27017/distcomp')
	db=client.distcomp
	db.users.update({"name":username},{"$set":{"IPAddress":ip,"Port":port,"NodeType":types,"StartTime":start_time}}) 
	#return None

def main():
	username="dishant"
	ip="IPv6"
	port="5000"
	types="Manager"
	start_time="Time"
	isAlive="Yes"
	file_path="SomePath"
	updateDB(username,ip,port,types,start_time,isAlive,file_path)

if __name__ == "__main__":
    main()

