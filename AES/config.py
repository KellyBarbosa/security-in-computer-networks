from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)

FORMAT = 'utf-8'
SIZE = 1024
PORT = 13000
HOST = 'localhost'
KEY = b'key must be 128.'
IV = b"\x8a'\xd8\xf59]\x157S[X\xc0t\xcb\xa2\xc8"

def encrypt(data):
    cipher = Cipher(algorithms.AES(KEY),modes.CBC(IV),backend=default_backend()).encryptor()
    return (cipher.update(data) + cipher.finalize())

def decrypt(data):
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend()).decryptor()
    return cipher.update(data)