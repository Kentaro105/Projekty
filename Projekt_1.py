"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Keltner
email: dawekeltner71@gmail.com
discord: davidk8500
"""
users = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user = input("Username: ")
password = input("Password: ")

if user not in users:
    print("unregistered user, terminating the program..")
    exit()
elif users[user] != password:
    print("incorrect password, terminating the program..")
    exit()    
print("----------------------------------------")

print(f"Welcome to the app {user}")
print("We have 3 texts to be analyzed")
text_selection = input("Enter a number btw. 1 and 3 to select: ")
if int(text_selection) not in list(range(1,4)):
    print("Wrong text number selected, terminating the programm...")
    exit()
print("----------------------------------------")

text_selected = TEXTS[int(text_selection)-1]
words = text_selected.split()

word_count = len(words)
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
numeric_sum = 0
word_length = {}

for word in words: 
    if word.istitle():
        titlecase_count += 1
    elif word.isupper():
        uppercase_count += 1
    elif word.islower():
        lowercase_count += 1
    elif word.isnumeric():
        numeric_count += 1
        numeric_sum += int(word)
    word = word.rstrip(",.")
    word_length[len(word)] = word_length.get(len(word),0)+1  

# print stats

print(f"There are {len(words)} words in the selected text")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("----------------------------------------")

header_format = "{:<4}|{:<20}|{:<10}"
row_format = "{:<4}|{:<20}|{:<10}"

print(header_format.format("LEN", "OCCURENCES", "NR."))
for lenght, count in sorted(word_length.items()):
    print(row_format.format(lenght, '*'*count, count))  
