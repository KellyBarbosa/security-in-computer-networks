import string
import random

alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
len_alphabet = len(alphabet)

def getKey(val):
  for k, v in alphabet.items():
    if val == v:
      return k

def genKey(size=6, chars=string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def encrypt(message):
  new_message = ''
  for i in range(len_message):
    encrypted_letter = (alphabet[message[i]] + alphabet[key[i]])%len_alphabet
    new_message += getKey(encrypted_letter)
  return new_message

def decrypt(message):
  new_message = ''
  for i in range(len_message):
    decrypted_letter = (alphabet[message[i]] - alphabet[key[i]])%len_alphabet
    new_message += getKey(decrypted_letter)
  return new_message

message = input("Digite uma mensagem (sem caracteres especiais): ").lower()
if " " in message:
  message = message.replace(" ", "")
len_message = len(message)
key = genKey(len_message)

encrypted_message = encrypt(message)

print(f"\nA mensagem informada foi: {message}\nA mensagem criptografada é: {encrypted_message}\nA mensagem descriptografada é: {decrypt(encrypted_message)}")