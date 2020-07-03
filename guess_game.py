#Number guessing program
#Computer will pick a random number between 1 and 20
#User will try to guess it in 6 attempts
# if user guesses number greater than random,then computer will say 'too high'
# if user guesses number lower than random,then computer will say 'too low'

import random

print ('Please enter your name :')
myName = input()
print ('Well '+myName+' i am guessing a number')
secretNumber = random.randint(1,20)

for guessTaken in range (1,7):
    print (myName+' please choose your number')
    guess = input()
    if int(guess) > secretNumber:
        print('Too high')
    elif int(guess) < secretNumber:
        print('Too Low')
    else:
        break

if int(guess) == secretNumber:
    print('Your guess of ' + str(guess)+ ' is correct')
    print('You took '+str(guessTaken)+' chances')
else:
    print('You lose. The number is '+str(secretNumber))
