import random


def random_word():
    words = ['abject', 'belong', 'jelly', 'unnatural', 'whistle', 'little', 'hum', 'level',
             'arrogant', 'circle', 'representative', 'brash', 'verse', 'report', 'ritzy',
             'hammer', 'effect', 'end', 'light', 'ambitious', 'nasty', 'crayon', 'roll',
             'minor', 'whisper', 'eight', 'cautious', 'curvy', 'tangible', 'stroke', 'extend',
             'rhetorical', 'coherent', 'murder', 'kaput', 'testy', 'skate', 'brief', 'telling',
             'count', 'carpenter', 'hesitant', 'vigorous', 'saw', 'rose', 'development',
             'curve', 'boat', 'signal', 'flagrant']
    word = words[random.randint(0, len(words) - 1)]
    underscore = ""
    for x in range(len(word)):
        underscore += "_ "
    return [x for x in word], underscore, word


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
        print((guess_word == actual_word) * ("Yep! " + actual_word + " is the word!") +
              (guess != actual_word) * ("Nope! That's not the word"))
        return
    elif len(letter) > 1 and letter != "guess":
        print("Prints only one letter!")
        return
    try:
        int(letter)
        print("Don't type numbers")
        return None
    except ValueError:
        return letter


def print_board(mistakes):
    printed_word = ""  # this is the word that will be actually printed and is based of print_word
    for x in print_word:  # iterates thru print word and adds the content to printed_word
        printed_word += x + ' '
    printed_guessed_letters = ""  # this is the set of letters that will actaully be printed, based on guessed_letters
    for x in guessed_letters:  # iterates thru guessed letters and adds the content to printed_word
        printed_guessed_letters += x + " "
    draw_hangman(mistakes)  # inputs the number of mistakes the user has made and draws the appropriate picture
    print(printed_word + "\n" + underscore + "\nGuessed letters: " + printed_guessed_letters)
    # prints the letters that correspond to the right letters (letters in word)


def check_guess_with_word(letter):
    global right, mistakes, guessed_letters
    if letter in word:
        print(letter + " is in the word!")
        for x in range(len(word)):
            if word[x] == letter:
                print_word[x] = letter
                right += 1
    else:
        print(letter + " is not in the word")
        mistakes += 1
    guessed_letters += letter
    return print_word


def draw_hangman(mistakes):
    hangman = ["   ", "   ", "   "]
    hangman[0] = (mistakes >= 1) * "( )" + (mistakes == 0) * "   "
    hangman[1] = (mistakes >= 2 and mistakes < 5) * " | " + (mistakes >= 5 and mistakes < 6) * "/| " + (
                mistakes >= 6) * "/|\\" + (mistakes < 2) * "   "
    hangman[2] = (mistakes >= 3 and mistakes < 4) * "/  " + (mistakes >= 4) * "/ \\" + (mistakes < 3) * "   "
    print("                    \n"
          "          _____     \n"
          "         |     |    \n"
          "        " + hangman[0] + "    |    \n"
                                    "        " + hangman[1] + "    |    \n"
                                                              "        " + hangman[2] + "    |    \n"
                                                                                        "              /|\   ")


# ______________________________________________________________________________________________________________
guessed_letters = []  # list of the letters that have already been guessed
word, underscore, actual_word = random_word()  # makes a list of the letters in the word and an undercore that matches
print_word = [' ' for x in range(len(word))]  # has a list of the word that will be printed
# print(word)
mistakes, right = 0, 0  # counter for the amount of words that are right and the amount of words that are wrong
print_board(mistakes)
while mistakes < 6 and not right == len(
        word):  # continues if you havent completed the hangman or if you havent gotten it right
    guess = input("What letter do you think is in the word?\nOptions:\n-guess\n-(print one letter)\n").strip().lower()
    guess = check_guess(guess)  # makes sure that the input is not a number
    if guess in guessed_letters:
        print("you already guessed that letter")
    elif guess != None and right != len(word):
        print_word = check_guess_with_word(guess)  # checks if the letter is in the word
        print_board(mistakes)
print((mistakes == 6) * ("You Lose\nThe word was " + actual_word) + (right == len(word)) * "You Win!")
