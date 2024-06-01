# import of choice function from random library and Fore,Style from colorama library
from random import choice
from colorama import Fore,Style

### creating block

# creating list with words
some_list = ['fizzy','dizzy','major','march','maker']
# creating list to add coloured symbols and then join them to have a coloured word
colored_word_list = []
# creating counter for game to have a limited tries
# (you can delete it everywhere in the code and then the game will run until you guess the word)
counter = 0
# randomly choice of the word from the some_list (random library)
hidden_word = choice(some_list)

# not necessary, just to know the hidden word (can be freely deleted)
print(hidden_word)

# make the list of symbols from word
hidden_word = list(hidden_word)

# setting that the game will run until the counter reaches 5
while counter != 5:

    # clear out the list from the previous instances of the game + input
    colored_word_list.clear()
    guessed_word = input('Guess a word: ')

    # validation (isinstance function return the input that contains ONLY the letters)
    if len(guessed_word) == 5 and isinstance(guessed_word,str):
        guessed_word = list(guessed_word)

        # check of the winning scenario
        if guessed_word == hidden_word:
            print(f'You have guessed {''.join(hidden_word)}')
            break

        else:
            # zip makes the pair of tuples for each element of two lists (you can google it)
            for pair in zip(guessed_word, hidden_word):

                # loop to extract letters from the first word of tuple
                for letter in pair[0]:

                    # validation: if letter exists in hidden_word and on the right place
                    if letter in hidden_word and pair[0] == pair[1]:

                        # Fore.{Color_Name} makes the text that color, and Style.RESEL_ALL stops this formatting
                        colored_word_list.append(Fore.GREEN + letter + Style.RESET_ALL)

                    # validation: if letter doesn't exist in hidden_word
                    elif letter not in hidden_word:
                        colored_word_list.append(Fore.RED + letter + Style.RESET_ALL)

                    # validation: if letter exists in hidden_word and on the right place
                    elif letter in hidden_word and pair[0] != pair[1]:
                        colored_word_list.append(Fore.YELLOW + letter + Style.RESET_ALL)

            # joining the list of the colorful symbols into word
            print(''.join(colored_word_list))

            # adding counter (we add here because this is the only instance that input was validated)
            counter += 1
    else:
        print('You have entered wrong word or not word at all!')
while guessed_word != hidden_word:
    print('You are out of tries!')
    break

# If you have any additional questions
# telegram: @osygne, slack: Oleksandr Lebediev