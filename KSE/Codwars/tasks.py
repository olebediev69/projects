def board_print():
    board = {f'{a}{b}': None for b in [1, 2, 3, 4, 5, 6, 7, 8] for a in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}
    boards = list(board.keys())

    for i in range(0, 64, 8):
        print(boards[i], boards[i + 1], boards[i + 2], boards[i + 3], boards[i + 4], boards[i + 5], boards[i + 6],
              boards[i + 7])


def knight_moves(current_pos):
    possible_positions = []
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    current_pos_list = [current_pos[0], int(current_pos[1])]

    current_pos_letter_index = symbols.index(current_pos_list[0])
    current_pos_number_index = numbers.index(current_pos_list[1])

    if current_pos_letter_index - 2 in range(0, 8):
        if current_pos_number_index - 1 in range(0, 8):
            possible_positions.append(symbols[current_pos_letter_index - 2] + str(numbers[current_pos_number_index - 1]))
        if current_pos_number_index + 1 in range(0, 8):
            possible_positions.append(symbols[current_pos_letter_index - 2] + str(numbers[current_pos_number_index + 1]))
    if current_pos_letter_index + 2 in range(0, 8):
        if current_pos_number_index - 1 in range(0, 8):
            possible_positions.append(symbols[current_pos_letter_index + 2] + str(numbers[current_pos_number_index - 1]))
        if current_pos_number_index + 1 in range(0, 8):
            possible_positions.append(symbols[current_pos_letter_index + 2] + str(numbers[current_pos_number_index + 1]))
    if current_pos_letter_index + 1 in range(0, 8):
        if current_pos_number_index - 2 in range(0, 8):
            possible_positions.append(symbols[current_pos_letter_index + 1] + str(numbers[current_pos_number_index - 2]))
        if current_pos_number_index + 2 in range(0, 8):
            possible_positions.append(symbols[current_pos_letter_index + 1] + str(numbers[current_pos_number_index + 2]))
    if current_pos_letter_index - 1 in range(0, 8):
        if current_pos_number_index - 2 in range(0, 8):
            possible_positions.append(symbols[current_pos_letter_index - 1] + str(numbers[current_pos_number_index - 2]))
        if current_pos_number_index + 2 in range(0, 8):
            possible_positions.append(symbols[current_pos_letter_index - 1] + str(numbers[current_pos_number_index + 2]))

    print (possible_positions)


board_print()
knight_moves('h8    ')