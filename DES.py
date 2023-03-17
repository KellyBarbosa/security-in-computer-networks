clear_text = input('Informe o texto claro: ')

def dec2bin(value):
  return format(int(value), "b")

def bin2dec(value):
  return int(str(value),2)

def xor(value1, value2):
  return int(value1) ^ int(value2)

def complete_bits(value):
  zeros = [0] * (64 - len(value))
  zeros = ''.join(map(str, zeros))
  return zeros+value

def generate_key():
  return ''.join(map(str,  [1] * 48))

def generate_initial_permutation(value):
  initial_permutation_table = (58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7)
  return ''.join(value[e-1] for e in initial_permutation_table)

def expansion(value):
  expansion_table = (32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1)
  return ''.join(value[e-1] for e in expansion_table)

def calculate_box(value):
  l = bin2dec(value[0]+value[-1])
  c = bin2dec(value[1:-1])
  if l == 0:
    l = 1
  if c == 0:
    c = 1
  return l, c

def replacement_boxes(value):
  b1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
  b2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
  b3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
  b4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
  b5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
  b6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
  b7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
  b8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
  boxes = (b1,b2,b3,b4,b5,b6,b7,b8)
  v = [value[:6], value[6:12], value[12:18], value[18:24], value[24:30], value[30:36], value[36:42], value[42:]]
  new_value = ''
  count_box = 0
  for i in v: 
    l, c = calculate_box(i)
    v_box = boxes[count_box][l-1][c-1]
    v_bin = dec2bin(v_box)
    if len(v_bin) < 4:
      while len(v_bin) < 4: 
        v_bin = '0'+ v_bin
    new_value += v_bin
    count_box += 1
  return new_value

def permutation(value):
  permutation_table = (16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25)
  return ''.join(value[e-1] for e in permutation_table)

def cryptography(n_rounds):
  value = initial_permutation
  for i in range(n_rounds):
    result = round(value)
    value = result
  return value

def round(text):
  l_text = text[:32]
  r_text = text[32:]
  r_expansion = expansion(r_text)
  r_xor = ''
  for i in range(len(r_expansion)):
    r_xor += str(xor((r_expansion[i]), key[i]))
  r_replacement_boxes = replacement_boxes(r_xor)
  r_permutation = permutation(r_replacement_boxes)
  r_xor = ''
  for i in range(len(r_permutation)):
    r_xor += str(xor((l_text[i]), r_permutation[i]))
  return r_text+r_xor

clear_text_bin = dec2bin(clear_text)
new_clear_text_bin = complete_bits(clear_text_bin)
initial_permutation = generate_initial_permutation(new_clear_text_bin)
key = generate_key()
while True:
  n_rounds = int(input('Informe a quantidade de rounds: '))
  if n_rounds > 0 and n_rounds < 17:
    break
encrypted_value =  cryptography(n_rounds)
print(f'Valor após o round {n_rounds}: {encrypted_value}')
print(f'Bits 1, 16, 33 e 48:\n1: {encrypted_value[0]}\n16: {encrypted_value[15]}\n33: {encrypted_value[32]}\n48: {encrypted_value[47]}')