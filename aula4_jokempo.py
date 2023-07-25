import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



print("Bem vindo ao jogo Jokenpo!!!")

usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura. "))

if usuario == 0:
    usuario = pedra
    print(f"Você escolheu pedra:\n\n{usuario}")

if usuario == 1:
    usuario = papel
    print(f"Você escolheu papel:\n\n{usuario}")

if usuario == 2:
    usuario = tesoura
    print(f"Você escolheu tesoura:\n\n{usuario}")

computador = random.randint(0, 2)

if computador == 0:
    computador = pedra
    print(f"Computador escolheu pedra:\n\n{computador}")

if computador == 1:
    computador = papel
    print(f"Computador escolheu papel:\n\n{computador}")

if computador == 2:
    computador = tesoura
    print(f"Computador escolheu tesoura:\n\n{computador}")

if usuario == pedra:
  if computador == pedra:
    print("Deu empate!")
  if computador == papel:
    print("Você perdeu!")
  if computador == tesoura:
    print("Você ganhou!")

if usuario == papel:
  if computador == pedra:
    print("Você ganhou!")
  if computador == papel:
    print("Deu empate!")
  if computador == tesoura:
    print("Você perdeu!")

if usuario == tesoura:
  if computador == pedra:
    print("Você perdeu!")
  if computador == papel:
    print("Você ganhou!")
  if computador == tesoura:
    print("Deu empate!")
