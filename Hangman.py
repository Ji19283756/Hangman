from random import choice


def random_word():
    words = ['abject', 'belong', 'jelly', 'unnatural', 'whistle', 'little', 'hum', 'level',
             'arrogant', 'circle', 'representative', 'brash', 'verse', 'report', 'ritzy',
             'hammer', 'effect', 'end', 'light', 'ambitious', 'nasty', 'crayon', 'roll',
             'minor', 'whisper', 'eight', 'cautious', 'curvy', 'tangible', 'stroke', 'extend',
             'rhetorical', 'coherent', 'murder', 'kaput', 'testy', 'skate', 'brief', 'telling',
             'count', 'carpenter', 'hesitant', 'vigorous', 'saw', 'rose', 'development',
             'curve', 'boat', 'signal', 'flagrant']

    word = choice(words)
    underscore = "_ " * len(word)

    return list(word), underscore, word


def check_guess(letter):
    global mistakes, right, actual_word
    if letter == "guess":
        # print(actual_word)
        guess_word = input("What do you think the word is?\n").lower()
        if guess_word == actual_word:
            right = len(word)
        else:
            mistakes += 1
            print_board(mistakes)
        print(f"Yep! {actual_word} is the word!") if guess_word == actual_word \
            else print("Nope! That's not the word")
        return None
    elif len(letter) > 1 and letter != "guess":
        print("Prints only one letter!")
        return None
    if letter in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        print("Don't type numbers")
        return None
    else:
        return letter


def print_board(mistakes):
    # printed_word = ""  # this is the word that will be actually printed and is based of print_word
    print_worded = "".join(letter + ' ' for letter in print_word)

    # this is the set of letters that will actaully be printed, based on guessed_letters
    printed_guessed_letters = "".join(letter + " " for letter in guessed_letters)

    draw_hangman(mistakes)  # inputs the number of mistakes the user has made and draws the appropriate picture

    # prints the letters that correspond to the right letters (letters in word)
    print(f"{print_worded}\n{underscore}\nGuessed letters: {printed_guessed_letters}")


def check_guess_with_word(user_letter):
    global right, mistakes, guessed_letters
    if user_letter in word:
        print(f"{user_letter} is in the word!")
        for x, word_letter in enumerate(word):
            if user_letter == word_letter:
                print_word[x] == user_letter
                right += 1
    else:
        print(f"{user_letter} is not in the word")
        mistakes += 1
    guessed_letters += user_letter
    return print_word


def draw_hangman(mistakes):
    hangman_body_dict = {0: "   ", 1: "   ", 2: " | ", 3: " | ", 4: " | ", 5: "/| ", 6: "/|\\"}
    hangman_leg_dict = {0: "   ", 1: "   ", 2: "   ", 3: "/  ", 4: "/ \\", 5: "/ \\", 6: "/ \\"}
    hangman = ["   "] * 3
    hangman[0] = "( )" if mistakes >= 1 else "   "
    hangman[1] = hangman_body_dict[mistakes]
    hangman[2] = hangman_leg_dict[mistakes]
    print("                    \n"
          "          _____     \n"
          "         |     |    \n"
          f"        {hangman[0]}    |    \n"
          f"        {hangman[1]}    |    \n"
          f"        {hangman[2]}    |    \n"
          "              /|\   ")


# ______________________________________________________________________________________________________________
guessed_letters = []  # list of the letters that have already been guessed
word, underscore, actual_word = random_word()  # makes a list of the letters in the word and an undercore that matches
print_word = [" "] * len(word)  # has a list of the word that will be printed
# print(word)
mistakes, right = 0, 0  # counter for the amount of words that are right and the amount of words that are wrong
print_board(mistakes)
while mistakes < 6 and not right == len(
        word):  # continues if you havent completed the hangman or if you havent gotten it right
    guess = input("What letter do you think is in the word?\nOptions:\n-guess\n-(print one letter)\n").strip().lower()
    guess = check_guess(guess)  # makes sure that the input is not a number
    if guess in guessed_letters:
        print("you already guessed that letter")
    elif guess is not None and right != len(word):
        print_word = check_guess_with_word(guess)  # checks if the letter is in the word
        print_board(mistakes)

print(f"You lose\nThe word was {actual_word}") if mistakes == 6 else print("You win!")
