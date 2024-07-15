from random import sample,choice
from colorama import Fore,Style
from time import sleep

# functions block

def show_once(value1,value2):
    actual_matrix[value1] = hidden_matrix[value1]
    actual_matrix[value2] = hidden_matrix[value2]
    show_matrix(actual_matrix)
    sleep(1)
    actual_matrix[value1] = recovery_matrix[value1]
    actual_matrix[value2] = recovery_matrix[value2]

def show_matrix(matrix):
    values = list(matrix.values())
    print()
    for i in range(0,6,3):
        print (values[i], values[i + 1], values[i + 2])

def placemines(matrix):
    cells = list(matrix.keys())
    for i in ['*', '&', '#']:
        for a in sample(cells, 2):
            cells.remove(a)
            matrix[a] = i

# variables, collections announcing
actual_matrix = {n: '?' for n in range(1, 7)}
hidden_matrix = {n: '?' for n in range(1, 7)}
recovery_matrix = {n: '?' for n in range(1, 7)}
guessed_cells = set()
colors = [Fore.LIGHTCYAN_EX,Fore.BLUE,Fore.LIGHTYELLOW_EX]
lives = 4

# logic block
placemines(hidden_matrix)
while True:
    if '?' in actual_matrix.values() and lives > 0:

        show_matrix(actual_matrix)
        try:
            cell_1, cell_2 = map(int, input(f'\n{Fore.BLUE}{Style.BRIGHT}•{Style.RESET_ALL} Format [cell_1 cell_2]: ').split())
        except ValueError:
            print(f'\n{Fore.RED}{Style.BRIGHT}!{Style.RESET_ALL} Invalid input')
            continue

        if (cell_1 not in guessed_cells) and (cell_2 not in guessed_cells):
            if (cell_1 and cell_2) in range(1,7):


                if hidden_matrix[cell_1] == hidden_matrix[cell_2]:
                    random_color = choice(colors)
                    actual_matrix[cell_1] = random_color + hidden_matrix[cell_1] + Style.RESET_ALL
                    actual_matrix[cell_2] = random_color + hidden_matrix[cell_2] + Style.RESET_ALL
                    guessed_cells.add(cell_1)
                    guessed_cells.add(cell_2)
                    colors.remove(random_color)
                    print(f'\n{Fore.GREEN}{Style.BRIGHT}#{Style.RESET_ALL} You have guessed a pair!')

                else:
                    show_once(cell_1,cell_2)
                    lives -= 1
                    print(f'\n{Fore.RED}{Style.BRIGHT}#{Style.RESET_ALL} The number of tries left: {lives}')

            else:
                print(f'{Fore.RED}!{Style.RESET_ALL} The cell number is out of range or already taken')
        else:
            print(f'{Fore.RED}{Style.BRIGHT}!{Style.RESET_ALL} One of the cells is already taken')

    elif '?' not in actual_matrix.values():
        show_matrix(actual_matrix)
        print(f'\n{Fore.GREEN}{Style.BRIGHT}You have won!{Style.RESET_ALL}')
        break

    elif '?' in actual_matrix.values() and lives == 0:
        show_matrix(actual_matrix)
        print(f'\n{Fore.RED}{Style.BRIGHT}You are out of tries!{Style.RESET_ALL}')
        break