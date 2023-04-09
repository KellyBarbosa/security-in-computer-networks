import sympy
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

caracteres = [ascii_lowercase, ascii_uppercase, digits, punctuation]
random.shuffle(caracteres)
caracteres = ''.join(caracteres)

def digitar():
    while True:
        seed = int(input("Informe um número de pelo menos 1024 bits: "))
        if(seed.bit_length() >= 1024 and seed%2 != 0):
            return seed
        else:
            print("O número digitado precisa ser maior. Tente novamente!")

def sortear():
    import secrets
    while True:
        seed = secrets.randbits(1024)
        if(seed %2 != 0):
            return seed

def genPQ():
    while True:
        number = sympy.randprime(1,10000000000000000000000) 
        if seed%number != 0 and number % 4 == 3:
            return number
        
def genBBS(seed, p, q):
    size = random.randint(1, 100)
    xn = seed**2 % (p*q)
    bbs = ''
    for i in range(1, size+1):
        xn = xn**2 % (p*q)
        bbs += str((xn**2 % (p*q))%2)
    return int(bbs, 2)

def genPass(password_length, seed, p, q): 
    password = ''
    while len(password) < password_length:
        password += caracteres[genBBS(seed, p, q)%len(caracteres)]
    return password

while True:
    op = int(input("Deseja digitar a semente ou gerar uma aleatoriamente? (1 - Digitar e 2 - Gerar)\nEscolha: "))
    if(op == 1 or op == 2):
        break

while True:
    password_length = int(input("Informe o comprimento da senha (no mínimo 16 caracteres): "))
    if password_length >= 16:
        break

if(op == 1):
    seed = digitar()
else:
    seed = sortear()

print(f'A sua senha é: {genPass(password_length, seed, genPQ(), genPQ())}')