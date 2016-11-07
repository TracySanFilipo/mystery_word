Mystery Word Game
This is a guessing game that uses the large library of Unix included on the operating system. The list of words, including proper names and some obscure ones, that this game pulls from makes the game challenging but fun!

Main()
The main() function is called to run the game. It gives the user a choice between playing the game by typing 'y', or typing 'n' to quit. Any other selections result in a repeat of this question. If the user chooses 'y', the game() function is called and the rest of the functions are called within it. When this function is finished, the main function is looped through again to give the user the option of playing again.

Difficulty_from_user()
The difficulty_from_user() function is the first function that is called within the main game function. It allows the user to choose between three difficulty levels of the game. The recognized inputs are 1, 2, and 3, for easy, normal, and hard respectively. Any other selection leads to a repeat of these three choices. When one of these is selected, it becomes the return of the function (remaining a string).

Obtain_wordlist()
The obtain_wordlist() function is the second function called within the game() function. It takes the output of the difficulty_from_user() function as its input, and imports the words from the Unix dictionary. If '1' was received as the input, the words from the dictionary with lengths greater than or equal to four and less than or equal to six are appended to a list. If '2' was given as the input, words greater than or equal to six but less than or equal to eight are added to a list. If '3' is the input, words with eight or more characters are added to a list. Whichever list is created is returned as the output of this function.

Get_random_word()
The third function to be called within the game function, the get_random_word() function takes the word list returned from the obtain_wordlist() function and uses random choice (from the random library) on it. The word selected is returned as the output of this function.

Reveal_length_of_word()
This is the fourth function to be called within the game() function. It displays the message "The mystery word is # characters long.", with the length of the word chosen inserted into it.

Display_blanks_and_guessed_letters()
The display_blanks_and_guessed_letters() function is called directly before the main loop in the game() function, and after each guess is given. It takes a list of correctly guessed letters and the chosen word as its inputs. It uses a for loop to go through the word, and for each letter, appends the letter to a list if it was guessed, or appends an underscore representing its place if it has not been guessed. When the loop ends, the list is converted into a string, and displayed.

Obtain_user_guess()
The obtain_user_guess() function is called within a while loop in the game() function. It is given the list of correct guesses and the list of incorrect guesses as inputs. These are both created in the game() function as empty lists before the while loop begins, and are then appended to in the while loop. When the obtain_user_guess() function is run, a while loop is begun. The user is asked for an input. If the input is already on one of the lists of previous guesses, the user is told they have already guessed that letter. If the guess is not on these list, is an alphabet character, and has a length of one, it is lower cased and returned as the output. If a guess is made that fits into neither of these categories, the user is told the guess is not acceptable. The while loop continues until the user enters a guess that meets the second set of conditions and is returned.

Check_for_complete_word()
The check_for_complete_word() function is called after a correct guess is made. It takes the chosen word and the list of correct guesses as inputs. In it, a for loop is run, going through each letter of the chosen word. If any of the letters of the chosen word are not in the list of good guesses, the function returns False.

Game()
The game() function is the central function to this program. It calls the difficulty_from_user() function, then the obtain_wordlist() function, and then the get_random_word() function. Then, since it has the word that the user will try to guess, it gets the length of the word and calls the reveal_length_of_word() function to communicate the length to the user. Next, three empty variables are created for use, and the display_blanks_and_guessed_letters() function is run. A while loop is begun and looped through as long as the number of incorrect guesses is less than eight. Within this loop, the obtain_user_guess() function is run to request a guess and ensure it is a legitimate guess. Once a guess is returned as output from this function, if the guess is in the chosen word, it is appended to the list for correct guesses, a positive message congratulating the user is printed, the display_blanks_and_guessed_letters() function is run with the updated list of correct guesses, and the check_for_complete_word() function is run. If the output of the check_for_complete_word() function is not False, a congratulatory "You win" message is displayed, including the correctly guessed word. The game loop is broken, and the loop in the main() function is run again. If the guess is not in the chosen word, it is appended to the list of incorrect guesses and the count of incorrect guesses increases by one. A message is printed informing the user that the guess was incorrect and how many guesses are left before the game is lost.  The display_blanks_and_guessed_letters() function is run to ensure that the user can view it. If the count of incorrect guesses reaches eight, the while loop ends, and a "you lose" message is printed from the game() function. The chosen word is revealed as part of this message, and the game() function is finished running.
