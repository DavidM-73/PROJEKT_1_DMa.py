'''
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: David Marek
email: David.32@seznam.cz
discord: David M.#7065
"""
import ...
author =
'''
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

########################################################
import re

users = ("bob", "ann" , "nike", "liz", "Radim")
paswords = ("123", "pass123", "password123", "pass123", "666")
separator = "-" * 60
stars = "*"
poradi_textu = [1, 2, 3]

text = dict(zip(poradi_textu, TEXTS))

print(separator)
print(
     "$ python projekt1.py"
     )
jmeno = input('Enter your username: ')
heslo = input('Now the password: ')
print(separator)

prihlasovaci_udaje = dict(zip(users,paswords))

if not jmeno in prihlasovaci_udaje or prihlasovaci_udaje[jmeno] != heslo:
    print('Unregistered user, terminating the program..')
    print()
    quit()
else:
    print('Welcome to the app,',jmeno)
    print('We have 3 texts to be analyzed.')
    print(separator)

zadani_textu = int(input('Enter a number btw. 1 and 3 to select: '))
print(separator)

if 1 <= zadani_textu <= 3:
    zadany_text = text[zadani_textu]

    vycistena_slova = []
    for slovo in zadany_text.split(): 
        ciste_slovo = slovo.strip(".,!?") 
        vycistena_slova.append(ciste_slovo)

    pocet_slov = len(vycistena_slova)
    print(f"There are {pocet_slov} words in the selected text.")

    s_velkym = 0
    for upper in vycistena_slova:
        if(upper[0].isupper()):
            s_velkym += 1
    print(f'There are {s_velkym} titlecase words.')

    slova = re.findall(r'\b[A-Z]+\b', zadany_text)
    jen_velke = 0
    for slovo in slova:    
             jen_velke += 1
    print(f'There are {jen_velke} uppercase words.')

    jen_male = 0
    for lower in vycistena_slova:
        if(lower[0].islower()):
            jen_male += 1
    print(f'There are {jen_male} lowercase words.')

    regex = r'\b\d+\b'
    pocet_cisel = 0
    for match in re.findall(regex, zadany_text):
        if match.isdigit():
            pocet_cisel += 1
    print(f'There are {pocet_cisel} numeric strings.')

    cisla = re.findall(regex, zadany_text)
    soucet_cisel = 0
    for cislo in cisla:
        try:
             soucet_cisel += int(cislo)
        except ValueError:
              pass
    print(f'The sum of all the numbers {soucet_cisel}')

    delka_slova = {}
    for slovo in vycistena_slova:
        delka = len(slovo)
        if delka in delka_slova:
            delka_slova[delka] += 1
        else:
            delka_slova[delka] = 1
else:
    print('The text of the entered number does not exist!')
    quit()

print(separator)
print(("LEN|".rjust(4)),("OCCURENCES".center(18)),("|NR.".ljust(4)))
print(separator)

for delka, pocet in sorted(delka_slova.items()):
      print(f"{str(delka).rjust(3)}| {(stars * pocet).ljust(19)}|{pocet}")

print(separator)
print('Thank you for using our word analyzer.')
print()