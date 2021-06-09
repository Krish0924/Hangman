word = "hello"
bodyPartsLost = 0
 
def display(letters):
    underscores = ["_" for _ in range(5)]
    global bodyPartsLost
    bodyPartsLost = 0

    for l in letters:
        if l in word:
            for i in range(len(word)):
                if l == word[i]:
                    underscores[i] = l
        else:
            bodyPartsLost += 1


    if "_" not in underscores:
        print("congrats you found the word it was " + word + "!")
        return True
    else:
        print(underscores)
        return False

    

letters = []

while bodyPartsLost <= 7:
    print("try to figure out this word!")
    letter = input("type a letter: ")
    letters.append(letter)
    hasWon = display(letters)
    if hasWon:
        break
    print("you have lost " + str(bodyPartsLost) + " body parts out of 7")