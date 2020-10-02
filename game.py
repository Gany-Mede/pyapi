#!/usr/bin/python3

import random
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'west' : 'Battle Room',
                },

            'Battle Room': {
                'east' : 'Hall',
                'south' : 'Stocks Room'
                },
            'Stocks Room' : {
                'north': 'Battle Room',
                'east': 'Kitchen',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                  'west' : 'Stocks Room'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'east' : 'Dragon Room',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'east' : 'Riddle Room',
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },
            'Riddle Room' : {
                  'west': 'Pantry',
                  'south' : 'Dragon Room',
                },
            'Dragon Room' : {
                  'north': 'Riddle Room',
                  'west' : 'Dining Room',

                }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

userScore = 0
computerScore = 0

#Battle Room function
def battle():
    print("Welcome to the rock paper scissors game!")
    print("The best of three wins, if there is a draw, there will be a fourth round.\n")
    
    global userScore
    global computerScore

    def printScore():
        print(f"The score is Player: {userScore} and Computer: {computerScore}")

    def getCompTurn():
        computerTurn = random.randint(1,3)
        return computerTurn 

    def calculate(user, computer):
        global userScore
        global computerScore
#For Rock
        if user == 1 and computer == 2:
            computerScore +=1
            print("Computer beat your Rock with Paper!")
            printScore()
        elif user == 1 and computer == 3:
            userScore +=1
            print("You beat computer's Scissors with a Rock!")
            printScore()
        elif user == 1 and computer == 1:
            print("You both picked Rocks!")
            printScore()
#For Paper        
        if user == 2 and computer == 3:
            computerScore +=1
            print("Computer beat your Paper with Scissors!")
            printScore()
        elif user == 2 and computer == 1:
            userScore +=1
            print("You beat computer's Rock  with Paper!")
            printScore()
        elif user == 2 and computer == 2:
            print("You both picked Paper!")
            printScore()
#For Scissors        
        if user == 3 and computer == 1:
            computerScore +=1
            print("Computer beat your Scissors with a Rock!")
            printScore()
        elif user == 3 and computer == 2:
            userScore +=1
            print("You beat computer's Paper with Scissors!")
            printScore()
        elif user == 3 and computer == 3:
            print("You both picked Scissors!")
            printScore()

#Inputs
    userFirst = int(input("Round 1: Type 1 for Rock, 2 for Paper or 3 for Scissors: "))
    calculate(userFirst, getCompTurn())
    
    userSecond = int(input("\nRound 2: Type 1 for Rock, 2 for Paper or 3 for Scissors: "))
    calculate(userSecond, getCompTurn())

    userThird = int(input("\nRound 3: Type 1 for Rock, 2 for Paper or 3 for Scissors: "))
    calculate(userThird, getCompTurn())

    while userScore == computerScore:
        userInput = int(input("\nTiebreaker: Type 1 for Rock, 2 for Paper or 3 for Scissors: "))
        calculate (userInput, getCompTurn())

    if userScore > computerScore:
        print("\nCongratulations! You won!")
        printScore()
    else:
        print("\nComputer won! You lost!")
        printScore()
#Reset the score
    userScore=0
    computerScore = 0

#Stocks Room function
def stocks():
    print("In this room, you get to check your favorite stock quotes!")

    while True:
        try:
            begin_html = 'https://finance.yahoo.com/quote/'
            userInput = input('\nEnter stock ticker symbol: ')
            end_html = begin_html + userInput
            with closing(get(end_html, stream = True)) as resp:
                html = BeautifulSoup(resp.content, 'html.parser')
                price = html.find('span',{'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
                name = html.find('h1',{'class':'D(ib) Fz(18px)'})
                print(f"\nThe current stock price for {name.text} is: ${price.text}")
        except:
            print("You entered non-existent stock symbol!")
        userInput = input("\nWould you like to enter another stock symbol? Press any key for yes or Q to quit ").lower()
        if userInput == 'q':
            break;


#Riddle function
def riddles():
    global inventory
    score = 0
    print("WELCOME TO THE RIDDLE ROOM!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Get at least 3 questions right and you will win a prize, get less than 3 questions right and you will lose one of the items in your inventory!")
    answer1 = int(input("\nHow many months of the year have 28 days? "))
    if answer1 == 12:
        print("That is correct! ")
        score +=1
    else: 
        print("You got this one wrong! ")
        print("The answer is 12. All months have 28 days in them")
        score -= 1
    print(f"You current score is: {score}")
    answer2 = int(input("\nWhen Grant was 8, his brother was half his age. Now, Grant is 14. How old is his brother? "))
    if answer2 == 10:
        print("You are right!")
        score +=1
    else: 
        print("Wrong! Better learn how to count")
        print("His brother is 10. Half of 8 is 4, so Grant’s brother is 4 years younger. This means when Grant is 14, his brother is still 4 years younger, so he’s 10.")
        score -=1
    print(f"Your current score is {score}")
    answer3 = int(input("\nYou’re running a race and at the very end, you pass the person in 2nd place. What place did you finish the race in? Type just a number.  "))
    if answer3 == 2:
        print("Good Job!!")
        score +=1
    else: 
        print("Got this one wrong!")
        print("If you pass a person in 2nd place, you are now in 2nd place")
        score -=1
    print(f"Your curent score is {score}")
    answer4 = int(input("\nIf two is company and three is a crowd, what are four and five? "))
    if answer4 == 9:
        print("You are absolutely right!")
        score +=1
    else:
        print("Got you! The Answer is 9")
        score -=1
    print(f"Your current score is {score}")
    answer5 = int(input("\nI am an odd number; take away an alphabet and I become even. What number am I ?"))
    if answer5 == 7:
        print("Yes! You are right!")
        score += 1
    else:
        print("This is elementary!")
        print("The answer is: 7 (SEVEN-S=EVEN)")
    print(f"\nYour final score is {score}")
    if score >= 3:
        print("Congratulations! Your prize is a magic riddle  shield!!!")
        inventory.append('shield')
    else: 
        if not inventory:
            print("You bum, you have nothing to take!")
        else:
            print(f"You lost: {inventory[-1]}")
            inventory.pop()

#Dragon Room
def dragon():
    if 'shield' in inventory:
        print("\nYou enter the room, there is a dragon looking at you, you are looking at the dragon. \nThe dragon doesn't like when people stare at him... \nIt breathes FIRE... and.... YOU BLOCKED IT WITH YOUR MAGIC SHIELD!!! \nThe dragon was not ready for that, got confused and flew away.")
    else:
        print("\nDragon: 'Well, would you look at that, dinner just came in. \nYou are a little early. \nI just recently ate, but don't let that fool you... \nI'll fry you anyway and just eat you later.' \nDragon breathes fire... AND YOU ARE FRIED!!! \nGame over!  ")
        exit()


#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  ## Start riddles
  if currentRoom == 'Riddle Room':
      riddles()
  
  #Start battle
  if currentRoom == 'Battle Room':
      battle()
  #Stocks
  if currentRoom == 'Stocks Room':
      stocks()
  ##Dragon Room
  if currentRoom == 'Dragon Room':
      dragon()
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  
  ## If a player enters a room with a monster BUT HAS A COOKIE
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
    print('The monster takes your cookie and runs away! Whew!')
    del rooms[currentRoom]['item']
    inventory.remove('cookie')

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

