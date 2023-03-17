alphabet = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26 }

def getKey(val):
  for k, v in alphabet.items():
    if val == v:
      return k

def decrypt(text, key):
  new_message = ''
  for letter in text:
    new_message += getKey((alphabet[letter] - key)%len(alphabet))
  return new_message

message = "cgrzm namfrzmnemzn unem namr fdnm namerzmnmv efdgpnamqrmgzmbdasveeva ny"
for key in range(1,27):
  print(f"Chave: {key} - A mensagem descriptografada é: {decrypt(message, key)}")