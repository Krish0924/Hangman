word = "hello"
bodyPartsLost = 0

def display(letters):
    amount = ["_" for _ in range(5)]
    
    for l in letters:
        if l in word:
            for i in range(len(word)):
                if l == word[i]:
                    amount[i] = l

    print(amount)

letters = []

while bodyPartsLost <= 7:
    print("try to figure out this word!")
    letter = input("type a letter: ")
    letters.append(letter)
    display(letters)
    print("you have lost zero body parts out of seven")