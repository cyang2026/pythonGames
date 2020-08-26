import random
print("Welcome to this game! This is a number guessing game.")
print("You can decide the range of this game!")
while(True):
    print("Enter the maximum number that can be selected.")
    maxNum = int(input())
    print("Now enter the minimum number that can be selected.")
    minNum = int(input())
    if maxNum > minNum:
        break
    else:
        print("Please pick a maximum number that is larger than the minimum number.")
highScores = []
def playerGuess(num):
    guess = int(input())
    if guess == num:
        print("Congratulations!")
        return True
    if guess < num:
        print("The guess is too small.")
    if guess > num:
        print("The guess is too large.")

def playGame(num):
    print("Enter a number between " + str(minNum) + " and " + str(maxNum) + "!")
    attempts = 0
    gamesPlayed = 0
    while(True):
        if playerGuess(num):
            attempts += 1
            highScores.append(attempts)
            highScores.reverse()
            print("You're best score is " + str(highScores[0]))
            gamesPlayed += 1
            print("You've played " + str(gamesPlayed) + " game(s) so far.")
            print("Would you like to play another game?")
            while(True):
                answer = input()
                if answer == 'yes':
                    playGame(random.randint(minNum, maxNum))
                    break
                if answer == 'no':
                    print("Thanks for playing!")
                    break
                else:
                    print("Please answer with yes or no.")
            break
        elif attempts == 9:
            print("You have failed! Try again to get a sub 10 attempt score!")
            break
        else:
            attempts += 1
            print("Attempts: " + str(attempts))
playGame(random.randint(minNum, maxNum))

