import random
class playGame:
    board = [["O","O","X","H","O","p","X","X","F"], ["O","X","X","X","X","O","O","O","F"], ["O","O","O","O","O","X","X","K","F"], ["X","X","X","X","O","O","O","O","F"], ["O","X","O","s","O","X","X","X","F"], ["H","X","O","X","X","X","X","X","F"], ["O","O","O","O","M","O","O","O","F"], ["K","X","X","X","X","X","X","E"]]
    inventory = []
    col = 0
    row = 0
    finishedGame = False
    died = False
    def get_location(self, input_col, input_row):
        location = self.board[input_row][input_col]
        return location
    def restart_player(self):
        self.col = 0
        self.row = 0
        self.inventory.clear()
        self.died = True
    def report_coords(self):
        print("You are currently at row " + str(self.row + 1) + " and column " + str(self.col + 1) + ".")
    def get_inventory(self):
        if len(self.inventory) != 0:
            for item in self.inventory:
                print(item)
        else:
            print("Oh, it looks like you don't have anything in your inventory. That's unfortunate...")
    def north(self):
        if self.row != 0:
            to_north = self.get_location(self.col, (self.row - 1))
            if to_north != "X":
                self.row -= 1
                print("You moved north! Keep exploring, you're not there yet!")
                self.pickUpKey(to_north)
                self.openChest(to_north)
                self.fallInHole(to_north)
                self.fightMonster(to_north)
            else:
                print("Oops, there's a wall there.")
        else:
            print("Oops, that's outside of the maze.")
    def south(self):
        if self.row != 7:
            to_south = self.get_location(self.col, (self.row + 1))
            if to_south != "X":
                self.row += 1
                print("You moved south! Keep exploring, you're not there yet!")
                self.pickUpKey(to_south)
                self.openChest(to_south)
                self.fallInHole(to_south)
                self.fightMonster(to_south)
                self.checkFinished(to_south)
            else:
                print("Oops, there's a wall there.")
        else:
            print("Oops, that's outside of the maze.")
    def west(self):
        if self.col != 0:
            to_west = self.get_location((self.col - 1), self.row)
            if to_west != "X":
                self.col -= 1
                print("You moved west! Keep exploring, you're not there yet!")
                self.pickUpKey(to_west)
                self.openChest(to_west)
                self.fallInHole(to_west)
                self.fightMonster(to_west)
            else:
                print("Oops, there's a wall there.")
        else:
            print("Oops, that's outside of the maze.")
    def east(self):
        if self.col != 7:
            to_east = self.get_location((self.col + 1), self.row)
            if to_east != "X":
                self.col += 1
                print("You moved east! Keep exploring, you're not there yet!")
                self.pickUpKey(to_east)
                self.openChest(to_east)
                self.fallInHole(to_east)
                self.fightMonster(to_east)
            else:
                print("Oops, there's a wall there.")
        else:
            print("Oops, that's outside of the maze.")
    def pickUpKey(self, direction):
        if direction == "K":
            print("Oh look! It's a key!")
            print("Let's pick it up and put it in our inventory. We might need this later!")
            self.inventory.append("Key")
    def openChest(self, direction):
        if direction == "s":
            print("Oh? What's this?")
            print("It's a chest! Let's see...")
            print("You'll need a key to open this. Let's look in our inventory...")
            if "Key" in self.inventory:
                print("Brilliant! You have a key!")
                print("Okay, let's open this up...")
                print("A sword! That's great! We might need this for later, so let's put it in our inventory.")
                self.inventory.append("Sword")
                self.board[4][3] = "O"
            else:
                print("Oh no! You don't have a key.")
                print("Oh well, we'll leave this here and come back later, then.")
        elif direction == "p":
            print("Oh? What's this?")
            print("It's a chest! Let's see...")
            print("You'll need a key to open this. Let's look in our inventory...")
            if "Key" in self.inventory:
                print("Brilliant! You have a key!")
                print("Okay, let's open this up...")
                print("A sword! That's great! We might need this for later, so let's put it in our inventory.")
                self.inventory.append("Potion")
                self.board[0][5] = "O"
            else:
                print("Oh no! You don't have a key.")
                print("Oh well, we'll leave this here and come back later, then.")
    def fallInHole(self, direction):
        if direction == "H":
            print("Oh no! You fell in a hole!")
            print("Guess you have to restart, then...")
            self.restart_player()
    def fightMonster(self, direction):
        if direction == "M":
            print("Oh no! There's a monster here!")
            print("Quick, let's look in our inventory, is there anything in here that'll help?")
            if "Sword" in self.inventory and "Potion" in self.inventory:
                print("Oh, thank goodness, you've got a sword AND a potion.")
                print("This'll be a huge asset. Anyways, let's go and tackle that monster!")
                print("Good job! You've defeated the monster!")
                self.board[6][4] = "O"
            elif "Sword" in self.inventory:
                print("Okay, you've got a sword in your inventory.")
                print("That will be extremely helpful. Anyways, let's go and tackle that monster!")
                print("Good job! You've defeated the monster!")
            elif "Potion" in self.inventory:
                print("Okay, you've got a potion in your inventory.")
                print("That will be extremely helpful. Anyways, let's go and tackle that monster!")
                print("Good job! You've defeated the monster!")
            else:
                print("Oh no, you don't have anything helpful in your inventory.")
                print("I guess we'll just have to take our chances, then.")
                print("Good luck!")
                probability = random.randint(0, 10)
                if probability >= 8:
                    print("You got really lucky! You managed to defeat the monster with your bare hands!")
                    print("Congratulations! Now you can continue on your journey through the maze.")
                else:
                    print("Oh no! The monster defeated you!")
                    print("It's okay, it wasn't likely that you would survive, anyway.")
                    print("But you've got to restart now.")
                    self.restart_player()
    def checkFinished(self, direction):
        if direction == "E":
            print("Congratulations! You've finished the maze!")
            self.finishedGame = True
    def flashlightNorth(self):
        if self.row != 0:
            to_north = self.board[self.row - 1][self.col]
            if to_north == "H":
                print("To the north is a gaping hole. Best not to go there...")
            elif to_north == "K":
                print("To the north you can see a faint glimmer of... is that copper? Check it out!")
            elif to_north == "p":
                print("To the north you can see a faint outline of a small box. What's that?")
            elif to_north == "O":
                print("To the north lies an open path.")
            elif to_north == "X":
                print("To the north lies a wall of the maze. Try a different direction!")
        else:
            print("To the north lies the outer wall of the maze.")
    def flashlightSouth(self):
        if self.row != 7:
            to_south = self.board[self.row + 1][self.col]
            if to_south == "K":
                print("To the south you can see a faint glimmer of... is that copper? Check it out!")
            elif to_south == "O":
                print("To the south lies an open path.")
            elif to_south == "X":
                print("To the south lies a wall of the maze. Try a different direction!")
        else:
            print("To the south lies the outer wall of the maze.")
    def flashlightEast(self):
        if self.col != 7:
            to_east = self.board[self.row][self.col + 1]
            if to_east == "s" or to_east == "p":
                print("To the east you can see a faint outline of a small box. What's that?")
            elif to_east == "X":
                print("To the east lies a wall of the maze. Try a different direction!")
            elif to_east == "O":
                print("To the east lies an open path.")
            elif to_east == "M":
                print("To the east, you can hear a quiet growl and ominous shuffling of... is that feet? You've got to check that out...")
        else:
            print("To the south lies the outer wall of the maze.")
    def flashlightWest(self):
        if self.col != 0:
            to_west = self.board[self.row][self.col - 1]
            if to_west == "s":
                print("To the west you can see the faint outline of a small box. What's that?")
            elif to_west == "H":
                print("To the west is a gaping hole. Best not to go there...")
            elif to_west == "X":
                print("To the west lies a wall of the maze. Try a different direction!")
            elif to_west == "O":
                print("To the west lies an open path.")
        else:
            print("To the west lies the outer wall of the maze.")
    def teleport(self, to_row, to_col):
        self.row = to_row - 1
        self.col = to_col - 1

