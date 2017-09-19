import random

def menu():
    """The main user interaction window"""
    while(True):
        display_main_menu()
        choice = int(input('Welcome to the Stock Game! \n Enter your choice: '))
        if(choice == 0):
            print("This game is a simplified simulation of how stocks work in the 'real world'. You have a 1000 dollars"
                  "\nand 30 days to make as much money as possible. Invest and sell your stocks wisely, as every day the stocks"
                  "\nwill move up and down at random. Good luck!!")
            menu()
        elif(choice == 1):
            runGame()
        elif (choice == 2):
            print("This game was made by Michael Hendrick, an undergraduate at Boston University in the Fall of 2017.")
            menu()
        elif (choice == 3):
            return "Goodbye!"
        print()

def display_main_menu():
    """ prints a menu of options
    """
    print()
    print('(0) See Instructions')
    print('(1) Begin Game')
    print('(2) Credits')
    print('(3) Quit')
    print()

class player:
    """Creates the player object"""
    def __init__(self, money, name):
        self.name = name
        self.money = money
        self.stockInTechCo = 0
        self.stockInCheapBuy = 0
        self.stockInMcTaco = 0

class company(player):
    """Creates the company object"""
    def startingMoney(self):
        self.money = str(random.randint(100, 1000))

    def stockMovement(self):
        """Causes the stocks to move up and down randomly"""
        amountOfMovement = random.randint(20, 50)
        helperInt = random.randint(0,10)
        moneyAttribute = int(self.money)
        if (helperInt % 2 == 0 ):
            moneyAttribute = moneyAttribute + amountOfMovement
            self.money = str(moneyAttribute)
        else:
            moneyAttribute = moneyAttribute - amountOfMovement
            self.money = str(moneyAttribute)

def runGame():
    """The function that runs the game itself"""
    dayCounter = 1
    techCo = company("100", "TechCo")
    cheapBuy = company("100", "CheapBuy")
    mcTaco = company("100", "McTaco")
    techCo.startingMoney()
    cheapBuy.startingMoney()
    mcTaco.startingMoney()
    name = str(input("What is your name?"))
    user = player("1000", name)
    print("It's a new day, " + user.name + "!")
    while (dayCounter < 3):
        gameMenu()
        turn = int(input("Today is Day " + str(dayCounter) + ". What would you like to do?"))
        print()
        if (turn == 0):
            print("You have " + user.money + " dollars")
        elif (turn == 1):
            seePrices(techCo, cheapBuy, mcTaco)
        elif (turn == 2):
            print("You have " + user.money + " dollars in your bank account.")
            allocateFunds(user,techCo, cheapBuy, mcTaco)
            dayCounter += 1
            techCo.stockMovement()
            cheapBuy.stockMovement()
            mcTaco.stockMovement()
            print("Day advancing...")
            print()
            print("It's a new day!")
        elif (turn == 3):
            print("These are your stocks: \n")
            print("TechCo: " + str(user.stockInTechCo))
            print("CheapBuy: " + str(user.stockInCheapBuy))
            print("McTaco: " + str(user.stockInMcTaco))
        elif (turn == 4):
            dayCounter += 1
            techCo.stockMovement()
            cheapBuy.stockMovement()
            mcTaco.stockMovement()
            print("Day advancing...")
            print()
            print("It's a new day, " + user.name + "!")
    endGame(user,techCo,cheapBuy,mcTaco)

def endGame(user,techCo,cheapBuy,mcTaco):
    """Handles the end game logic"""
    print()
    print("You made " + str(int(user.money) - 1000) + " dollars over the course of 30 days!")
    listOfCompanyMoney = [techCo.money, cheapBuy.money, mcTaco.money]
    listOfCompanyMoney = list(map(int, listOfCompanyMoney))
    lengthOfCompanyMoneyList = len(listOfCompanyMoney) - 1
    resultOfMostMoney = mostProfitableCompanyRecursion(listOfCompanyMoney, lengthOfCompanyMoneyList)
    print("The company that finished with the most money was " + mostProfitbaleCompanyName(resultOfMostMoney, techCo, cheapBuy))
    print("(1) Yes")
    print("(2) No")
    replay = int(input("Would you like to play again?"))
    if(replay == 1):
        print()
        runGame()
    elif(replay == 2):
        print ("Thanks for playing " + user.name + "!")

