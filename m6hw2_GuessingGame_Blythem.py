#Michael Blythe
#M6HW2
#CTI-110
#11/12/17
#
#

#main fuction that will first greet the user
def main():
    print('Guess the correct number between 1 and 100')
    print()
    #calls the program to the play_game fuction
    play_game()
    #once the correct number is found, you are redirected to this message
    
    playAgain = input('Would you like to play again? (y / n)')
    #if / else statment to determine if the program should run again or exit
    if playAgain == 'y':
         main()
    else:
        print('Thanks for playing!')
        exit()

        
def play_game():
    #imports random number
    import random
    #sets range of random number
    randomNumber = random.randint(1,100)
    #stores user guess as variable userGuess
    userGuess = int(input('Enter a number:'))

    #while loop to cause the game to run until the user guess matches
    while userGuess != randomNumber:
        if userGuess > randomNumber:
            print('Guess lower!')
            userGuess = int(input('Enter a number:'))
        elif userGuess < randomNumber:
            print('Guess higher!')
            userGuess = int(input('Enter a number:'))
    #upon completing the while loop, you are congratulated with this message      
    print('You guessed correctly!')
    print()

main()
