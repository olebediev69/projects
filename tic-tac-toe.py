# tic-tac-toe game

from colorama import Fore,Back,Style
import time

def game_status(basic_matrix):
    basic_matrix_values = list(basic_matrix.values())
    for i in range(0, 9, 3):
        print(basic_matrix_values[i], basic_matrix_values[i + 1], basic_matrix_values[i + 2])

def logic_block(basic_matrix,leaderboard):
    basic_matrix_values = list(basic_matrix.values())
    winning_combinations = [
        (0, 1, 2),  # horizontal top row
        (3, 4, 5),  # horizontal middle row
        (6, 7, 8),  # horizontal bottom row
        (0, 3, 6),  # vertical left column
        (1, 4, 7),  # vertical middle column
        (2, 5, 8),  # vertical right column
        (0, 4, 8),  # diagonal top-left to bottom-right
        (2, 4, 6)  # diagonal top-right to bottom-left
    ]

    for combo in winning_combinations:
        if basic_matrix_values[combo[0]] == basic_matrix_values[combo[1]] == basic_matrix_values[combo[2]] == Fore.GREEN + 'X' + Style.RESET_ALL:
            leaderboard['X'] += 1
            return 'X'
        elif basic_matrix_values[combo[0]] == basic_matrix_values[combo[1]] == basic_matrix_values[combo[2]] == Fore.RED + 'O' + Style.RESET_ALL:
            leaderboard['O'] += 1
            return 'O'

leaderboard = {'X':0, 'O':0}

while True:
    do_you_wanna_play = input(Fore.CYAN + "Do you wanna play (y/n):" + Style.RESET_ALL + ' ')
    if do_you_wanna_play.lower() == 'y':
        start_time = time.time()
        basic_matrix = {
                        1: '•', 2: '•', 3: '•',
                        4: '•', 5: '•', 6: '•',
                        7: '•', 8: '•', 9: '•'
        }
        previous_move = []
        print('Current game status is:')
        while '•' in basic_matrix.values():
            game_status(basic_matrix)
            cell_character_input = input(Fore.BLACK + Back.WHITE + 'Enter a cell and a character, format: [cell_number-character]:' + Style.RESET_ALL + ' ')
            cell_input,xo_input = cell_character_input.split('-')

            xo_input = xo_input.upper()

            if (xo_input == 'X' or xo_input == 'O') and cell_input.isdigit():
                cell_input = int(cell_input)
                if len(previous_move) == 0 or xo_input != previous_move[-1]:
                    if basic_matrix.get(cell_input) == '•':
                        if xo_input == 'X':
                            basic_matrix[cell_input] = Fore.GREEN + xo_input + Style.RESET_ALL
                            previous_move.append(xo_input)
                        else:
                            basic_matrix[cell_input] = Fore.RED + xo_input + Style.RESET_ALL
                            previous_move.append(xo_input)
                    else:
                        print(Fore.RED + 'This cell is already ocupied' + Style.RESET_ALL)
                else:
                    print(Fore.RED + 'This character was the previous move, change it' + Style.RESET_ALL)
                    continue
            else:
                print(Fore.RED + 'The input values is wrong, try again' + Style.RESET_ALL)
            winner = logic_block(basic_matrix,leaderboard)
            if winner:
                game_status(basic_matrix)
                print(Fore.LIGHTCYAN_EX + f'\n {winner} wins! \n' + Style.RESET_ALL)
                print(Fore.BLUE + 'The current leaderboard is: ' + Style.RESET_ALL + Fore.GREEN + 'X' + Style.RESET_ALL + f':{leaderboard["X"]} ' + Fore.RED + 'O' + Style.RESET_ALL + f':{leaderboard["O"]}')
                stop_time = time.time()
                print(f'This game took {round(stop_time - start_time,0)} seconds')
                break
        else:
            print('The game has ended!')
    elif do_you_wanna_play.lower() == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Wrong input, please try again')
        continue