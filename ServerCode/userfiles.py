import pymongo
from pymongo import MongoClient

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

def main():
	filenames = findjobs()
	print(filenames)

if __name__ == "__main__":
    main()