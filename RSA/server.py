from socket import *
import config
import rsa

public_key, private_key = rsa.newkeys(512)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((config.HOST, config.PORT))
serverSocket.listen()

print(f"[LISTENING] Server is listening on {config.HOST}:{config.PORT}")

while True:
    conn, addr = serverSocket.accept()
    conn.send(public_key.save_pkcs1())
    KEY = rsa.decrypt(conn.recv(config.SIZE), private_key)
    IV = rsa.decrypt(conn.recv(config.SIZE), private_key)
    conn.send(("AUTHENTICATED").encode(config.FORMAT))
    print("\n[+][NEW CONNECTION] The client is connected now.")
    while True:
        try:
            message = conn.recv(config.SIZE)

            decrypted_message = config.decrypt_AES(
                message, KEY, IV).decode()

            if decrypted_message.replace(" ", "").lower() == 'exit' or decrypted_message.replace(" ", "") == 'ERROR':
                break
            print(f"Message received: {decrypted_message}")
        except:
            print("An error has occurred. Connection terminated.")
            break

    print("[-][CONNECTION ENDED] Client is disconnected.")
    conn.close()
