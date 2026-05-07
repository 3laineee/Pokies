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



def win():
    """
    changes the balance when you win
    """
    bet = bet*10
    balance += bet
    print("Ding Ding Ding!!!")
    print("Jackpot!! your new balance is {}".format(balance))
    player_profile["lifetime_wins"] += bet #adds lifetime_wins
    

#lose
def lose():
    """
    changes the balance when you lose
    """
    print("You lose!")
    print("your new balance is {}".format(balance))
    player_profile["lifetime_losses"] += bet * row #adds lifetime losses



def number_asker():
    """
    asks the user for values
    """
    print("Your current balance is ${}.".format(balance))
    rows = 0
    bet = 0

    again = True
    again2 = True
    while again == True:
        try: #try and accept to make sure no crashes/errors

            while again2 == True: #keeps on asking until get number within range
                rows=int(input(("How much rows are you betting?(1-5):$ ")))
                #checks if the rows are inbetween the range
                if rows > 5 or rows < 1:
                    print("Please pick a number within the range!")
                else:
                    again2 = False
            
            bet=int(input("How much money are you betting?: "))
            again == False
            return rows, bet
        except ValueError:
            print("Please pick a number!") #if there is eroor ask them to try again


def value_checker(rows,bet):
    """
    checks if the balance can handle the money
    """
    #calculates the total number
    total_number=rows*bet
    #loops until total number < balance
    while  total_number>balance:     #
        print("Thats too expensive bet less or reduce the amount of rows!")
        value1, value2 = number_asker() #asks user for numbers again and checks if it is bigger than balanv4e
        total_number = value1*value2
        
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

    if row == 2: #checks if user won any of the two rows
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            win()
        else:
            lose()
     
    if row == 3: #check if user won any of the three rows
        if slot_machine[5][0]==slot_machine[6][0]==slot_machine[7][0]==slot_machine[8][0]==slot_machine[9][0]:
            win()
        elif slot_machine[0][0]==slot_machine[1][0]==slot_machine[2][0]==slot_machine[3][0]==slot_machine[4][0]:
            win()
        elif slot_machine[10][0]==slot_machine[11][0]==slot_machine[12][0]==slot_machine[13][0]==slot_machine[14][0]:
            win()
        else:
            lose()

    if row == 4: #check if user won any of the four rows
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

    if row == 5: #check if user won any of the 5 rows
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
        try: #reduces error
            name = input("What is your name?: ").upper()
            location = input("Which region are you playing from?: ").upper()
            again == False
            return name, location
        except ValueError:
            print("Please use your real name and location.")

def profile_compiler(name, location):
    """
    takes the info and turns it into a "profile" list
    """
    profile = {"name": name, "location": location, "lifetime_losses":0, "lifetime_wins":0, "targeted_ads": False}
    return profile


def balance_depositer():
    """
    asks user to add more money 
    """
    again = True
    amount = 0
    
    if player_profile["targeted_ads"] == True: #checks if user is a whale and deposits follows accordingly
        while again == True:
            try:
                amount = int(input("How much money would you like to deposit?:$ ")) * 2
                break #breaks when it is correct
            except ValueError:
                print("Please choose a number!")
    else:
        while again == True: #if user isnt whale just normal
            try:
                amount = int(input("How much money would you like to deposit?:$ ")) * 2
                break #breaks when it is correct
            except ValueError:
                print("Please choose a number!")
        return amount

def whale_checker():
    """
    checks if user is whale and prints deal
    """
    if player_profile["lifetime_losses"] >= 500:
        player_profile["targeted_ads"] = True
        print("---SPECIAL VIP OFFER---")
        print("Double your next deposit!")
    else:
        print("Keep playing to get exculsive deals!")


#main routine
if __name__ == "__main__":
    #setting up variables
    loop = 0
    balance = 1000
    again = 'T'
    bet = 0

    #asks for user info and turns it into a dictionary
    name1, location1 = user_info()
    player_profile = profile_compiler(name1, location1)

    while again == 'T':
        choice = input("Would you like to deposit some more money? (Yes or No): ").upper()
        if choice == 'YES': #try and except to not crash
            deposit = balance_depositer()
            balance += deposit #adds the deposit to balance

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

        #checks if user is a 'whale'
        whale_checker()


        #asks user to play again
        repeat = True
        while repeat == True: #keeps looping untill get T or F
            again = input("Would you like to play again? T or F: ").upper()
            if again != 'T' and again != 'F': 
                print("Please choose another value!")
            else:
                repeat = False

    print("Thank you for playing!") #thank user for playing

            
            

        
        
