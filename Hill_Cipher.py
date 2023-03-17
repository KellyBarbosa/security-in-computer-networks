import numpy as np 
from egcd import egcd

alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
len_alphabet = len(alphabet)

def getKey(val):
  for k, v in alphabet.items():
    if val == v:
      return k

def genKey():
  dim = 2
  key = [[3,3], [2, 5]]
  det = int(np.round(np.linalg.det(key))) 
  inv = np.linalg.inv(key)
  gcd, x, y = egcd(det, len_alphabet)
  return key, dim, det, inv, x

def encrypt(text, len_text):
  encrypted_message = ''
  unencrypted_message = []
  for i in message:
    unencrypted_message.append(alphabet[i])
  parts = int(len_text/len_key)
  addRandom = False
  if len_text%len_key != 0:
    parts += 1
    addRandom = True
  start = 0
  end = len_key
  for i in range(parts):
    unencrypted_partial_message = unencrypted_message[start:end]
    if addRandom and i == (parts-1):
      unencrypted_partial_message.append(alphabet[text[0]])
    res = (np.dot(key, unencrypted_partial_message))%len_alphabet
    for i in res:
      encrypted_message += getKey(i)
    start=end
    end += len_key
  return encrypted_message

def decrypt(text, len_text):
  decrypted_message = ''
  encrypted_message = []
  for i in text:
    encrypted_message.append(alphabet[i])
  parts = int(len_text/len_key)
  addRandom = False
  if len_text%len_key != 0:
    parts += 1
    addRandom = True
  start = 0
  end = len_key
  inv_key = inv_mult * np.round(det * inv).astype(int) % (len_alphabet)
  for i in range(parts):
    res = (np.dot(inv_key, encrypted_message[start:end]))%len_alphabet
    for i in res:
      decrypted_message += getKey(i)
    start=end
    end += len_key
  if addRandom:
    decrypted_message = decrypted_message[:-1]
  return decrypted_message

key, len_key, det, inv, inv_mult = genKey()

message = input("Digite uma mensagem (sem caracteres especiais): ").lower()
if " " in message:
  message = message.replace(" ", "")
len_message = len(message)

print(f'\nA mensagem digitada foi: {message}')
encrypted_message = encrypt(message, len_message)
print(f'Texto criptografado: {encrypted_message}')
print(f'Texto descriptografado: {decrypt(encrypted_message, len_message)}')