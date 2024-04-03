from random import randint

def greet():
    name = input("What is your name? ")
    if (name == "Leo"):
        print("That's my name too!")
    else:
        print("Hello ", name)

def numberGame():
    #choose a random number
    #between 1  & 100
    number = randint(1, 100)
    greet()
    print("I'm thinking of a number between 1 & 100.")
    guess = int(input("Can you guess what it is? "))
    while guess:
        if number == guess:
            print("That's right! It's ", number)
            break
        elif number > guess:
            print("Nope. Higher.")
        else:
            print("Nope. Lower.")
        guess = int(input("What's your guess? "))

numberGame()
