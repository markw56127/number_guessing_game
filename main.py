import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
def number_game():
  number = random.randint(1,100)
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
  if difficulty == 'easy':
    attempts = 10
  elif difficulty == 'hard':
    attempts = 5
  while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
      print("You win!")
      break
    elif guess < number:
      attempts -= 1
      if attempts == 0:
        print(f"You lose. The number was {number}")
      else:
        print(f"Too low.\nGuess again.\nYou have {attempts} remaining attempts to guess the number.")
    elif guess > number:
      attempts -= 1
      if attempts == 0:
        print(f"You lose. The number was {number}")
      else:
        print(f"Too high.\nGuess again.\nYou have {attempts} remaining attempts to guess the number.")
    else:
      print("Please enter a number.")
  again = input("Would you like to play again? Type 'yes' or 'no'. ")
  if again == 'yes':
    number_game()

number_game()
