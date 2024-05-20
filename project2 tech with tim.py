import random

top_of_range=input("enter a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <= 0:
        print("please type a number greater than 0 next time")
        quit()

else:
    print("please type a number next time")
    quit()

random_number = random.randint(0 ,top_of_range)  #prints randomly any number written in the bracket(it ca be between them also)
print(random_number)

while True:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("you got it! ")
    else:
        print("you got it wrong")