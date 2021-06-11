from termcolor import cprint, colored

word = "hello"
bodyPartsLost = 0

def ldetetcion(letter):
    # one character
    # in the alphabet

    if letter.isalpha() and len(letter) == 1:
        return True
    else:
        return False

def display(letters):
    underscores = ["_" for _ in range(5)]
    global bodyPartsLost
    bodyPartsLost = 0

    for l in letters:
        if l in word:
            for i in range(len(word)):
                if l == word[i]:
                    underscores[i] = colored(l, "green")
        else:
            bodyPartsLost += 1

    print(" ".join(underscores))

    if "_" not in underscores:
        print("Congrats you found the word it was " + colored(word, "green") + "!")
        return True
    else:
        return False

letters = []

while bodyPartsLost <= 7:
    print("Try to figure out this word!")
    letter = input("Type a letter: ")
    while not ldetetcion(letter):
        print("That is not a letter. Try again.")
        letter = input("Type a letter: ")
    letters.append(letter)
    hasWon = display(letters)
    if hasWon:
        break
    print("You have lost " + colored(str(bodyPartsLost), "red") + " body parts out of " + colored("7", "green"))

# Possible changes:
    # "you have lost 8 body parts out of 7"
    # Guessing same letter multiple times

    # Make printing of underscores prettier
    # Colors (you can look up termcolor)
    # deal with guesses of multiple letters or no letters or numbers