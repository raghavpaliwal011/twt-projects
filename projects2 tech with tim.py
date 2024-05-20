# project 1

print("welcome to my computer quiz")
score=0

playing=input ("do you want to play? ")

if playing != "yes":
    quit()

print("okay lets play  :-) ")
answer = input("what does cpu stands for? ")
if answer .lower == "central processing unit":
    print('correct !')
    score+=1
else:
    print("wrong answer you dumb :< ")
    score-=1

answer = input("what does gpu stands for ?")
if answer .lower == "graphics processing unit":
    print('correct !')
    score+=1

else:
    print("wrong answer you dumb :< ")
    score-=1

answer = input("what does ram stands for? ")
if answer .lower == "random access memory":
    print('correct !')
    score+=1
else:
    print("wrong answer you dumb :< ")
    score-=1

answer = input("what does psu stands for? ")
if answer .lower == "power supply":
    print('correct !')
    score+=1
else:
    print("wrong answer you dumb :< ")
    score-=1

print("you got"+str(score)+"questions correct")

#extra gyaan

text="RAGHAV IS PVP GOD" #it converts the capital to small (.lower)
print(text.lower())

text="raghav is gta god" #it converts the small to capital (.upper)
print(text.upper())