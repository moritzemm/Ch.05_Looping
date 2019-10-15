'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
game=0
heads=0
tails=0
import random
while game<50:
    num = random.randrange(0, 2)
    if num==0:
        print("Heads")
        game+=1
        heads+=1
    else:
        print("Tails")
        game+=1
        tails+=1
print("There where ",heads," heads")
print("There where ",tails, " tails")






