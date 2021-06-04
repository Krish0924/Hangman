word = "hello"
bodyPartsLost = 0

def display(letter):
    amount = ["_" for _ in range(5)]
    
    print(amount)
    if letter in word:
        index = word.index(letter)
        amount[index] = letter
        print(amount)
        

while bodyPartsLost <= 7:
    print("try to figure out this word!")
    letter = input("type a letter: ")
    display(letter)
    print("you have lost zero body parts out of seven")