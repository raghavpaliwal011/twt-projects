name = input ("type your name : ")
print("welcome",name,"to this adventure! ")

answer=input(
    "you have come to a dirt road and it has come to an end and you can go left or right.which way would you like to go ? ").lower()
 
if answer == "left":
    answer = input ("you have come to a river,you can walk around or swina accross? type walk to walk around and swim to swim accross: ")
    
    if answer =="swim":
        print("you swam accross and were eaten by an alligator.i meant you lost you noob.")
    elif answer =="walk":
        print("you walked for many miles and ran out of water and you lost the game you noob.")
    else:
        print('not a valid option you lose')
elif answer == "right":
    answer = input ("you have come to a bridge , it looks wobbly , do you want to cross it or head back (cross/back) ? ")

    if answer =="back":
        print("you go back and lose.")
    elif answer =="cross":
        print("you crossed the bridge and meet a stranger . do you talk to them (yes/no) ?")

        if answer =="yes":
            print("you talk to the stranger and he give you gold. you win")

        elif answer == "no":
            print("you lose")

        else:
            print('not a valid option you lose')

    else:
        print('not a valid option you lose')
    
else:
    print('not a valid option you lose')

print("thank you for trying ," , name)
