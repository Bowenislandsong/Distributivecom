import os
import subprocess


From = "/home/ubuntu/Final_website/home/ubuntu/Source/"
To =  "/var/ftp/pub/outgoing/"

listoftxt=os.listdir(From)

for x in listoftxt:
        ff = From+x
        subprocess.call('sudo mv '+ff+' '+To,shell=True)