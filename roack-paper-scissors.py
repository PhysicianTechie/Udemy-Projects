# rock paper scissors game plan

# first create options to choose
options = ['rock', 'paper', 'scissors']
import random

#create no of turns
while True:
  try:
    turns = int(input('Please choose 3 or 5 : '))
    if turns == 3 or turns == 5:
      break
    continue
  
  except ValueError:
    print('Invalid choice')


# how many victories you need to win the game
necessary_wins = int(turns/2) + 1


# main logid of the game
# set the counter
player_wins = 0
computer_wins = 0

#main while loop breaks only when someone wins
while True:
  
  # to get the player input
  while True:
    player = input( " 'rock','paper','scissors' : ")
    if player in options:
      break

  computer = random.choice(options)


  if player == computer:
    print ('Its a Tie')
  elif player == 'rock' and computer =='paper':
    print ('computer wins as paper covers rock')
    computer_wins += 1
  elif player == 'paper' and computer == 'scissors':
    print ('computer wins as scissors cut  paper')
    computer_wins += 1
  elif player == 'scissors' and computer == 'rock':
    print ('computer wins as rock smashes scissors')
    computer_wins += 1
  elif player == 'paper' and computer == 'rock':
    print ('player wins as paper covers rock')
    player_wins += 1
  elif player == 'scissors' and computer == 'paper':
    print ('player wins as scissors cut paper')
    player_wins += 1
  elif player == 'rock' and computer == 'scissors':
    print ('player wins as rock smashes scissors')
    player_wins +=1

    if player_wins == necessary_wins or computer_wins ==necessary_wins:
      break

if player_wins > computer_wins:
  print ('player wins')
else:
  print ('commputer wins')


print (f' You scored: {player_wins} points')



