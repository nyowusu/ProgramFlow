import random

highest = 10
play = ['yes', 'Yes', 'y', 'Y']
# guess = int(input("Guess a number between 1 and {} ".format(highest).strip()))
guessAgain = 'y'
numGuess = 0

# while guess != answer:
#     if guess > answer:
#         guess = int(input("Guess lower than {} ".format(guess).strip()))
#     else:
#         guess = int(input("Guess higher than {} ".format(guess).strip()))
# else:
#     print("Well done! You got it! ")

while guessAgain in play:
    answer = random.randint(1, highest)
    numGuess = 0
    print(answer)
    guess = int(input("Guess a number between 1 and {} ".format(highest).strip()))

    if guess == answer:
        print("Well done! You guessed it the first time! ")
    else:
        numGuess += 1
        while guess != answer:
            if guess > answer:
                guess = int(input("Guess lower than {} ".format(guess).strip()))
            elif guess < answer:
                guess = int(input("Guess higher than {} ".format(guess).strip()))
            numGuess += 1

        print("Well done! You guessed it after {} try(ies) ".format(numGuess))

    guessAgain = input("Do you want to guess a different number? y/n ")
