from socket import *
import socket
import config
import rsa
import os
import secrets

KEY = os.urandom(32)
IV = secrets.token_bytes(16)

public_key, private_key = rsa.newkeys(512)

clientSocket = socket.socket(AF_INET, SOCK_STREAM)
clientSocket.connect((config.HOST, config.PORT))

SERVER_KEY = clientSocket.recv(config.SIZE)
PUBLIC_SERVER_KEY = rsa.PublicKey.load_pkcs1(SERVER_KEY)
encryptedMessage = rsa.encrypt(KEY, PUBLIC_SERVER_KEY)
clientSocket.send(encryptedMessage)
encryptedMessage = rsa.encrypt(IV, PUBLIC_SERVER_KEY)
clientSocket.send(encryptedMessage)
messageReceived = clientSocket.recv(config.SIZE).decode(config.FORMAT)
if messageReceived == 'AUTHENTICATED':
    print(f'Connection started.\n')
    while True:
        message = input("Enter a message (Type 'exit' to finish): ")
        original_message = message

        while len(message) % 16 != 0:
            message += " "
        try:
            encryptedMessage = config.encrypt_AES(message.encode(), KEY, IV)
        except ValueError:
            print("An error has occurred. Connection terminated.")
            message = 'ERROR'
            while len(message) % 16 != 0:
                message += " "
            clientSocket.send(config.encrypt_AES(message.encode(), KEY, IV))
            break
        else:
            clientSocket.send(encryptedMessage)
            if original_message.lower() == 'exit':
                break
    print('\nConnection closed.')
    clientSocket.close()
