secret_word = "sean"
Guess = ""
guesscount= 0
guesslimit= 3
outofguess = False
while Guess != secret_word and not(outofguess):
    if guesscount < guesslimit:
        Guess = input("Enter guess: ")
        guesscount += 1
else:
    outofguess = True

print("You win!")
