# funny game with bombs
from random import sample
from colorama import Fore, Back, Style


def game_state_display(game_state):
    game_state = list(game_state.values())
    print()
    for i in range(0, 16, 4):
        print(game_state[i], game_state[i + 1], game_state[i + 2], game_state[i + 3])
    print()


def mines_placement(game_state, number_of_mines):
    mines_positions = sample(range(1, 17), number_of_mines)
    for pos in mines_positions:
        game_state[pos] = 'x'
    return mines_positions


def win_counter(game_state):
    counter = 0
    for v in game_state.values():
        if v == '•':
            counter += 1
    return counter


basic_matrix = {
    1: '•', 2: '•', 3: '•', 4: '•',
    5: '•', 6: '•', 7: '•', 8: '•',
    9: '•', 10: '•', 11: '•', 12: '•',
    13: '•', 14: '•', 15: '•', 16: '•'
}
visual_game_matrix = {
    1: '•', 2: '•', 3: '•', 4: '•',
    5: '•', 6: '•', 7: '•', 8: '•',
    9: '•', 10: '•', 11: '•', 12: '•',
    13: '•', 14: '•', 15: '•', 16: '•'
}

number_of_mines = int(input('Enter the number of mines you want to have (1-5): '))

if number_of_mines > 0 and number_of_mines <= 5:
    if number_of_mines == 1:
        number_of_lives = 1
    elif number_of_mines in range(2, 4):
        number_of_lives = 2
    else:
        number_of_lives = 3
else:
    print('Please enter a positive integer between 1 and 5')
    exit(1)

print(f'You have {number_of_lives} lives left.')
mines_placement(basic_matrix, number_of_mines)

game_state_display(visual_game_matrix)

while number_of_lives > 0:
    player_choice = int(input('Enter a number between 1 and 16: '))
    if visual_game_matrix[player_choice] == '•':
        if basic_matrix[player_choice] == 'x':
            number_of_lives -= 1
            visual_game_matrix[player_choice] = Fore.RED + 'x' + Style.RESET_ALL
            print(f'The number of lives remaining: {number_of_lives}')
        else:
            visual_game_matrix[player_choice] = Fore.GREEN + '✓' + Style.RESET_ALL

        game_state_display(visual_game_matrix)

        if win_counter(visual_game_matrix) == number_of_mines:
            print(Fore.CYAN + 'You have won! Congrats!' + Style.RESET_ALL)
            break
    else:
        print('You have entered here before, please try again')

if number_of_lives == 0:
    print(Fore.LIGHTCYAN_EX + 'Game Over' + Style.RESET_ALL)
