from random import randint
from random import shuffle
from time import sleep

count_pc = 0
count_human = 0


def main():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    intro()
    currentplayer_index = 0
    start_symbols = ['X', 'O']
    p1 = input(f'Good day, Please state your name: ').capitalize()
    p2 = input(f'Good day Player 2! your opponent will be {p1}. '
               f'Please state your name(if you like to play against Computer, Please type Computer): ').capitalize()
    print(f'{p1} to select your symbol please type 1 for X or 2 for O: ')

    p_1_symbol_start = 5

    p_2_symbol_start = 4

    while p_1_symbol_start not in range(1, 2) or p_2_symbol_start not in range(1, 2):
        try:
            print(f'{p1} to select your symbol please type 1 for X or 2 for O: ')
            p_1_symbol_start = int(
                input(f'hello {p1}, Please state your symbol! you could choose from {str(start_symbols)}'))
            print(f'{p2} to select your symbol please type 1 for X or 2 for O : ')
            p_2_symbol_start = int(
                input(f'hello {p2}, Please state your symbol! you could choose from {str(start_symbols)}'))
            continue
        except ValueError as ve:
            continue
    if p2 == "Computer":
        p2 = 'Computer'
    else:
        pass
    if p_1_symbol_start == p_2_symbol_start:
        print(f'hey {p2}, you cannot choose the same symbol as {p1}!! ')
        print('the symbol will be auto corrected for you !!')
        sleep(5)

        if p_1_symbol_start == 1 or p_1_symbol_start == 'X':
            p_2_symbol_start = start_symbols[1]
            print(f'{p2}, your symbol is corrected to {start_symbols[1]} ! ')
            sleep(5)
        else:
            p_2_symbol_start = start_symbols[0]
            print(f'{p2}, your symbol is corrected to {start_symbols[0]} ! ')
            sleep(5)
    else:
        p_1_symbol_start = start_symbols[int(p_1_symbol_start) - 1]
        p_2_symbol_start = start_symbols[int(p_2_symbol_start) - 1]

    startup_player = randint(1, 2)
    startup_player -= 1
    if startup_player == 1:
        currentplayer_index = 0
    else:
        currentplayer_index = 1

    players = [p1, p2]
    symbols = [p_1_symbol_start, p_2_symbol_start]
    current_player = players[currentplayer_index]
    print_board(board)

    while not find_winner(board):
        current_player = players[currentplayer_index]
        symbol = symbols[currentplayer_index]
        announce_player_turn(current_player)
        print_board(board)
        if not choose_location(board, symbol, current_player):
            if current_player != "Computer":
                print('that is not a correct option!! Please try again!')
                print('please select a field from 1 to 9')
                print('below you will find a help for the fields: ')
                print('|1|2|3|')
                print('|4|5|6|')
                print('|7|8|9|')
                input('Press ENTER to continue')
            else:
                pass
            continue
        empty_board(board)

        currentplayer_index = (currentplayer_index + 1) % len(players)
    print(f'Congratulations, {current_player}!! you have won the game !!')
    print(f'you won with board {print_board(board)}')
    reply()


def empty_board(board):
    count = 0
    for cells in board:
        for cel in cells:
            if cel == 'X' or cel == "O":
                count += 1

            else:
                pass
    if count == 9:
        print('field is full the game is a tie: ')
        reply()
    else:
        pass


def choose_location(board, symbol, current_player):
    if current_player == "Computer":

        row = randint(1, 3)
        row -= 1
        col = randint(1, 3)
        col -= 1
        cell = board[row][col]
        if cell is not None:
            return False

        board[row][col] = symbol
        return True
    else:
        try:
            print('please choose your location on the Board.')
            print('you could select the fields  using numbers from 1 to 9:')
            print('The first field of the board is 1 !')
            print()
            print_board(board)
            print()
            k = int(input('please select your field: '))
            if k in range(1, 10):
                if k == 1:
                    cell = board[0][0]
                    if cell is not None:
                        return False
                    else:
                        board[0][0] = symbol
                        return True
                elif k == 2:
                    cell = board[0][1]
                    if cell is not None:
                        return False
                    else:
                        board[0][1] = symbol
                        return True
                elif k == 3:
                    cell = board[0][2]
                    if cell is not None:
                        return False
                    else:
                        board[0][2] = symbol
                        return True
                elif k == 4:
                    cell = board[1][0]
                    if cell is not None:
                        return False
                    else:
                        board[1][0] = symbol
                        return True
                elif k == 5:
                    cell = board[1][1]
                    if cell is not None:
                        return False
                    else:
                        board[1][1] = symbol
                        return True
                elif k == 6:
                    cell = board[1][2]
                    if cell is not None:
                        return False
                    else:
                        board[1][2] = symbol
                        return True
                elif k == 7:
                    cell = board[2][0]
                    if cell is not None:
                        return False
                    else:
                        board[2][0] = symbol
                        return True
                elif k == 8:
                    cell = board[2][1]
                    if cell is not None:
                        return False
                    else:
                        board[2][1] = symbol
                        return True
                elif k == 9:
                    cell = board[2][2]
                    if cell is not None:
                        return False
                    else:
                        board[2][2] = symbol
                        return True
        except ValueError as ve:
            print(ve)
            print('please select digit for the field')
            return False
        else:
            pass


def find_winner(board):
    sequences = get_winning_sequence(board)
    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequence(board):
    sequence = []

    rows = board
    sequence.extend(rows)

    for cols in range(0, 3):
        col = [
            board[0][cols],
            board[1][cols],
            board[2][cols],
        ]
        sequence.append(col)

    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    sequence.extend(diagonals)

    return sequence


def reply():
    print()
    z = input('Would you like to play again? please select Y for yes or type anything else to Quit: ')
    if z == 'Y':
        main()
        return True
    else:
        print('GoodBye')
        exit()


def intro():
    print()
    print('Welcome to my game!')
    print('I hope you will have a lot of fun here ;)')
    print()


def announce_player_turn(current_player):
    print()
    print(f'it is {current_player} turn ! Here is the Board :  ')
    print()


def print_board(board):
    for row in board:
        print('|', end='')
        for cells in row:
            symbol = cells if cells is not None else "_"
            print(symbol, end='| ')
        print()


if __name__ == '__main__':
    main()

