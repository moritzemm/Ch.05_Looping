'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
print("Welcome to my camel game!")
print("You must travel 200 miles, You will have a mob of angry people wanting to harm you")
print("You will be asked to give camands every few miles")
print("Your commands will be as follows\n1.Drink\n2.normal speed\n3.Zoom\n4.Sleep\n5.Update\n6.Quit ")
print("Good Luck!\n        ")
done = False
M=0
T=0
CT=0
C=6
N=-20
import random
while not done:
    if T<6:
        if N < M:
            if CT<9:
                RN = random.randint(1, 21)

                In = int(input("Choose:\n1.Drink\n2.normal speed\n3.Zoom\n4.Sleep\n5.Update\n6.Quit\n "))
                if RN==7:
                    print("You found an oasis! You drank tons and so did your camel. You also refilled your canteen")
                    T=0
                    CT=0
                    C=6
                if T >= 4:
                    print("You are thirsty")
                if M == 200 and done == False:
                    print("Congratulations! You Won!")
                if In==6:
                    done=True
                elif In==1:
                    if C>0:
                        C-=1
                        T=0
                    else:
                        print("Error, you can't drink your out of water")
                    print("You have ",C,"Drinks left")
                elif In==5:
                    print("Miles traveled:",M)
                    print("Drinks Left:", C)
                    print("The people are", N , "Miles behind you")
                    print("Your thirst is",T)
                elif In==4:
                    CT==0
                    print("Your camel is happy")
                    N += random.randrange(7,15)
                elif In==3:
                    M+= random.randrange(10,21)
                    print("You have traveled", M, "Miles")
                    T+=1
                    CT += random.randrange(1,4)
                elif In==2:
                    M+= random.randrange(5,13)
                    print("You have traveled",M,"Miles")
                    T+=1
                    CT+=1
                    N += random.randrange(7, 15)
                else:
                    print("Sorry, Not an option")
            elif CT > 5 and CT <=9:
                    print("Your camel is getting tired")
            else:
                 print("Your camel is dead")
        elif N > M-15:
            print("The natives are getting close")
        else:
            print("The natives have caught you, They stole your camel and killed you")
            done = True
    else:
        print("You died of thirst")
        done = True
        print("Good try! Play again?")