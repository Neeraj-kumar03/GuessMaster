import random
target=random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit(Q): ")
    if userChoice == "Q":
        break

    userChoice = int(userChoice)
    if userChoice == target:
        print("Well Done:")
        break
    elif userChoice > target:
        print("Your number is bigger than the target")
    else:
        print("Your number is smaller than the target")    
print("---GAME OVER----")        