def mostProfitableCompanyRecursion(companyList, listIndex):
    """Uses recursion to figure out which company ended with the most money"""
    if (listIndex > 0):
        return max(companyList[listIndex], mostProfitableCompanyRecursion(companyList, listIndex - 1))
    else:
        return companyList[listIndex]

def mostProfitbaleCompanyName(moneyResult, techCo, cheapBuy):
    """Returns the name of the company that ended with the most money"""
    if (moneyResult == techCo.money):
        return "TechCo"
    elif (moneyResult == cheapBuy.money):
        return "CheapBuy"
    else:
        return "mcTaco"

def gameMenu():
    """ prints a menu of options
    """
    print()
    print('(0) See Your Money')
    print("(1) See Today's Prices")
    print('(2) Allocate Funds')
    print('(3) See Your Stocks')
    print('(4) Do nothing and Advance Day')
    print()

def seePrices(techCo, cheapBuy, mcTaco):
    """Shows the current prices of the stocks"""
    print("TechCo is selling at " + techCo.money + "\nCheapBuy is selling at " + cheapBuy.money + "\nMcTaco is selling at " + mcTaco.money)

def allocateFundsMenu():
    """The menu that shows users what things they can do with their money"""
    print()
    print("(0) See Today's Prices")
    print('(1) Buy in TechCo')
    print("(2) Sell in TechCo")
    print('(3) Buy in CheapBuy')
    print('(4) Sell in CheapBuy')
    print('(5) Buy in McTaco')
    print('(6) Sell in McTaco')
    print()


def allocateFunds(user,techCo, cheapBuy, mcTaco):
    """The function that allows users to buy or sell thier stocks"""
    allocateFundsMenu()
    holdTrue = user.money
    while (holdTrue == user.money):
        decision = int(input("What are you going to do?"))
        if(decision == 0):
            seePrices(techCo, cheapBuy, mcTaco)
        elif(decision == 1):
            companyMoney = int(techCo.money)
            if (int(user.money) - companyMoney < 0):
                print("You don't have enough money!")
                allocateFunds(user, techCo, cheapBuy, mcTaco)
                print()
            else:
                user.money = str(int(user.money) - companyMoney)
                user.stockInTechCo += 1
        elif (decision == 2):
            if(user.stockInTechCo <= 0):
                print("You can't sell if you don't own any stocks!")
                allocateFunds(user, techCo,cheapBuy, mcTaco)
                print()
            else:
                companyMoney = int(techCo.money)
                user.money = str(int(user.money) + companyMoney)
                user.stockInTechCo -= 1
        elif (decision == 3):
            companyMoney = int(cheapBuy.money)
            if (int(user.money) - companyMoney < 0):
                print("You don't have enough money!")
                allocateFunds(user, techCo, cheapBuy, mcTaco)
                print()
            else:
                user.money = str(int(user.money) - companyMoney)
                user.stockInCheapBuy += 1
        elif (decision == 4):
            if (user.stockInCheapBuy <= 0):
                print("You can't sell if you don't own any stocks!")
                allocateFunds(user, techCo, cheapBuy, mcTaco)
                print()
            else:
                companyMoney = int(cheapBuy.money)
                user.money = str(int(user.money) + companyMoney)
                user.stockInCheapBuy -= 1
        elif (decision == 5):
            companyMoney = int(mcTaco.money)
            if (int(user.money) - companyMoney < 0):
                print("You don't have enough money!")
                allocateFunds(user, techCo, cheapBuy, mcTaco)
                print()
            else:
                user.money = str(int(user.money) - companyMoney)
                user.stockInMcTaco += 1
        elif (decision == 6):
            if (user.stockInMcTaco <= 0):
                print("You can't sell if you don't own any stocks!")
                allocateFunds(user, techCo, cheapBuy, mcTaco)
                print()
            else:
                companyMoney = int(mcTaco.money)
                user.money = str(int(user.money) + companyMoney)
                user.stockInMcTaco -= 1


menu()