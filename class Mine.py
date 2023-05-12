import random

class Tile:
    def __init__(self,boarder):
        self.reveal = False
        self.value = 0
        self.boarder = boarder
        self.bomb = False

    def nMineP(self, number):
        self.value = number
    def isBomb(self):
        self.bomb = True
    def revTile(self):
        self.reveal = True

def createBoard(x,y):
    board = []
    for i in range(y+2):
        if (i == 0 or i == y+1):
            board.append([Tile(True) for i in range(x+2)])
        else:
            board.append([Tile(True) if i == 0 or i == x+1 else Tile(False) for i in range(x+2)])
    return board

def pFrontBoard(fBoard):
    for row in fBoard:
        lista = []
        for i in row:
            if i.boarder: 
                lista.append("l")
            elif not(i.reveal):
                lista.append("X")
            else:
                lista.append(str(i.value)) 
        print("".join(lista))

def randomSeed(board,numBomb):
    if numBomb > (len(board[0]) * len(board)//3):
        print("Max number of mines is "+ str((len(board[0]) * len(board)//3)))
        numBomb =(len(board[0]) * len(board)//3)
    while(numBomb>0):
        pFrontBoard(board)
        x = random.randint(1,len(board)-2)
        y = random.randint(1,len(board[0])-2)
        print(board[x][y].bomb)
        if not(board[x][y].bomb):
            board[x][y].isBomb()
            numBomb -= 1
    return board

def addNumbers(board):
    perimeter = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    for i in range(1,len(board)-1):
        for j in range(1,len(board[0])-1):
            bombsP = 0
            if not(board[i][j].bomb):
                for k in perimeter:
                    if board[i+k[0]][j+k[1]].bomb:
                        bombsP += 1
                if bombsP == 0:
                    board[i][j].nMineP(".")
                else:
                    board[i][j].nMineP(bombsP)
    return board


def countBombs(board):
    count = 0
    for i in range(1,len(board)-1):
        for j in range(1,len(board[0])-1):
            if board[i][j].bomb:
                count += 1
    return count


def zeroRecusion(board,x,y):
    perimeter = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    board[x][y].revTile()
    for i in perimeter:
        if board[x+i[0]][y+i[1]].value == "." and not(board[x+i[0]][y+i[1]].reveal):
            zeroRecusion(board,x+i[0],y+i[1])
        else:
            board[x+i[0]][y+i[1]].revTile()
    return board

def spaceRem(board):
    count = 0
    for i in board:
        for j in i:
            if not(j.reveal):
                count += 1
    return count

def inputValue(board):
    PPMD = True
    numBomb = countBombs(board)
    pFrontBoard(board)
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
        
        if board[x][y].value == ".":
            board[x][y].revTile()
            pFrontBoard(board)
            zeroRecusion(board,x,y)
        elif board[x][y].bomb:
            for i in range(1,len(board)-1):
                for j in range(1,len(board[0])-1):
                    if board[i][j].bomb:
                        board[i][j].revTile()
            pFrontBoard(board)
            print("Loser")
            break
        else:
            board[x][y].revTile()
        
        if numBomb >= spaceRem(board):
            pFrontBoard(board)
            print("Winner")
            break
        
        pFrontBoard(board)

board =addNumbers(randomSeed(createBoard(10,10),10))

pFrontBoard(board)

inputValue(board)

#b = Tile(False)
#b.nMineP(3)
#print(b.value)1