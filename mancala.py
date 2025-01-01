BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '
NUM_CUPS = 6

dictionary = {'Cup1': 4, 'Cup2': 4, 'Cup3': 4, 'Cup4': 4, 'Cup5': 4, 'Cup6': 4, 'Mancala2': 0, 'Cup7': 4, 'Cup8': 4,
               'Cup9': 4, 'Cup10': 4, 'Cup11': 4, 'Cup12': 4, 'Mancala1': 0}

def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]

def get_player():
    bothnames = []
    name1 = input('Player 1 please tell me your name? ')
    name2 = input('Player 2 please tell me your name ')
    bothnames.append(name1)
    bothnames.append(name2)
    return bothnames

def take_turn(player, cups):
    followingplayer = {'No marbles': player}
    if cups > 12 or cups < 1:
        followingplayer = {'Nonexistent': player}
        return followingplayer
    moves = dictionary[f'Cup{cups}']
    if moves == 0:
        followingplayer = {'There is no stones': player}
        return followingplayer
    dictionary[f'Cup{cups}'] = 0
    if cups > 6:
        i = cups
    else:
        i = cups - 1

    while moves != 0:
        i += 1
        if i == 14:
            i = 0
        dictionary[list(dictionary.keys())[i]] += 1
        moves -= 1
        if moves == 0:
            if list(dictionary.keys())[i] == 'First Mancala' or list(dictionary.keys())[i] == 'Second Mancala':
                followingplayer = {'Try Again': player}
                return followingplayer
    if player == 0:
        followingplayer = {'Player': 1}
        return followingplayer
    elif player == 1:
        followingplayer = {'Player': 0}
        return followingplayer

def victory(list):
    if sum(list[0:6]) == 0 or sum(list[8:13]) == 0:
        boardchange(dictionary, players)
        if dictionary['Mancala1'] > dictionary['Mancala2']:
            print(f'{players[1]} has won the game!!')
            return True

        else:
            print(f'{players[0]} is the winner.')
            return True

    return False

def boardchange(stones, names):
    Opened = []
    counter = 6
    for i in range(12):
        opening = []
        if i < 6:
            opening.append(list(stones.keys())[i])
            opening.append('Stones')
            opening.append(f'{SPACE * (BLOCK_WIDTH - 4)} {stones[f"Cup{i + 1}"]} ')
            for i in range(BLOCK_HEIGHT - 3):
                opening.append(SPACE * BLOCK_WIDTH)
            Opened.append(opening)
        else:
            opening.append(list(stones.keys())[i + counter])
            opening.append('Stones')
            opening.append(f'{SPACE * (BLOCK_WIDTH - 4)} {stones[f"Cup{i + counter}"]} ')
            for i in range(BLOCK_HEIGHT - 3):
                opening.append(SPACE * BLOCK_WIDTH)
            Opened.append(opening)
            counter -= 2
    upperline = Opened[0:NUM_CUPS]
    lowerline = Opened[NUM_CUPS:]

    mancala1 = []
    mancala2 = []
    for i in range((BLOCK_HEIGHT) - 1):
        mancala1.append(SPACE * BLOCK_WIDTH)
        mancala2.append(SPACE * BLOCK_WIDTH)

    mancala1.append(f'{names[1]}')
    mancala2.append(f'{names[0]}')
    for i in range((BLOCK_HEIGHT) - 2):
        mancala1.append(SPACE * BLOCK_WIDTH)
        mancala2.append(SPACE * BLOCK_WIDTH)
    mancala1.append('stones')
    mancala1.append(f'{SPACE * (BLOCK_WIDTH - 3)} {stones["Mancala1"]} ')
    mancala2.append('stones')
    mancala2.append(f'{SPACE * (BLOCK_WIDTH - 3)} {stones["Mancala2"]} ')
    draw_board(upperline, lowerline, mancala1, mancala2)

def turns(liveplayer, following_player):
    if list(liveplayer.keys())[0] == 'Nonexistent':
        liveplayer = take_turn(following_player['Nonexistent'], (int(input(
            f'{players[(following_player["Does not exist"])]} Nonexistent. What cup do you want to move? '))))
    elif list(liveplayer.keys())[0] == 'Player':
        liveplayer = take_turn(following_player['Player'],
                               int(input(f'{players[following_player["Player"]]} What cup do you want to move? ')))
    elif list(liveplayer.keys())[0] == 'No stones':
        liveplayer = take_turn(following_player['No stones'],
                               int(input(f'{players[1]} your cup had no marbles. What cup do you want to move? ')))
    elif list(liveplayer.keys())[0] == 'Play Again':
        liveplayer = take_turn(following_player['Play Again'], (int(input(
            f'{players[following_player["Play Again"]]} your cup landed in mancala. What cup do you want to move? '))))
    return liveplayer

def run_game():
    boardchange(dictionary, players)
    liveP = take_turn(0, int(input(f'{players[0]} what cup do you want to move? ')))
    next_player = liveP
    winner = False
    while not winner:
        boardchange(dictionary, players)
        liveP = turns(liveP, next_player)
        next_player = liveP

        winner = victory(list(dictionary.values()))

if __name__ == "__main__":
    players = get_player()
    run_game()