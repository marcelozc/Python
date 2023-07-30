import random
from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["arvore","amor","gato","cacho","rio","perola","flor","lua","ceu","melao","mesa","chave","banho","livro","cesta","marca","peixe","sorte","praia","bolsa","antes","rocha","camel","amigo","pipa","canto","vaso","papai","queijo","rodas","trevo","sobre","lente","velho","corte","prato","cinza","terra","mundo","lirio","leao","cavalo","roda","barco","pele","sapato","chuva","lago","alien","caneta","pastel","danca","teatro","pesca","piscar","brinco","fraco","anjos","sucos","biscoito","canto","fazer","falar","comer","chove","passeio","forno","pular","bebes","azeite","fruta","fofoca","areia","feira","salmao","bruxa","brasa","fogos","cegar","habito","focos","honra","joias","mural","palha","irmao","limpo","pneus","queda","toalha","vagas","sorte","secar","pegar","velho","queda","visita","rapou","acatar","bigorna","cinico"]
chosen_word = random.choice(word_list)

vidas = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
n = len(chosen_word)
for _ in range(len(chosen_word)):
  display.append("_")

print(f"A palavra que você precisa descobrir tem {n} letras\n")
print(f"{display}")
print(stages[vidas])

fim_de_jogo = False
tentativas = []

while not fim_de_jogo:
  guess = input("Escolha a letra: ").lower()
  clear()
  
  if len(guess) == 1:
    if guess not in tentativas:
      for position in range(len(chosen_word)):
        letter = chosen_word[position]
            
        if letter == guess:
          display[position] = letter
          
      if guess in chosen_word:
        print(f"Você acertou, {guess} é uma das letras.\n")      
      
      if guess not in chosen_word:
        vidas -= 1
        print(f"Você errou, {guess} não é uma das letras.\n")

      tentativas.append(guess)
      print(f"tentativas:{sorted(tentativas)}")
      print(stages[vidas])
      print(f"{display}\n")
        
      if vidas == 0:      
        print(f"GAME OVER... Você perdeu!\nA palavra era {chosen_word}")
        break      
    
      if "_" not in display:
        fim_de_jogo = True
        print("Você venceu!")      
    
    else:
      print(f"Você já escolheu a letra {guess} anteriormente. Tente novamente.")
      print(f"tentativas:{sorted(tentativas)}")
      print(stages[vidas])
      print(f"{display}\n")
  
  else:
    print("Escreva apenas uma letra...")
