from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import time
import pyfiglet

salt = b'\x8e\xbf\xa4\xaa$\x8f9\x8eH\x9a\x1a~\xbd\\\x9f^g"\xe0UGV\x0b\x17\x0b\x8c\x04F\x85\x01\xbe\x10'
init_vector = b'q\xbd~{E\xca\xca\x1c\xf9\x89&]\xad0\xc8\xf0'

def generate_key():
    print('16 bytes : {}'.format(get_random_bytes(16)))
    print('32 bytes : {}'.format(get_random_bytes(32)))

def banner():
    banner_view = pyfiglet.figlet_format('Encryptor', font='cybermedium')
    return print(banner_view)
    
def encrypt_file(file_path, secret_key):
    try:
        key = PBKDF2(secret_key, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC, iv=init_vector)
        
        with open(file_path,'rb') as open_file:
            origin_file = open_file.read()
            encrypting_file = cipher.encrypt(pad(origin_file, AES.block_size))
            open_file.close()
        
        with open(file_path, 'wb') as write_file:
            write_file.write(encrypting_file)
            write_file.close()
    except:
        print('Terjadi Kesalahan Pada Proses Encrypt File')
        return main()
    
def decrypt_file(file_path, secret_key):
    try:
        key = PBKDF2(secret_key, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC, iv=init_vector)
        
        with open(file_path,'rb') as open_file:
            origin_file = open_file.read()
            decrypting_file = unpad(cipher.decrypt(origin_file),AES.block_size)
            open_file.close()
        
        with open(file_path, 'wb') as write_file:
            write_file.write(decrypting_file)
            write_file.close()
    except:
        print('Terjadi Kesalahan Pada Proses Decrypt File (Kemungkinan Salah Secret Key)')
        return main()

def main():
    banner()
    print('version : v1.0')
    print('author  : MHM\n')
    print(' MENU '.center(50,'='))
    print('1. Encrypt - Mengubah Text Biasa Ke Cipher Text')
    print('2. Decrypt - Mengubah Cipher Text ke Text Biasa')
    print('\n')
    menu_choice = input('Pilih Menu [1/2] ? ')
    
    if menu_choice == '1':
        print(' Encrypt '.center(50,'-'))
        file_path = input('Masukkan Lokasi File atau Nama File = ')
        if os.path.exists(file_path):    
            secret_key = input('Masukkan Secret Key = ')
            encrypt_file(file_path, secret_key)
        else:
            print('Tidak Ada File Dengan Nama {}\nKembali Ke Menu Utama...'.format(file_path))
            time.sleep(2)
            os.system('cls')
            return main()
        
    elif menu_choice == '2':
        print(' Decrypt '.center(50,'-'))
        file_path = input('Masukkan Lokasi File atau Nama File = ')
        if os.path.exists(file_path):    
            secret_key = input('Masukkan Secret Key = ')
            decrypt_file(file_path, secret_key)
        else:
            print('Tidak Ada File Dengan Nama {}\nKembali Ke Menu Utama...'.format(file_path))
            time.sleep(2)
            os.system('cls')
            return main()
            
    else:
        print('Tidak Ada Menu Yang Dipilih')
        print('Kembali Ke Menu Utama dalam 3 detik...')
        time.sleep(3)
        os.system('cls')
        return main()

if __name__ == '__main__':
    main()
    #generate_key()