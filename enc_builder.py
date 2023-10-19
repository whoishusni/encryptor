from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from enc_attr import Encryption_Attributes

class Encryption_Builder:
    def __init__(self, secret_key):
        self.secret_key = secret_key
    
    def build_encryptor(self):
        enc_at = Encryption_Attributes()
        key = PBKDF2(self.secret_key,enc_at.get_salt(), dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC, iv=enc_at.get_iv())
        return cipher