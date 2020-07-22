import random
#create a random number
#creating found and setting it to False
#Run this code while found is still = to False
#Getting an input of a number. Making it an int.
#Run if our goes is the random number 
#Make found True
#Say you Win 
r = random.randit(-100,100)
found = False
while found == False:
  g = int(input("Guess a nubmer:  "))
  if g==r:
    print("You win!!!")

  elif g > r:
      print(str(g), "is more then it")
  elif g < r:
        print(str(g), "is less then it")
  else:
          print("This is not a number, try again.")

   