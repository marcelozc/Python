alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
  cypher_text = ""
  
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      cypher_text += new_letter
    else:
      cypher_text += char
  print(f"The encoded text is {cypher_text}")
  
def decrypt(cypher_text, shift_amount):
  plain_text = ""
  for char in cypher_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position - shift_amount
      new_letter = alphabet[new_position]
      plain_text += new_letter
    else:
      plain_text += char
  print(f"The decoded text is {plain_text}")

repete = True

while repete:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  
  if direction == "encode":
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)

  again = input("\nDo you want to re-do the program? (type yes/no) ")
  if again == "yes":
    repete = True   
  else:
    repete = False
