import random
import sys

def difficulty_from_user():
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

def obtain_wordlist(difficulty_level_chosen):
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

def reveal_length_of_word(wordlength):
    print("The mystery word is {} characters long.".format(wordlength))

def display_blanks_and_guessed_letters(secret_word, good_guesses):
    flashy_display_list = []
    for letters in secret_word:
        if letters in good_guesses:
            flashy_display_list.append(letters)
        else:
            flashy_display_list.append("_")
    flashy = " ".join(flashy_display_list)
    print("\n" + flashy + "\n")

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

def check_for_complete_word(secret_word, good_guesses):
    for letters in secret_word:
        if letters in good_guesses:
            continue
        else:
            return False

def game():
    difficulty_level = difficulty_from_user()
    possibilities = obtain_wordlist(difficulty_level)
    the_mystery_word = get_random_word(possibilities)
    word_length = len(the_mystery_word)
    reveal_length_of_word(word_length)
    bad_guesses_number = 0
    bad_guesses = []
    good_guesses = []
    display_blanks_and_guessed_letters(the_mystery_word, good_guesses)
    while bad_guesses_number < 8:
        guess = obtain_user_guess(bad_guesses, good_guesses)
        if len(guess) == 1:
            if guess in the_mystery_word:
                good_guesses.append(guess)
                print("Good job! The letter {} is in the mystery word! You still have {} guesses left".format(guess, (8 - bad_guesses_number)))
                display_blanks_and_guessed_letters(the_mystery_word, good_guesses)
                result = check_for_complete_word(the_mystery_word, good_guesses)
                if result != False:
                    print("You win! The mystery word was {}".format(the_mystery_word))
                    break
            else:
                bad_guesses_number += 1
                bad_guesses.append(guess)
                print("Sorry, {} is not in the word. You only have {} guesses remaining.".format(guess, (8 - bad_guesses_number)))
                display_blanks_and_guessed_letters(the_mystery_word, good_guesses)
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

if __name__ == "__main__":
    main()
