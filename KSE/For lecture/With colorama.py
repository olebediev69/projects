from random import sample
from colorama import Fore, Style

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

        print(Fore.GREEN + 'You have guessed one pair and won!' + Style.RESET_ALL)
        break
    elif len(set(revealed_signs)) == 3:
        values = list(actual_matrix.values())
        for i in range(0, 6, 3):
            print(values[i], values[i + 1], values[i + 2])
        print(Fore.MAGENTA + 'You are out of tries. Game over' + Style.RESET_ALL)
        break
    else:
        print('The number of tries left:', Fore.LIGHTCYAN_EX + f'{3 - tries}' + Style.RESET_ALL)
        values = list(actual_matrix.values())
        for i in range(0, 6, 3):
            print(values[i], values[i + 1], values[i + 2])

        while True:
            cell_input = int(input('Enter the number of cells you want to check: '))
            if cell_input in range(1, 7) and cell_input not in occupied_cells:
                actual_matrix[cell_input] = Fore.LIGHTBLUE_EX + hidden_matrix[cell_input] + Style.RESET_ALL
                revealed_signs.append(hidden_matrix[cell_input])
                occupied_cells.add(cell_input)
                tries += 1
                break
            else:
                print(Fore.RED + '\nYou have entered a strange value, try again\n' + Style.RESET_ALL)

















































# from random import sample
# from colorama import Fore,Style
#
# # variables and collections creation
# hidden_matrix = {
#     1:'1',2:'2',3:'3',
#     4:'4',5:'5',6:'6'
# }
# actual_matrix = {
#     1:'1',2:'2',3:'3',
#     4:'4',5:'5',6:'6'
# }
# tries = 0
# revealed_signs = []
# occupied_cells = set()
#
# # place signs in the hidden_matrix
# cells = list(hidden_matrix.keys())
# sign_1 = sample(cells,2)
# for i in sign_1:
#     cells.remove(i)
#     hidden_matrix[i] = '*'
#
# sign_2 = sample(cells,2)
# for i in sign_2:
#     cells.remove(i)
#     hidden_matrix[i] = '>'
#
# sign_3 = sample(cells,2)
# for i in sign_3:
#     cells.remove(i)
#     hidden_matrix[i] = '<'
#
# while True:
#     print(revealed_signs)
#     # condition for the victory
#     if len(set(revealed_signs)) < len(revealed_signs) and len(revealed_signs) != 0:
#
#         # display the current status of the game field
#         values = list(actual_matrix.values())
#         for i in range(0, 6, 3):
#             print(values[i], values[i + 1], values[i + 2])
#
#         print(Fore.GREEN + 'You have guessed one pair and won!' + Style.RESET_ALL)
#         break
#
#     # condition for the defeat
#     elif len(set(revealed_signs)) == 3:
#
#         values = list(actual_matrix.values())
#         for i in range(0, 6, 3):
#             print(values[i], values[i + 1], values[i + 2])
#
#         print(Fore.MAGENTA + 'You are out of tries. Game over' + Style.RESET_ALL)
#         break
#
#     # condition for the cell input
#     else:
#
#         # display matrix and number of tries
#         print('The number of tries left:' , Fore.LIGHTCYAN_EX + f'{3 - tries}' + Style.RESET_ALL)
#
#         values = list(actual_matrix.values())
#         for i in range(0, 6, 3):
#             print(values[i], values[i + 1], values[i + 2])
#
#         # input with validation and tries counter
#         while True:
#             cell_input = int(input('Enter the number of cells you want to check: '))
#             if cell_input in range(1, 7) and cell_input not in set(occupied_cells):
#                 actual_matrix[cell_input] = Fore.GREEN + hidden_matrix[cell_input] + Style.RESET_ALL
#                 revealed_signs.append(hidden_matrix[cell_input])
#                 occupied_cells.add(cell_input)
#                 tries += 1
#                 break
#
#             else:
#                 print(Fore.RED + '\n You have entered strange value, try again \n' + Style.RESET_ALL)
#                 continue