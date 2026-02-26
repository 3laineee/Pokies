#Pokies code 3.0
#ELAINE CHEN 26/02/2026
#import random
import random

#setting up the rows
slot_machine=[["🍒","🍌","🍎","🍍","🍐"],["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"],["🍒","🍌","🍎","🍍","🍐"],["🍒","🍌","🍎","🍍","🍐"],["🍒","🍌","🍎","🍍","🍐"],["🍒","🍌","🍎","🍍","🍐"],["🍒","🍌","🍎","🍍","🍐"],["🍒","🍌","🍎","🍍","🍐"]]

#setting up variables
loop = 0
balance = 1000
again = 'T'
bet = 0

#setting up fucntions

#winning functim
def win_1():
    bet = bet*10
    balance += bet
    print("Ding Ding Ding!!!")
    print("Jackpot!! your new balance is {}".format(balance))
    again = input("Would you like to play again (T or F): ")
#lose
def lose():
    print("You lose!")
    print("your new balance is {}".format(balance))
    choice= input("Would you like to play again (T or F): ")
    #sends the info 'outside' of the function
    return choice.upper()

#shuffling the small lists inside the big list slot machine using random
def shuffle():
    random.shuffle(slot_machine[0])
    random.shuffle(slot_machine[1])
    random.shuffle(slot_machine[2])
    random.shuffle(slot_machine[3])
    random.shuffle(slot_machine[4])
    random.shuffle(slot_machine[5])
    random.shuffle(slot_machine[6])
    random.shuffle(slot_machine[7])
    random.shuffle(slot_machine[8])

#shows you the symbols:
def plinko():
    print(slot_machine[0][0]+slot_machine[1][0]+slot_machine[2][0])
    print(slot_machine[3][0]+slot_machine[4][0]+slot_machine[5][0])
    print(slot_machine[6][0]+slot_machine[7][0]+slot_machine[8][0])

    
while again == 'T' and balance > 0:
    shuffle()
    print("Your current balance is ${}.".format(balance))
    bet=int(input(("How much money are you betting?:$ ")))
    rows=int(input("How much rows are you betting? (1-3): "))

#checks if their bet is bigger than their balance or not
    if rows*bet > balance:
        print("Thats too expensive bet less or reduce the amount of rows!")
    else:
        total = rows*bet
        balance= balance-total
        print("Your current balance is:${}".format(balance))
        plinko()

        #checks how much rows their betting
        if rows == 1:
        #checks the slots for winning or losing
            if slot_machine[3]==slot_machine[4]==slot_machine[5]:
                #sets again the value of the input of win_1
                again=win_1()
            else:
                again =lose()

        if rows == 2:
            if slot_machine[3]==slot_machine[4]==slot_machine[5]:
                again=win_1()
            elif slot_machine[0]==slot_machine[1]==slot_machine[2]:
                again =win_1()
            else:
               again = lose()
 
        if rows == 3:
            if slot_machine[3]==slot_machine[4]==slot_machine[5]:
                again =win_1()
            elif slot_machine[1]==slot_machine[2]==slot_machine[3]:
                again =win_1()
            elif slot_machine[6]==slot_machine[7]==slot_machine[8]:
                again =win_1()
            else:
                again =lose()
#when while loop is broken thank user
print("Thanks for playing, see you next time!")


