'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
answer=input("Type Y if you want to play")
if answer.lower()="y":

print("What move do you chose?")
import random
num=random.randrange(1,4)
if num==1:
    print("rock")
elif num==2:
    print("paper")
else:
    print("sissors")










