from socket import *
import socket
import config

clientSocket = socket.socket(AF_INET, SOCK_STREAM)
clientSocket.connect((config.HOST,config.PORT))

message = input("Enter a message: ")

while len(message)%16 != 0:
     message += " "

encryptedMessage = config.encrypt(message.encode())
print(f'The encrypted message is: {encryptedMessage}')
clientSocket.send(encryptedMessage)
messageReceived = clientSocket.recv(config.SIZE).decode(config.FORMAT)

print (f"Server response: {messageReceived}")

clientSocket.close()