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
    underscores = ["_" for _ in range(len(word))]
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

letters = set()

stickman = [
    colored(" O", "green") + "\n" + colored("/", "green") + colored("|", "green") + colored("\\", "green") + "\n" + colored("/ ", "green") + colored("\\", "green"),
    colored(" O", "green") + "\n" + colored("/", "green") + colored("|", "green") + colored("\\", "green") + "\n" + colored("/ ", "green") + colored("\\", "red"),
    colored(" O", "green") + "\n" + colored("/", "green") + colored("|", "green") + colored("\\", "green") + "\n" + colored("/ ", "red") + colored("\\", "red"),
    colored(" O", "green") + "\n" + colored("/", "green") + colored("|", "green") + colored("\\", "red") + "\n" + colored("/ ", "red") + colored("\\", "red"),
    colored(" O", "green") + "\n" + colored("/", "green") + colored("|", "red") + colored("\\", "red") + "\n" + colored("/ ", "red") + colored("\\", "red"),
    colored(" O", "green") + "\n" + colored("/", "red") + colored("|", "red") + colored("\\", "red") + "\n" + colored("/ ", "red") + colored("\\", "red"),
    colored(" O", "red") + "\n" + colored("/", "red") + colored("|", "red") + colored("\\", "red") + "\n" + colored("/ ", "red") + colored("\\", "red")
]

while bodyPartsLost < 6:
    print("Try to figure out this word!")
    letter = input("Type a letter: ")
    while not ldetetcion(letter):
        print("That is not a letter. Try again.")
        letter = input("Type a letter: ")
    letters.add(letter)
    hasWon = display(letters)
    if hasWon:
        break
    print(stickman[bodyPartsLost])

#deal with spaces