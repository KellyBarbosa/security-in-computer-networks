from socket import *
import config

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((config.HOST,config.PORT))
serverSocket.listen()

print(f"[LISTENING] Server is listening on {config.HOST}:{config.PORT}")

while True:
    conn, addr = serverSocket.accept()
    print("\n[+][NEW CONNECTION] The client is connected now.")
    message = conn.recv(config.SIZE)
    print(f"Message received: {message}")
    print(f"Message decrypted: {config.decrypt(message).decode()}")
    conn.send(("Message received and successfully decoded!").encode(config.FORMAT))
    conn.close()