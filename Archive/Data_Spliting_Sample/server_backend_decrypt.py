from cryptography.fernet import Fernet
import client_sim


user1=['yzy123@bu.edu','123456']

mess='yzy123@bu.edu 123456'
def decryp(cipher_text,key):
	cipher_suite = Fernet(key)
	plain_text = cipher_suite.decrypt(cipher_text)
	return plain_text

(cipher_text,key)=client_sim.encryp(mess)
plain_text=decryp(cipher_text,key)
plain_text=str(plain_text,encoding="utf-8")
print(plain_text)
inf=plain_text.split()
print(inf)
if inf[0]==user1[0]:
	if inf[1]==user1[1]:
		print('pass')
	else:
		print('not pass')
else:
	print('not pass')