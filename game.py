import random
text = ""
while True:
    try :
        text = int(input("Level: "))
        if text <= 1: 
            continue
    except (NameError, ValueError):
        continue

    number = random.randrange(1, text)
    break



while True:
    print(number)
    try:
        guess = int(input("Guess: "))
    except (NameError, ValueError):
        continue

    if guess > number:
        print("Too large!")
        continue
    elif guess < number:
        print("Too small")
        continue
    elif guess == number:
        print("Just right!")
        break