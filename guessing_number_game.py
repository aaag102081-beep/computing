import random
print("")
secret = random.randint(1,50)
# print(secret)
chances = int(input("Enter the number of chances you would like: "))
while chances>0:
    num = int(input("Please enter a number between 1 to 50: "))
    if num == secret:
        print("You guessed it right!")
        break
    else:
        if num>secret:
            print("Guess Lower")
        else:
            print("Guess Higher")
    chances = chances - 1
    print("You have",chances,"chances left")
print("Game Ended")

