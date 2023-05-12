import random

def createBoard(x,y):
    sideX = ["l" for i in range(x+2)]
    center = ["l" if i == 0 or i == x+1 else -2 for i in range(x+2)]
    board = []
    for i in range(y+2):
        if (i == 0 or i == y+1):
            board.append(sideX.copy())
        else:
            board.append(center.copy())
    return board

def printBoard(board):
    for i in board:
        if i != board[0] or i != board[len(board)-1]:
            print(i[1:-1])

def randomSeed(board,numBomb):
    if numBomb > (len(board[0]) * len(board)//3):
        print("Max number of mines is "+ str((len(board[0]) * len(board)//3)))
        numBomb =(len(board[0]) * len(board)//3)
    while(numBomb>0):
        x = random.randint(1,len(board)-2)
        y = random.randint(1,len(board[0])-2)
        if board[x][y] == -2:
            board[x][y] = 9
            numBomb -= 1
    return board

def addNumbers(board):
    perimeter = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    for i in range(1,len(board)-1):
        for j in range(1,len(board[0])-1):
            bombsP = 0
            if board[i][j] != 9:
                for k in perimeter:
                    if board[i+k[0]][j+k[1]] == 9:
                     bombsP += 1
                board[i][j] = bombsP
    return board

def countBombs(board):
    count = 0
    for i in range(1,len(board)-1):
        for j in range(1,len(board[0])-1):
            if board[i][j] == 9:
                count += 1
    return count

def cFrontBoard(x,y):
    sideX = ["l" for i in range(x)]
    center = ["l" if i == 0 or i == x-1 else "X" for i in range(x)]
    board = []
    for i in range(y):
        if (i == 0 or i == y-1):
            board.append(sideX.copy())
        else:
            board.append(center.copy())
    return board
    
def pFrontBoard(fBoard):
    for row in fBoard:
        print(" ".join(row))

def zeroRecusion(fBoard,board,x,y):
    perimeter = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    fBoard[x][y] = "."
    for i in perimeter:
        if board[x+i[0]][y+i[1]] == 0 and fBoard[x+i[0]][y+i[1]] == "X":
            zeroRecusion(fBoard,board,x+i[0],y+i[1])
        else:
            if board[x+i[0]][y+i[1]] == 0:
                fBoard[x+i[0]][y+i[1]] = "."
            else:
                fBoard[x+i[0]][y+i[1]] = str(board[x+i[0]][y+i[1]])
    return fBoard

def spaceRem(board):
    count = 0
    for i in board:
        for j in i:
            if j == "X":
                count += 1
    return count

def inputValue(board,fBoard):
    PPMD = True
    numBomb = countBombs(board)
    pFrontBoard(fBoard)
    while (PPMD):
        while (PPMD):
            x = input("Coordenada y: ")
            y = input("Coordenada x: ")
            if x.isdigit() and y.isdigit():
                x = int(x)
                y = int(y)
                if x <= len(board)-2 and x >= 1 and  y <= len(board[0])-2 and y >= 1:
                    break
                else:
                    print("Inputs invalid")
            else:
                print("Inputs invalid")
        if board[x][y] == 0:
            zeroRecusion(fBoard,board,x,y)
        elif board[x][y] == 9:
            for i in range(1,len(board)-1):
                for j in range(1,len(board[0])-1):
                    if board[i][j] == 9:
                        fBoard[i][j] = str("Q")
            pFrontBoard(fBoard)
            print("Loser")
            break
        else:
            fBoard[x][y] = str(board[x][y])
        
        if numBomb >= spaceRem(fBoard):
            pFrontBoard(fBoard)
            print("Winner")
            break
        
        pFrontBoard(fBoard)
    
numBomb = 1

board = addNumbers(randomSeed(createBoard(10,10),numBomb))

printBoard(board)
fBoard = cFrontBoard(len(board[0]),len(board))
inputValue(board,fBoard)