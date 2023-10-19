from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import os
import time
from enc_builder import Encryption_Builder
from enc_banner import create_banner
    
def encrypt_file(file_path, encryption_builder):
    try:
        cipher = encryption_builder.build_encryptor()        
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

def decrypt_file(file_path, encryption_builder):
    try:
        cipher = encryption_builder.build_encryptor()        
        with open(file_path,'rb') as open_file:
            origin_file = open_file.read()
            decrypting_file = unpad(cipher.decrypt(origin_file),AES.block_size)
            open_file.close()
        
        with open(file_path, 'wb') as write_file:
            write_file.write(decrypting_file)
            write_file.close()
    except:
        print('Terjadi Kesalahan Pada Proses Encrypt File')
        return main()

def main():
    banner = create_banner()
    print(banner)
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
            enc_builder_var = Encryption_Builder(secret_key)
            encrypt_file(file_path,enc_builder_var)
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
            enc_builder_var = Encryption_Builder(secret_key)
            decrypt_file(file_path, enc_builder_var)
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