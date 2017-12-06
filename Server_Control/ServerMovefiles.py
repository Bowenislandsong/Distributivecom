import os
import subprocess

currentpath  = os.getcwd()
From = "/home/ubuntu/Final_website/home/ubuntu/Source/"
To = currentpath + "/outgoing/"

listoftxt=os.listdir(From)

for x in listoftxt:
        ff = From+x
        subprocess.call('sudo mv '+ff+' '+To,shell=True)