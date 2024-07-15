# colors: https://gist.github.com/vratiu/9780109
from random import sample

Green = '\033[32m'
Magenta = '\033[95m'
Light_cyan = '\033[96m'
Light_blue = '\033[94m'
Red = '\033[91m'
Style_reset = '\033[0m'

hidden_matrix = {i: str(i) for i in range(1, 7)}
actual_matrix = {i: str(i) for i in range(1, 7)}
tries = 0
revealed_signs = []
occupied_cells = set()

cells = list(hidden_matrix.keys())
for sign in ['*', '>', '<']:
    for i in sample(cells, 2):
        cells.remove(i)
        hidden_matrix[i] = sign

while True:
    if len(set(revealed_signs)) < len(revealed_signs) and revealed_signs:

        values = list(actual_matrix.values())
        for i in range(0, 6, 3):
            print(values[i], values[i + 1], values[i + 2])

        print(Green + 'You have guessed one pair and won!' + Style_reset)
        break
    elif len(set(revealed_signs)) == 3:
        values = list(actual_matrix.values())
        for i in range(0, 6, 3):
            print(values[i], values[i + 1], values[i + 2])
        print(Magenta + 'You are out of tries. Game over' + Style_reset)
        break
    else:
        print('The number of tries left:', Light_cyan + f'{3 - tries}' + Style_reset)
        values = list(actual_matrix.values())
        for i in range(0, 6, 3):
            print(values[i], values[i + 1], values[i + 2])

        while True:
            cell_input = int(input('Enter the number of cells you want to check: '))
            if cell_input in range(1, 7) and cell_input not in occupied_cells:
                actual_matrix[cell_input] = Light_blue + hidden_matrix[cell_input] + Style_reset
                revealed_signs.append(hidden_matrix[cell_input])
                occupied_cells.add(cell_input)
                tries += 1
                break
            else:
                print(Red + '\nYou have entered a strange value, try again\n' + Style_reset)
                continue