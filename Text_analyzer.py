"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Skoupil
email: Tskoupil@gmail.com
discord: Palmex [IO]#2698
"""

'''
author = Tomáš Skoupil
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
# Zadání potřebných proměnných
credencials = {"bob" : "123" , 
               "ann" : "pass123" , 
               "mike" : "password123" , 
               "liz" : "pass123"}
username = input("Username: ")
password = input("Password: ")
znak = "*"
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
summary = 0
spliter = ("-") * 45

words_1 = TEXTS[0].split()
words_2 = TEXTS[1].split()
words_3 = TEXTS[2].split()

words_cleared = []
len_occurences = {}
# Pro nalezeni nejdelsiho slova v textu (TEXTS) a finalni upravu grafu 
# (aby znaky "|" na sebe navazovaly)
longest_word_length = 0
for text in TEXTS:
    words = text.split()
    for word in words:
        cleaned_word = word.strip(".,:;")
        if len(cleaned_word) > longest_word_length:
            longest_word_length = len(cleaned_word)
print(spliter)
# Ověření, že uživatel je v databázi a zadal správné heslo. 
# Pokud je vše v pořádku, uživatel je pozdraven a je mu zobrazena nabídka textů.
# Pokud není v databázi, nebo zadal špatné heslo, ukonči program (viz poslední řádek kódu)
if username in credencials and credencials[username] == password:
    print(f"Welcome to the app, {username}!")
    print("We have 3 texts to be analyzed:")
    print(spliter)
    print(f"\n 1. {TEXTS[0]}\n 2. \n{TEXTS[1]}\n 3. \n{TEXTS[2]}\n")

    # Uživatel vybere z možností 1-3.
    print(spliter)
    choice = (input("Enter a number btw. 1 and 3 to select: "))
    print(spliter)
    # Pokud vybere pouze číslo a to v rozmezí 1-3, :
    if choice.isdigit() and 1 <= int(choice) <= 3:
        # Zjištění počtu slov ve vybraném textu:
        selected_text = len(TEXTS[int(choice) - 1].split())
        # Vytvoření slovníku s očištěnými slovy z vybraného textu o interpunkce
        # Vytvoření smyček a proměných pro vyhledání počtu slov, které začínají velkým písmenem,
        # které jsou napsány malým písmem, velkým písmem, počet slov které jsou číslicí a také
        # suma hodnot v zadaném textu
        words_cleared = [word.strip(".,:;") for word in TEXTS[int(choice) - 1].split()]
        for word in words_cleared:
            if word.isupper() and word.isalpha():
                uppercase += 1
            elif word.islower() and word.isalpha():
                lowercase += 1
            elif word.istitle() and word.upper() and word.isalpha():
                titlecase += 1
            elif word.isdigit():
                numeric += 1
                summary += int(word)
            if len(word) not in len_occurences:
                len_occurences[len(word)] = 1
            else:
                len_occurences[len(word)] += 1
        # Výpis informací uživateli o vybraném textu
        print(f"""
There are {selected_text} words in the selected text
There are {titlecase} titlecase words.
There are {uppercase} uppercase words.
There are {lowercase} lowercase words.
There are {numeric} numeric strings.
The sum of all the numbers is {summary}""")
        print(spliter)
        # vytvoření jednoduchých grafických sloupců pro četnost slov o různých délkách
        print("LEN|     OCCURENCES    |NR.")
        print(spliter)
        for length, count in sorted(len_occurences.items()):
            bar = "*" * count
            print(f"{length:3}| {bar:{longest_word_length + 5}}| {count}")
    # Pokud uživatel vybere číslo mimo stanovené rozmezí, 
    # nebo zadá cokoliv jiného, upozorníme uživatele, 
    # že zadaná hodnota není v nabídce a ukončíme program.
    else:
        print("Selected option is unavailable. Terminating the program")
        quit()
# Uživatel zadal špatné jméno nebo heslo       
else:
    print("Unregistered user, terminating the program..")
    quit()