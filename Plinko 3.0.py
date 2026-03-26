#Pokies code 3.0
#ELAINE CHEN 26/02/2026
#import random
import random

#setting up the rows
slot_machine = [
    ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"],
    ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"],
    ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"],
    ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"],
    ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"], ["🍒","🍌","🍎","🍍","🍐"]
    ]

#setting up variables
loop = 0
balance = 1000
again = 'T'
bet = 0


def win():
    bet = bet*10
    balance += bet
    print("Ding Ding Ding!!!")
    print("Jackpot!! your new balance is {}".format(balance))
    choice =input("Would you like to play again? (T or F): ")
    return choice.capitalize()

#lose
def lose():
    """
    changes the ballence when you lose
    """
    print("You lose!")
    print("your new balance is {}".format(balance))
    #sends the info 'outside' of the function
    choice =input("Would you like to play again? (T or F): ")
    return choice.capitalize()

def number_asker():
    """
    asks the user for values
    """
    print("Your current balance is ${}.".format(balance))
    bet=int(input(("How much money are you betting?:$ ")))
    rows=int(input("How much rows are you betting? (1-5): "))
    return rows, bet

def value_checker(total_value):
    """
    checks if the balance can handle the money
    """
    while  total_value> balance:     #
        print("Thats too expensive bet less or reduce the amount of rows!")
        a, b = number_asker()
        total_value = balance_calculator(a, b)
    return total_value


def balance_calculator(row_value,bet_value):
    """
    calculates the current balance
    """
    total = row_value*bet_value
    balance_current= balance-total
    return balance_current



def shuffle():
    """
    shuffles the lists
    """
    for i in slot_machine:
        random.shuffle(i)

def plinko():
    """
    print the plinkos
    """
    print(slot_machine[0][0]+slot_machine[1][0]+slot_machine[2][0]+slot_machine[3][0]+slot_machine[4][0])
    print(slot_machine[5][0]+slot_machine[6][0]+slot_machine[7][0]+slot_machine[8][0]+slot_machine[9][0])
    print(slot_machine[10][0]+slot_machine[11][0]+slot_machine[12][0]+slot_machine[13][0]+slot_machine[14][0])
    
while again == 'T':    
    #shuffles the plinko
    shuffle()
    #asks user for num and calculates their balance
    a, b = number_asker()
    c = balance_calculator(a, b)
    #checks the value of the amount betting is vaild  and stores into a variable.
    new_balance=value_checker(c)
    print("Your new balance is ${}".format(new_balance))
    #print out plinkos
    plinko()

    #checks if user won
    if a == 1:
        #checks the slots for winning or losing
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]:
            #sets again the value of the input of win_1
            again=win()
        else:
            again =lose()

    if a  == 2:
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            again=win_1()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            again =win_1()
        else:
            again = lose()
     
    if a == 3:
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            again=win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            again =win()
        elif slot_machine[10][0]==slot_machine[11][0]==slot_machine[12][0]==slot_machine[13][0]==slot_machine[14][0]:
            again =win()
        else:
            again = lose()

    if a == 4:
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            again=win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            again =win()
        elif slot_machine[10][0]==slot_machine[11][0]==slot_machine[12][0]==slot_machine[13][0]==slot_machine[14][0]:
            again =win()
        elif slot_machine[0][0]==slot_machine[4][0]==slot_machine[6][0]==slot_machine[8][0]==slot_machine[12][0]:
            again=win()
        else:
            again = lose()

    if a == 5:
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            again=win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            again =win()
        elif slot_machine[10][0]==slot_machine[11][0]==slot_machine[12][0]==slot_machine[13][0]==slot_machine[14][0]:
            again =win()
        elif slot_machine[0][0]==slot_machine[4][0]==slot_machine[6][0]==slot_machine[8][0]==slot_machine[12][0]:
            again=win()
        elif slot_machine[2][0]==slot_machine[6][0]==slot_machine[8][0]==slot_machine[10][0]==slot_machine[14][0]:
            again=win()
        else:
            again = lose()


        
        

        
        
