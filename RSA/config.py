from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)

FORMAT = 'utf-8'
SIZE = 1024
PORT = 13000
HOST = 'localhost'

def encrypt_AES(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(
        iv), backend=default_backend()).encryptor()
    return (cipher.update(data) + cipher.finalize())

def decrypt_AES(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(
        iv), backend=default_backend()).decryptor()
    return cipher.update(data)
