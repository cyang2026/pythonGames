import random
print("Welcome to this game! This is a number guessing game.")
print("You can decide the range of this game!")
#Allows the player to choose the range of the game
while(True):
    print("Enter the maximum number that can be selected.")
    maxNum = int(input())
    print("Now enter the minimum number that can be selected.")
    minNum = int(input())
    if maxNum > minNum:
        break
    else:
        print("Please pick a maximum number that is larger than the minimum number.")
#Stores the high scores throughout the game
highScores = []
#Tells the player the accuracy of the guess
def playerGuess(num):
    guess = int(input())
    if guess == num:
        print("Congratulations!")
        return True
    if guess < num:
        print("The guess is too small.")
    if guess > num:
        print("The guess is too large.")
#Allows the player to play the game
def playGame(num):
    print("Enter a number between " + str(minNum) + " and " + str(maxNum) + "!")
    #Stores the attempt counts of the player
    attempts = 0
    while(True):
        if playerGuess(num):
            #This increments every time a player guesses
            attempts += 1
            #This stores the number of attempts that the player made to get the correct answer in this round in the list highScores
            highScores.append(attempts)
            #This sorts the list 
            highScores.sort()
            #This prints out their best score (lowest)
            print("Your best score is " + str(highScores[0]))
            print("Would you like to play another game?")
            #This asks the user if they want to play another game until they answer 'yes' or 'no'
            while(True):
                answer = input()
                if answer == 'yes':
                    #This plays the game again
                    playGame(random.randint(minNum, maxNum))
                    break
                if answer == 'no':
                    #This bresk the loop and thanks the player for playing
                    print("Thanks for playing!")
                    break
                else:
                    #If the player answers with anything other than 'yes' or 'no', this will run
                    print("Please answer with yes or no.")
            break
        else:
            #This also increments every time a player guesses
            attempts += 1
            print("Attempts: " + str(attempts))
#This runs the function playGame()
playGame(random.randint(minNum, maxNum))