import pymongo
import bcrypt
from pymongo import MongoClient

client = MongoClient('mongodb://dishantp:newuser@ds257485.mlab.com:57485/distcomp')
db=client.distcomp

def auth(username, password):
	flag = False
	user = db.users.find_one({"name": username})
	if user:
		if bcrypt.hashpw(password.encode('utf-8'), user['password']) == user['password']:
			flag = True
		else:
			flag = False
	return flag

def main():
	username = "dishant"
	password = "123"
	exists = auth(username, password)
	print(exists)

if __name__ == "__main__":
    main()