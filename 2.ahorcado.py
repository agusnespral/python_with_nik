import random

words = ["camino", "cochera", "aturdido", "galleta", "barcos", "cadena", "ventana", "estrella", "cubetera", "avioneta"]

again = 'y'

while again == 'y':
    print("\nHello! This game is called 'Ahorcado'. You have to guess the secret word. \n"
          "You have 7 chances. In each of them, you can either try to guess a single letter or the entire word \n"
          "If the letter is on the word, its position will be shown.\n"
          "You must guess the entire word before attemps are over.\n"
          "Try to get the complete word in as few attemps as possible.")

    input("Press ENTER to start")

    attempts = 0

    random_num = (random.randint(0, 9))
    chosen_word = words[random_num]
    char_guessed = 0
    chosen_word_len = len(chosen_word)
    attempts_count = 7
    bar_word = ""
    bar_word_count = 0
    guessed = False

    while attempts < 7:

        if bar_word_count == 0:
            print("Your word is:")
            for x in chosen_word:
                bar_word += '_'
            print(bar_word, " || ", char_guessed, "characters guessed over", chosen_word_len)
            print("Attempts left: ", attempts_count)
            bar_word_count = 1

        chance = input("\nPlease, type a letter or an entire word: ")
        attempts += 1
        attempts_count = 7 - attempts

        chance_len = len(chance)
        if chance_len > 1:
           if chance == chosen_word:
                print("CONGRATULATIONS, YOU are the MESSI of the ahorcados! You win the game in", attempts, "attempt/s.\n ")
                guessed = True
                again = input("Press 'y' if you want to try to guess a new word or 'e' to exit")
                break
           else:
               print("Bad call! The guessed word is not the secret one. You still have", attempts_count, "attempts.")

        elif chance_len == 1:
            pos = 0
            printing = 0
            for i in chosen_word:
                if i == chance:
                    bar_word = bar_word[:pos] + i + bar_word[pos + 1:]
                    printing += 1
                pos += 1

            if printing == 0:
                print("Bad call! The guessed letter is not part of the secret word. You still have", attempts_count,
                      "attempts.")
            else:
                print("Nice, your letter is in the word!\n", bar_word, ".\n You still have", attempts_count, "attempts.")

    if attempts == 7 and guessed == False:
        print("Beautiful LOOSER! You have no more attempts left.")
        again = input("Press 'y' if you want to try to guess a new word")