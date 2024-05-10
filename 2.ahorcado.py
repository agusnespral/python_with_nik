import random

words = ["camino", "cochera", "aturdido", "galleta", "barcos", "cadena", "ventana", "estrella", "cubetera", "avioneta"]

again = 'y'

def formarBarWord():
    global chosen_word, bar_word
    for x in chosen_word:
        bar_word += '_'

def mensajePrimerIntento():
    global bar_word, esPrimerIntento, attempts_count
    print("\nYour word is:")
    print(bar_word, " || ", " 0 characters guessed over", len(bar_word))
    print("Attempts left: ", attempts_count)
    esPrimerIntento = False

def arriesgaPalabra():
    global guessed, chosen_word, chance, attempts, attempts_count
    if chance == chosen_word:
        print("CONGRATULATIONS, YOU are the MESSI of the ahorcados! You win the game in", attempts, "attempt/s.\n ")
        opcionReplay()
        guessed = True
    else:
        print("Bad call! The guessed word is not the secret one. You still have", attempts_count, "attempts.")

def arriesgaLetra():
    global bar_word, attempts_count
    pos = 0
    printing = False
    for i in chosen_word:
        if i == chance:
            bar_word = bar_word[:pos] + i + bar_word[pos + 1:]
            printing = True
        pos += 1

    if not printing:
        if attempts_count > 0:
            print("Bad call! The guessed letter is not part of the secret word.")
        else:
            print("Bad call and thats all.")
            
    else:
        if attempts_count > 0:
            print("Nice, your letter is in the word!\n", bar_word, ".\n")
        else:
            print("Your letter is in the word.")

def opcionReplay():
    replay = input("Press 'y' if you want to try to guess a new word")
    if replay == 'y':
        play()
    else:
        despedida()

def despedida():
    print("\nSayonara!!!.\n")

def play():

    global words, chosen_word, attempts_count, bar_word, chance

    attempts = 0
    random_num = (random.randint(0, 9))
    chosen_word = words[random_num]
    attempts_count = 7
    bar_word = ""
    esPrimerIntento = True
    guessed = False

    formarBarWord()

    while attempts < 7 and not guessed:

        if esPrimerIntento:
            mensajePrimerIntento()
            
        chance = input("\nPlease, type a letter or an entire word: ")
        attempts += 1
        attempts_count = 7 - attempts

        if len(chance) > 1:
           arriesgaPalabra()

        elif len(chance) == 1:
            arriesgaLetra()

    if not guessed:
        print("\nBeautiful LOOSER! You have no more attempts left.")
        opcionReplay()


#FLUJO MAIN

print("\nHello! This game is called 'Ahorcado'. You have to guess the secret word. \n"
        "You have 7 chances. In each of them, you can either try to guess a single letter or the entire word \n"
        "If the letter is on the word, its position will be shown.\n"
        "You must guess the entire word before attemps are over.\n"
        "Try to get the complete word in as few attemps as possible.\n")

input("Press ENTER to start")

play()