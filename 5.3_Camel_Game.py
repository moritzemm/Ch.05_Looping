'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
print("Welcome to my camel game!")
print("You must travel 200 miles, You will have a mob of angry people wanting to harm you")
print("You will be asked to give camands every few miles")
print("Your commands will be as follows\n1.Drink\n2.normal speed\n3.Zoom\n4.Sleep\n5.Update\n6.Quit ")
done = False
M=0
T=0
CT=0
C=6
N=-20
import random
while not done:
    In=int(input("Choose:\n1.Drink\n2.normal speed\n3.Zoom\n4.Sleep\n5.Update\n6.Quit\n "))
    if In==6:
        set done=True
    elif In==1:
        C-=1
        print("You have ",C,"Drinks left")
    elif In==5:
        print("Miles traveled:",M)
        print("Drinks Left:", C)
        print("The people are", N , "Miles behind you")
        print("Your thirst is",T)
    elif In==4:
        set CT=0
        print("Your camel is happy")
        N += random.randrange(7,15)
    elif In==3:
        M+= random.randrange(10,21)
        T+=1
        CT += random.randrange(1,4)
    elif In==2:
        M+= random.randrange(5,13)
        print("You have traveled",M,"Miles")
        T+=1
        CT+=1
        N += random.randrange(7, 15)
    elif #15





