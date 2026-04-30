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
lifetime_losses = 0


def win():
    """
    changes the ballance when you win
    """
    bet = bet*10
    balance += bet
    print("Ding Ding Ding!!!")
    print("Jackpot!! your new balance is {}".format(balance))

#lose
def lose():
    """
    changes the ballence when you lose
    """
    print("You lose!")
    print("your new balance is {}".format(balance))
    #sends the info 'outside' of the function


def number_asker():
    """
    asks the user for values
    """
    print("Your current balance is ${}.".format(balance))
    rows = 0
    bet = 0

    again = True
    while again == True:
        try:
            rows=int(input(("How much rows are you betting?(1-5):$ ")))
            bet=int(input("How much money are you betting?: "))
            again == False
            return rows, bet
        except ValueError:
            print("Please pick a number!")


def value_checker(rows,bet):
    """
    checks if the balance can handle the money
    """
    #calculates the total number
    total_number=rows*bet
    #loops until total number < balance
    while  total_number>balance:     #
        print("Thats too expensive bet less or reduce the amount of rows!")
        a, b = number_asker()
        total_number = a*b
        
    return total_number


def balance_calculator(total_number):
    """
    calculates the current balance
    """
    #finds the current balance
    balance_current= balance-total_number
    return balance_current



def shuffle():
    """
    shuffles the lists
    """
    for i in slot_machine:
        random.shuffle(i)

def pokies():
    """
    print the plinkos
    """
    print(slot_machine[0][0]+slot_machine[1][0]+slot_machine[2][0]+slot_machine[3][0]+slot_machine[4][0])
    print(slot_machine[5][0]+slot_machine[6][0]+slot_machine[7][0]+slot_machine[8][0]+slot_machine[9][0])
    print(slot_machine[10][0]+slot_machine[11][0]+slot_machine[12][0]+slot_machine[13][0]+slot_machine[14][0])

def win_checker(row):
    """
    checks for any winning rows
    """
    if row == 1:
        #checks the slots for winning or losing
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]:
            #sets again the value of the input of win_1
            win()
        else:
            lose()

    if row == 2:
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            win()
        else:
            lose()
     
    if row == 3:
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            win()
        elif slot_machine[10][0]==slot_machine[11][0]==slot_machine[12][0]==slot_machine[13][0]==slot_machine[14][0]:
            win()
        else:
            lose()

    if row == 4:
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            win()
        elif slot_machine[10][0]==slot_machine[11][0]==slot_machine[12][0]==slot_machine[13][0]==slot_machine[14][0]:
            win()
        elif slot_machine[0][0]==slot_machine[4][0]==slot_machine[6][0]==slot_machine[8][0]==slot_machine[12][0]:
            win()
        else:
            lose()

    if row == 5:
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            win()
        elif slot_machine[10][0]==slot_machine[11][0]==slot_machine[12][0]==slot_machine[13][0]==slot_machine[14][0]:
            win()
        elif slot_machine[0][0]==slot_machine[4][0]==slot_machine[6][0]==slot_machine[8][0]==slot_machine[12][0]:
            win()
        elif slot_machine[2][0]==slot_machine[6][0]==slot_machine[8][0]==slot_machine[10][0]==slot_machine[14][0]:
            win()
        else:
            lose()

def user_info():
    """
    asks user for info and returns
    """
    again = True
    while again == True:
        try:
            name = input("What is your name?: ").upper()
            location = input("Which region are you playing from?: ").upper()
            again == False
            return name, location
        except ValueError:
            print("Please use your real name and location.")


#main routine
if __name__ == "__main__":
    #asks for user info
    name1, location1 = user_info()
    while again == 'T':    
        #shuffles the pokies
        shuffle()
        #asks user for num 
        row, bet = number_asker()
        #checks if num is valid
        total_number =value_checker(row, bet)
        balance = balance_calculator(total_number)
        print("Your new balance is ${}".format(balance))
        #print out plinkos
        pokies()
        #checks if user won
        win_checker(row)

        #asks user to play again
        repeat = True
        while repeat == True: #keeps looping untill get T or F
            again = input("Would you like to play again? T or F: ").upper()
            if again != 'T' and again != 'F': 
                print("Please choose another value!")
            else:
                repeat = False
            

    print("Thank you for playing!") #thank user for playing

            
            

        
        
