import random

def comparar(numero, palpite):
  if numero == palpite:
    print(f"Você acertou, o número é {numero}")
    global acabou 
    acabou = True
  elif numero > palpite:
    if dificuldade == "f" and i > 10 and acabou == False:
      print(f"Você não conseguiu adivinhar, o número era {numero}")       
      acabou = True
    elif dificuldade == "d" and i > 5 and acabou == False:
      print(f"Você não conseguiu adivinhar, o número era {numero}")
      acabou = True
    else:
      print(f"Você chutou muito baixo, meu número é mais alto que {palpite}...")
  elif numero < palpite:
    if dificuldade == "f" and i > 10 and acabou == False:
      print(f"Você não conseguiu adivinhar, o número era {numero}")
      acabou = True
    elif dificuldade == "d" and i > 5 and acabou == False:
      print(f"Você não conseguiu adivinhar, o número era {numero}")
      acabou = True
    else:  
      print(f"Você chutou muito alto, meu número é menor que {palpite}...")

print("Bem vindo ao jogo de advinhação!!\nEstou pensando em um número de 1 a 100")

numero = random.randint(1,100)
print(f"Para teste, o número que estou pensando é {numero}")

dificuldade = input("Escolha a dificuldade: Digite f para fácil e d para difícil: ")

acabou = False
i = 1

while acabou == False:
  if dificuldade == "f":        
    palpite = int(input("Digite seu palpite: "))
    i += 1
    comparar(numero,palpite)           

  if dificuldade == "d":    
    palpite = int(input("Digite seu palpite: "))
    i += 1
    comparar(numero,palpite)      

