# importar
import random, art
from game_data import data
from replit import clear

# criar função que escolhe item da lista
def choose():
  return data.choice(data)

# criar função que compara
def compare(a,b):
  if a > b:
    return "A"
  if b > a:
    return "B"

# criar função jogo
def game():
  game_should_continue = True
  score = 0
  A = choose()
  print(art.logo)
  while game_should_continue:    
    
    B = choose()
    while A == B:
      B = choose()
  
    A_followers = A["follower_count"]
    B_followers = B["follower_count"]
    
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    
    guess = input("Who has more followers? (A/B) ").upper()
    answer = compare(A_followers,B_followers)
          
    if guess != answer:
      clear()
      print(art.logo)
      print(f"{A['name']} has {A_followers}. {B['name']} has {B_followers}")
      print(f"Sorry, that was wrong. Final score: {score}.")
      game_should_continue = False
    else:
      clear()
      score += 1
      print(art.logo)
      print(f"{A['name']} has {A_followers}. {B['name']} has {B_followers}")
      print(f"You're right! Current score: {score}.\n")
      A = B  

game()