#Creating an instance
myGame = playGame()

#Actually playing the game
print("Welcome to this maze game! You can get started by entering any direction, or if you want a full list of commands, enter help. Your objective is to make it to the end of the maze, which is located at the coordinates 8, 8. Good luck!")
while(True):
    if myGame.died == True or myGame.finishedGame == True:
        break
    command = input()
    if command == "north":
        myGame.north()
    elif command == "south":
        myGame.south()
    elif command == "west":
        myGame.west()
    elif command == "east":
        myGame.east()
    elif command == "look north":
        myGame.flashlightNorth()
    elif command == "look south":
        myGame.flashlightSouth()
    elif command == "look west":
        myGame.flashlightWest()
    elif command == "look east":
        myGame.flashlightEast()
    elif command == "help":
        print("Type:")
        print("north/south/east/west - move in that direction")
        print("look north/south/east/west - look in that direction")
        print("exit - exit the game")
        print("get inventory - look in your inventory")
        print("coordinates - get your current coordinates")
    elif command == "exit":
        print("Thanks for playing!")
        break
    elif command == "get inventory":
        myGame.get_inventory()
    elif command == "coordinates":
        myGame.report_coords()
    elif command == "teleport":
        print("Enter the row:")
        tele_row = input()
        print("Enter the column:")
        tele_col = input()
        myGame.teleport(int(tele_row), int(tele_col))
    else:
        print("404: Command Not Found.")
        print("We can't seem to find the command you're looking for.")
        print("Please wait a couple of minutes and try again later.")
        print("if the issue persists, please contact support.")