import random

num=random.randint(1,99)
# random number generator
guess=0
# Gives guess a starting value

while guess!=num:
  guess=int(input("Guess a number between 1-99: "))
  # asks user for a number continuosly in a loop
  if guess<num:
    print("Too low! Try again!")
  elif guess>num:
    print("Too high! Try again!")
  elif guess==num:
    print("You got it!")
    break