"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie "Bulls and Cows"
author: David Keltner
email: dawekeltner71@gmail.com
discord: davidk8500
"""

import random



print(
"""Hi there!
--------------------------------------------------------------------------------------------------------------
Let's play a bulls and cows game.
--------------------------------------------------------------------------------------------------------------
Lets look quickly at the rules:
I've generated a random 4 digit number for you. You need to guess value and position of all 4 digits correctly
To guess all number you enter have to enter 4 digit number where first digit cannot be 0
Once you enter your number you will receive Bulls and Cows score where:
Bulls point = exact match of digit (position&value)
Cows point = partial match (value only, wrong possition)
Goal is to get 4 Bulls in as less guesses as possible!!
--------------------------------------------------------------------------------------------------------------
Let's play a bulls and cows game.
--------------------------------------------------------------------------------------------------------------
""")

# Vygenerovat unikátní číslo
number = random.sample(range(10), 4)
if number[0] == 0:  # První cifra nemůže být 0
    number[0] = random.randint(1, 9)

number = ''.join(map(str, number))
print(number)


pokusy = []

while True:
    if pokusy:
        print("Your previous guesses:")
        for i, (guess, bulls, cows) in enumerate(pokusy, 1):
            print(f"{i}. {guess}: {bulls} Bulls, {cows} Cows")# Zapsat pokus od hráče, pokud není "pokusy" prázdný
            

    guess = input("Enter your number: ")

    # Kontrola délky čísla
    if len(guess) != 4:
        print("Please enter a 4-digit number.")
        continue

    # Kontrola jedinečnosti čísel
    if len(set(guess)) != 4:
        print("All digits must be unique.")
        continue

    bulls = 0
    cows = 0

    # Vyhodnocení pokusu
    for i in range(4):
        if guess[i] in number:
            cows += 1
        if guess[i] == number[i]:
            bulls += 1
            cows -= 1
    pokusy.append((guess, bulls, cows))

    print(f"{bulls} Bulls, {cows} Cows")

    # Konec hry
    if bulls == 4:
        if len(pokusy) < 5 :
            zaverecna_zprava = "You are real pro in this game!"
        elif len(pokusy) > 5 and len(pokusy) < 10:
            zaverecna_zprava = "This is very good result but still can be better!"
        else:
            zaverecna_zprava = "There is still lot of space for improvement, try it again!"

        print(f"Congratulations, you managed to finished in {len(pokusy)} guesses. {zaverecna_zprava}")
        break
