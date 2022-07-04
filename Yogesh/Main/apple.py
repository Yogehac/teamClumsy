import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def security(msg):
    bytemsg=msg.encode()
    return bytemsg

def saltkey(key):
    salt = os.urandom(16)
    salt = b'salt_' 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )
    key = base64.urlsafe_b64encode(kdf.derive(security(key)))
    return key

def encryptdata(msg, key):
	f = Fernet(saltkey(key))
	encrypted = f.encrypt(security(msg))
	return encrypted
	
def decryptdata(hash, key):
	f=Fernet(saltkey(key))
	decrypt=f.decrypt(security(hash))
	decrypted=decrypt.decode()
	return decrypted



