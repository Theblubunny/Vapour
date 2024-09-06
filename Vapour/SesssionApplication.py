from Entity.Misc import account
from Entity.Misc import game
from Entity.Misc import AGJ
import random

from Entity.DatabaseConnection import DatabaseConnection

def startup_menu():
    print('------------------')
    print("Welcome to Steam!")
    print("1. Log in")
    print("2. Sign up")
    print("3. Forgot my ID!")
    print("4. Exit")

def menu(accName):
    print("\n------------------")
    print("Currently logged into: " + accName)
    print("What would you like to do?")
    print("1. Buy a Game")
    print("2. Play a Game")
    print("3. Publish a Game")
    print("4. My Games")
    print("5. My Account")
    print("6. Log Out")


def main():

    startUpInput = 0  # default value for user input
    dbcon = DatabaseConnection() # create a DatabaseConnection object that will get passed around
    acc = account(dbcon)  # this is the current Account object
    agj = AGJ(dbcon)
    g = game(dbcon)
    accName = ""
    accID = 0

    while(startUpInput != 4):

        startup_menu()
        startUpInput = int(input("Enter selection: "))

        if(startUpInput == 1):

            menuInput = 0
            ID = int(input("Enter Account ID: "))
            acc.findByID(ID)
            accName = acc.getName()
            accID = acc.getacc_id()

            while(menuInput != 6): # After logging in, all the other stuff happens
               
                menu(accName)
                menuInput = int(input("\nEnter selection: "))

                if(menuInput == 1):
                    
                    print("Welcome to the Steam Store!!!")
                    allgame = g.findAll()
                    for xgame in allgame:
                        print('------------------")')
                        print('ID: ', xgame.getgame_id(), '\nName: ', xgame.getName(), '\nCost: ', xgame.getCost(),
                              '\nDeveloper: ', xgame.getDev(), '\nPublisher: ', xgame.getPub(), '\nRating: ', xgame.getRating(),
                                '\nGenre: ', xgame.getGenreOne(), ', ', xgame.getGenreTwo(), ', ', xgame.getGenreThree(),
                                '\nAchievements: ', xgame.getTotalAchievements(), '\nDescription: ', xgame.getDescription()
                              )
                    print('------------------')
                    gameID = int(input("Which game would you like to buy?: "))    
                    agj.buyGame(accID, gameID)
                    print('Thank you for your purchase!')

                elif(menuInput == 2):
                    
                    agj.printLite(accID)
                    gameID = int(input("Which game would you like to play?: "))    
                    hours = int(input("How many hours would you like to play: "))
                    agj.increaseHour(accID, gameID, hours)
                    print('You played for ' + str(hours) + ' hours!')

                    # math for achievements
                    achMath = round(hours * 0.4)
                    agj.achievementGet(accID, gameID, achMath)
                
                elif(menuInput == 3):
                    n = input('Enter a name for your game: ')
                    c = float(input('Enter the cost of your game: '))
                    g.printDevs()
                    d = int(input('Who developed the game?: '))
                    g.printPubs()
                    p = int(input('Who published the game?: '))
                    g.printGenre()
                    ge1 = int(input('Choose the first genre of your game: '))
                    ge2 = int(input('Choose the second genre of your game: '))
                    ge3 = int(input('Choose the third genre of your game: '))
                    a = int(input('How many achievements does your game have?: '))
                    de = input('Write a short description for the game: ')

                    gme = game(dbcon)
                    gme.setName(n)
                    gme.setCost(c)
                    gme.setDev(d)
                    gme.setPub(p)
                    gme.setRating(random.randint(1, 7))
                    gme.setGenreOne(ge1)
                    gme.setGenreTwo(ge2)
                    gme.setGenreThree(ge3)
                    gme.setTotalAchievements(a)
                    gme.setDescription(de)
                    gme.insert()

                    print('Game Created!')

                elif(menuInput == 4):
                    agj.printOwnedGames(accID)     

                elif(menuInput == 5):
                    agj.printStats(accID)
                
        elif(startUpInput == 2):

            newName = input("Enter a name for your account: ")
            acc = account(dbcon)
            acc.setName(newName)
            acc.insert()

            print('Account Created!')

        elif(startUpInput == 3):

            print("Account List: ")
            allacc = acc.findAll()
            for xacc in allacc:
                print('(ID:)', xacc.getacc_id(), '(Name:)', xacc.getName(), '(Level:)',
                xacc.getLevel())

main()