import random


def check_in_row(table):
    for i in [0,3,6]:
        if table[i] != '-' and table[i] == table[i+1] == table[i+2]:
            return True
    return False

def check_in_column(table):
    for i in range(3):
        if table[i] != '-' and table[i] == table[i+3] == table[i+6]:
            return True
    return False

def check_in_diag(table):
    for i in [2,4]:
        if table[4] != '-' and table[4] == table[4+i] == table[4-i]:
            return True
    return False

def win(table):
    return check_in_row(table) or check_in_column(table) or check_in_diag(table)

def printTable(table):
    for i in [0,3,6]:
        print('\n',end='')
        for j in range(3):
            print( table[i+j], end='')
    print('\n')

    

#SETUP
player = {}
computer = {}
print('Welcome! You are going to play tik-tak-toe against me. \nHow can I call you?')
player['name'] = input() #player's name


#GAME

score = 0 #winned games
total = 0 #total games

newGame = True #for new games


while newGame:


    total += 1 #begins a new game

    #Setup
    color = ['X', 'O'] #colors
    draw = True #whether it is draw

    print('X or O? \n(hint: X begins)')
    player['color'] = input() #player's color: X or O
    while player['color'] not in color:
        print('Choose from X or O only')
        player['color'] = input()

    color.remove(player['color'])
    computer['color'] = color[0] #computer's color

    computer['name'] = 'AI' #computer's name

    board = ['-' for i in range(9)] #default board setup

    print('To choose a cell type in a number according to the following: ') #instructions: screen mode (1-9) vs developer mode (0-8)
    for i in [1,4,7]:
        print('\n', end='')
        for j in range(3):
            print(i+j, end='') #screen mode
    print('\n')   


    freeCells = [i+1 for i in range(9)] #free cells (on screen mode)

    #One round
    if player['color'] != 'X': #if computer begins
        print(computer['name'] + ' is choosing a cell.')
        s = random.choice(freeCells)
        board[s -1] = computer['color']
        freeCells.remove(s)
        printTable(board)

    while len(freeCells) > 0:
        #Player's turn
        print('It is your turn, ' + player['name'] + '! \n Choose a cell.')
        s = int(input()) #current step
        while s not in freeCells:
            print('Please choose an empty cell: ')
            s = int(input())

        board[s-1] = player['color'] #dev mode
        freeCells.remove(s)
        printTable(board)

        #check for winning
        if win(board):
            score += 1
            print('You won, ' + player['name'] + '!')
            draw = False
            break

        #Computer's turn
        print(computer['name'] + ' is choosing a cell.')
        s = random.choice(freeCells)
        board[s -1] = computer['color']
        freeCells.remove(s)
        printTable(board)

        #check for winning
        if win(board):
            print('You lost')
            draw = False
            break
    
    if draw:
        print('It is draw.')

    
    #Asks for new round
    print('Do you want to play again? (y/n)')
    ans = input()
    while ans != 'y' and ans != 'n':
        print('Choose y or n')
        ans = input()

    newGame = ans == 'y'

#SCORE
print('Thank you for playing with me, ' + player['name'])
print('Your score is ' + str(score) + ' in ' + str(total) + ' games.')
        
        
