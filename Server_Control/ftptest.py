from ftplib import FTP
#import ftplib

def uploadFile():
	ftp = FTP('18.216.9.67')     # connect to host, default port
	print(ftp.login())
	print(ftp.cwd('/incoming/uploading/'))
	ftp.set_pasv(False)
	print(ftp.retrlines('LIST'))
	filename = 'downloadthis.zip' #replace with your file in your home folder
	ftp.storbinary('STOR '+filename, open(filename, 'rb'))
	ftp.quit()

def downloadFile():
	ftp = FTP('18.216.9.67')     # connect to host, default port
	print(ftp.login())
	print(ftp.cwd('/outgoing/'))
	ftp.set_pasv(False)
	files = []
	ftp.retrlines('LIST',files.append)
	for filename in files:
		filename=filename.split(' ')[-1]
		localfile = open(filename, 'wb')
		ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
		localfile.close()
		pass
	#filename = 'test.txt' #replace with your file in the directory ('directory_name')
	ftp.quit()


downloadFile()

uploadFile()




# filename = 'test.txt' #replace with your file in the directory ('directory_name')
# localfile = open(filename, 'wb')

# ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
# ftp.quit()
# localfile.close()






 # 1123  sudo nano /etc/vsftpd.conf
 # 1124  sudo systemctl restart vsftpd
 # 1125  sudo ufw allow ftp-data
 # 1126  sudo ufw allow ftp
 # 1127  sudo ufw status
 # 1128  sudo mkdir -p /var/ftp/pub
 # 1129  sudo chown nobody:nogroup /var/ftp/pub
 # 1130  touch /var/ftp/pub
 # 1131  touch /var/ftp/pub/ftptest.txt
 # 1132  echo "vsftpd test file" | sudo tee /var/ftp/pub/test.txt

