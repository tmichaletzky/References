import random

print('Enter a number from 20 to 100')
top=int(input())

secretNumber = random.randint(1,top)
#print(secretNumber)

totalGuess = 6
askedNumber = 0
solved = False

print('Hello to my new mindblowing game.')
print('Your aim is to guess the number I have thought in range 1 to ' + str(top) + '.')
print('Careful! To do this, you can ask ' + str(totalGuess) + ' questions only!')
print("Are you ready for the game? Then let's begin!")

print('\nHow can I call you? (If I were you, I would call me Bitch.)')
name = input()
Boo = False
      
if name == 'Bitch' or name == 'bitch':
    Boo = True
    totalGuess = totalGuess + 2
    print('Congrats, ' + name + '! You got 2 extra guesses!')
    print('That means, you have a total of ' + str(totalGuess) + ' guesses overall.')
    print('\nAnyways: bjiiiiiiiiiiiiics')
else:
    print('Well, hello ' + name + '!')


for i in range(0,totalGuess):
    print('\nTake a guess from 1 to ' + str(top) +  '! You have ' + str(totalGuess - askedNumber) + ' guesses left.')
    guess = int(input())
    askedNumber = askedNumber + 1

    if guess > secretNumber:
        print('No, that is too high.') 
    elif guess < secretNumber:
        print('No, that is too low.') 
    else:
        print('Correct, you are reading my mind! You solved it in ' + str(askedNumber) + ' steps.')
        solved = True
        break

if solved:
    print('That is extraordinary!')
else:
    print('\nSorry, you reached your limit, you have not guessed it in ' + str(totalGuess) + ' steps. \n Try again later!')
    print('The number was ' + str(secretNumber) + '.')
      
print('\nBye, ' + name + ', thank you for playing with me! \n If you want play again, click Run again.')
