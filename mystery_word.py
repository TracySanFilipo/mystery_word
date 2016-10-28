import random
import sys

def try_to_get_difficulty_from_user():
    while True:
        difficulty = input("Choose a difficulty level: select 1 for easy, 2 for normal, or 3 for hard: ")
        if difficulty == '1':
            return '1'
        elif difficulty == '2':
            return '2'
        elif difficulty == '3':
            return '3'
        else:
            print("Select 1 for easy, 2 for normal, or 3 for hard. No other selections can begin the game.")

def obtain_words_of_appropriate_difficulty(difficulty_level_chosen):
    with open("/usr/share/dict/words", "r") as f:
        dictionarywords = f.read()
        cleanwords = dictionarywords.split("\n")
    if difficulty_level_chosen == "1":
        easy_words = []
        for words in cleanwords:
            if len(words) >= 4 and len(words) <= 6:
                easy_words.append(words)
        return easy_words
    if difficulty_level_chosen == "2":
        normal_words = []
        for words in cleanwords:
            if len(words) >= 6 and len(words) <= 8:
                normal_words.append(words)
        return normal_words
    if difficulty_level_chosen == "3":
        hard_words = []
        for words in cleanwords:
            if len(words) > 8:
                hard_words.append(words)
        return hard_words

def get_random_word(word_list):
    secret_word = random.choice(word_list)
    return secret_word

def check_length(mysteryword):
    length = len(mysteryword)
    return length

def reveal_length_of_word(wordlength):
    print("The mystery word is {} characters long.".format(wordlength))

def display_inital_blanks(length):
    display_list = []
    dash_number = "_" * length
    display_list = dash_number.split()
    print("_ "*length)
    return display_list

def display_blanks_and_guessed_letters(length, secret_word, good_guesses):
    flashy_display_list = []
    for letters in secret_word:
        if letters in good_guesses:
            flashy_display_list.append(letters)
        else:
            flashy_display_list.append("_")
    flashy = " ".join(flashy_display_list)
    print(flashy)

def obtain_user_guess(bad_guesses, good_guesses):
    while True:
        guess_from_user = input("Guess a letter: ")
        if guess_from_user in bad_guesses or guess_from_user in good_guesses:
            print("You have already guessed that.")
            continue
        elif guess_from_user.isalpha() == True and len(guess_from_user) == 1:
            lower_guess = guess_from_user.lower()
            return lower_guess
        else:
            print("That is not an appropriate guess.")
            continue

def remaining_letters(bad_guesses, good_guesses):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    remaining_alpha = []
    for letters in alphabet:
        if letters not in bad_guesses and letters not in good_guesses:
            remaining_alpha.append(letters)
    flash_remaining_alpha = ", ".join(remaining_alpha)
    print("The letters you have not guessed are: {}".format(flash_remaining_alpha))

def check_for_complete_word(secret_word, good_guesses):
    final_word = []
    for letters in secret_word:
        if letters in good_guesses:
            final_word.append(letters)
        else:
            return False

def game():
    difficulty_level = try_to_get_difficulty_from_user()
    possibilities = obtain_words_of_appropriate_difficulty(difficulty_level)
    the_mystery_word = get_random_word(possibilities)
    obtain_length_of_word = check_length(the_mystery_word)
    reveal_length_of_word(obtain_length_of_word)
    display_list_to_swap = display_inital_blanks(obtain_length_of_word)
    bad_guesses_number = 0
    bad_guesses = []
    good_guesses = []
    while bad_guesses_number < 8:
        guess = obtain_user_guess(bad_guesses, good_guesses)
        if len(guess) == 1:
            if guess in the_mystery_word:
                good_guesses.append(guess)
                print("Good job! The letter {} is in the mystery word! You still have {} guesses left".format(guess, (8 - bad_guesses_number)))
                display_blanks_and_guessed_letters(obtain_length_of_word, the_mystery_word, good_guesses)
                remaining_letters(bad_guesses, good_guesses)
                result = check_for_complete_word(the_mystery_word, good_guesses)
                if result != False:
                    print("You win! The mystery word was {}".format(the_mystery_word))
                    break
            else:
                bad_guesses_number += 1
                bad_guesses.append(guess)
                print("Sorry, {} is not in the word. You only have {} guesses remaining.".format(guess, (8 - bad_guesses_number)))
                display_blanks_and_guessed_letters(obtain_length_of_word, the_mystery_word, good_guesses)
                remaining_letters(bad_guesses, good_guesses)
        else:
            continue
    if bad_guesses_number >= 8:
        print("Sorry, you lose. The mystery word was {}.".format(the_mystery_word))

def main():
    while True:
        play_game_question = input("Would you like to play the mystery word game? Y/n ")
        if play_game_question.lower() == 'y':
            game()
        elif play_game_question.lower() == 'n':
            print("Good bye!")
            quit()
        else:
            print("Y for yes or n for no.")
            continue

main()
