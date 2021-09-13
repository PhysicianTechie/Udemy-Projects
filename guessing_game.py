#just praccting the game again!
# Guessing Game !

import random
#chhose a level

def choose_level():
  print ("How hard do you want the game to be ? ")
  print ("1 - Easy - 25 chances to try")
  print ("2 - Medium - 15 chances to try")
  print ("3 - Difficult- 5 chances to try")


  while True:
    try:
      level = int(input("How hard do you want the game to be level ( 1 , 2 or 3): "))
      if(level < 1 or level > 3):
        print (" Not a valid level")
        continue

      break
    except ValueError:
      print ("Invalid Choice")

  if level == 1: 
    chances = 25
  elif level == 2:
    chances =15
  else:
    chances =5

  return chances



def calculate_score(points , number , guess):
  lost_points = abs(number - guess)
  points = points - lost_points

  return points


def save_highest_score(score):
  record = 0

  try:
    with open("score.txt" , "r") as score_file:
      record_line = score_file.read()
      if record_line:
        record = int(record_line)
        print(f"The record ofr this game is : {record} points")

  except:
    print("There was no champion")


  if score > record:
    print("You are the new champion")
    with open("score.txt", "w") as score_file:
      score_file.write(str(score))

  else:
    print("Try again to beat the champion")




# main play game logic
def play_game(chances):
  number = random.randint(1,1000)
  points = 9999

  for turn in range(1, chances+1):
    print (f" -> Chance {turn} out of {chances}")

    while True:
      try:
        guess = int(input("Type a number between 1 and 1000: "))
        if (guess < 1 or guess > 1000):
          print("Your guess must be between 1 and 1000")
          continue

        break

      except ValueError:
        print("Invalid Guess value")

        #checking your guesse


    if guess == number: 
     print(f" >> You nailed it! final score: {points} << ")
     save_highest_score(points)
     break

    else:
      if guess > number:
        print(" Your guess was too high, try a lower number")
      elif guess < number:
        print(" Your guess was too low, try a higher number")

      
      points = calculate_score(points, number , guess)

    if turn == chances: 
      print(">> You ran out of chances! <<")
      print(f"The right number is: {number}")

    print("Game over!")


if __name__ == "__main__":
  
  print("#########################")
  print("Welcome to the Guessing Game!")
  print("Guess the number from 1 to 1000")
  print("##########################")


  chances = choose_level()

  play_game(chances)













