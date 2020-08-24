
# Tic Tac Toe

import random

def drawBoard(board):
    # This function prints out the board that makes up the game 

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
       
    
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This particular function shoud return True if the player wants to play again, or it should just return False.
    print('Do you honestly want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    # Given a board and a player's letter, this function returns True if that player has won.
    
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or 
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[7] == letter and board[4] == letter and board[1] == letter) or 
    (board[8] == letter and board[5] == letter and board[2] == letter) or 
    (board[9] == letter and board[6] == letter and board[3] == letter) or 
    (board[7] == letter and board[5] == letter and board[3] == letter) or 
    (board[9] == letter and board[5] == letter and board[1] == letter)) 

def getBoardCopy(board):
    
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Make your move now buddy its your turn. (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # This is our Tic Tac Toe Algorithm
    
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    
    if isSpaceFree(board, 5):
        return 5

    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # It should return True if every space on the board has been taken. or just return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to the Tic Tac Toe Realm!')

while True:
    
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # The Player's time to play.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Doosh Doosh You WIN!!!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('That was a close one, its a tie!!!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has destroyed you, the computer has eaten you for lunch!! YOU LOSE!!.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('That was a close one, its a tie!!!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
