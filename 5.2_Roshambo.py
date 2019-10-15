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
done=False
player=0
total=0
answer=input("Type Y if you want to play")
while answer.lower()=="y" and done==False :
    play=int(input("What move do you chose?\npress 1 for rock\npress 2 for paper\npress 3 for scissors\npress 4 to Quit"))
    import random
    num = random.randrange(1, 4)
    total+=1
    if play=="1":
        if num==1:
            print("Rock, we tied!")
        elif num==2:
            print("Paper, I win!")
        elif num==3:
            print("Scissors, You win!")
            player+=1
    elif play==2:
        if num == 1:
            print("Rock, You win!")
            player+=1
        elif num == 2:
            print("Paper, We tied!")
        elif num==3:
            print("Scissors, I win!")
    elif play==3:
        if num == 1:
            print("Rock, I win!")
        elif num == 2:
            print("Paper, You won!")
            player+=1
        elif num==3:
            print("Scissors, We tied!")

    else:
        print("You won", player, "times out of", total)
        done==True



