# combat game tutorial!
print("Welcome to my first game!")
name = input("What is your name? : ")
age = int(input("What is your age? : "))
print("hello", name, "you are", age, "years old")

health = 10
is_older = age
print("you are starting with", health, "health")

if is_older >=18:

  print("You are old enough")
  wants_to_play = input("Do you want to play?").lower()
  if wants_to_play == "yes":
    print("Lets play then")

    left_or_right = input("First choice...(left or right) ? : ")
    if left_or_right == 'left':
      ans = input ("nice you follow path and reach al lake .. do you swim across or go round?  ")

      if ans == "round":
        print("you went aound and reahed other side)")

      elif ans == "across":
        print("You lost as bit by fish and lost 5 health")
        health -= 5
        

      ans = input("You noticed a house and a river, which do you go? (river/house)? : ")
      if ans =="house":
        print("you go to house and greeted by stranger, he did not invite u so u lost another 5 ")
        health -=5

        if health <= 0:
          print("you have now 0 health and you loose")
        else:
          print("you survived")

      else:
        print("you fell in river and lost")

    else:
      print("yu feel down and lost...")




  else:
    print("see ya later")
  
  
elif is_older >14:
  print("take permission of your mom and let us know")

else:
  print("need to grow up buddy")

