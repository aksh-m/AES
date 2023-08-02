from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import fingerprintnormalization
import fingerprinthash

def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    with open(input_file, 'rb') as file:
        plaintext = file.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(output_file, 'wb') as file:
        file.write(iv + ciphertext)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        ciphertext = file.read()
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(output_file, 'wb') as file:
        file.write(plaintext)


key = finger123.key1  # 16 bytes


print('1. Encryption')
print('2. Decryption')

choice=int(input())
if choice==1:

    print('Enter file name to encrypt:')
    input_file = input()
    print('Enter file name for encrypted file:')
    encrypted_file=input()
    encrypt_file(input_file, encrypted_file, key)
    print("File encrypted successfully.")
if choice==2:
    print('Enter file name to decrypt:')
    encrypted_file= input()
    print('Enter file name for decrypted file:')
    decrypted_file = input()
    decrypt_file(encrypted_file, decrypted_file, key)
    print("File decrypted successfully.")
