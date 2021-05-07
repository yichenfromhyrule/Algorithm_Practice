"""
15-110 Hw6 - Battleship Project
Name:
AndrewID:
"""

import hw6_battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *

import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4

'''
makeModel(data)
#5 [Check6-1] & #3 [Check6-2] & #3 [Hw6] & #4 [Hw6]
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"] = 10
    data["cols"] = 10
    data["boardSize"] = 500
    data["cellSize"] = data["boardSize"]/data["rows"]

    data["computerBoardShipNum"] = 5
    data["userBoardShipNum"] = 5
    data["computerBoard"] = emptyGrid(data["rows"],data["cols"])
    data["userBoard"] = emptyGrid(data["rows"], data["cols"])

    data["computerBoard"] = addShips(data["computerBoard"], data["computerBoardShipNum"])
    data["tempShip"] = []
    data["numberOfUserShips"] = 0

    data["winner"] = None
    data["maxTurn"] = 50
    data["currentTurn"] = 0

'''
makeView(data, userCanvas, compCanvas)
#6 [Check6-1] & #2 [Check6-2] & #3 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, compCanvas, data["computerBoard"], False)
    # User Canvas
    # 1. At first set user grid equal to test.testGrid()
    #drawGrid(data, userCanvas, test.testGrid(), True)
    # 2. Set it back to an empty grid
    drawGrid(data, userCanvas, data["userBoard"], True)
    # 3. Set it to testShip
    #drawShip(data, userCanvas, test.testShip())
    # 4. Set it to an empty Ship
    drawShip(data, userCanvas, data["tempShip"])
    drawGameOver(data,userCanvas)

'''
keyPressed(data, events)
#5 [Hw6]
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.char=='\r':
        makeModel(data)


'''
mousePressed(data, event, board)
#5 [Check6-2] & #1 [Hw6] & #3 [Hw6]
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if data["winner"] == None:
        [row, col] = getClickedCell(data, event)
        if board == "user":
            clickUserBoard(data, row, col)
        else:
            if data["numberOfUserShips"]==5:
                runGameTurn(data,row,col)


#### WEEK 1 ####

'''
emptyGrid(rows, cols)
#1 [Check6-1]
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grids = [[1 for _ in range(cols)] for _ in range(rows)]
    return grids


'''
createShip()
#2 [Check6-1]
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    # 1. Choose a row and a col
    row = random.randint(1,8)
    col = random.randint(1,8)
    # 2. Choose vertical or horizontal
    vorh = random.randint(0,1)
    # 3
    if vorh==0: #vertical
        return [[row-1, col],[row, col], [row+1, col]]
    else:
        return [[row, col-1], [row, col], [row, col+1]]


'''
checkShip(grid, ship)
#3 [Check6-1]
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for cell in ship:
        cellRow = cell[0]
        cellCol = cell[1]
        if grid[cellRow][cellCol] != EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
#4 [Check6-1]
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    currentShips = 0
    while currentShips!=numShips:
        newShip = createShip()
        if checkShip(grid, newShip):
            for cell in newShip:
                cellRow = cell[0]
                cellCol = cell[1]
                grid[cellRow][cellCol] = SHIP_UNCLICKED
            currentShips += 1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
#6 [Check6-1] & #1 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for y in range(0, int(data["cols"])):
        for x in range(0, int(data["rows"])):
            x1 = (y * data["cellSize"])
            x2 = (x1 + data["cellSize"])
            y1 = (x * data["cellSize"])
            y2 = (y1 + data["cellSize"])
            if grid[x][y]==SHIP_UNCLICKED and showShips==True:
                canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
            else:
                if grid[x][y]==SHIP_UNCLICKED and showShips==False:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                elif grid[x][y]==SHIP_CLICKED:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                elif grid[x][y]==EMPTY_CLICKED:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    canvas.update()
    canvas.pack()



### WEEK 2 ###

'''
isVertical(ship)
#1 [Check6-2]
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    for i in range (0, len(ship)-1):
        if (ship[i][1] != ship[i+1][1]) or (ship[i+1][0]-ship[i][0]!=1) :
            return False
    return True


'''
isHorizontal(ship)
#1 [Check6-2]
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    for i in range (0, len(ship)-1):
        if (ship[i][0] != ship[i+1][0]) or (ship[i+1][1]-ship[i][1]!=1):
            return False
    return True


'''
getClickedCell(data, event)
#2 [Check6-2]
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    x_pos = event.x
    y_pos = event.y
    col = int(x_pos // data["cellSize"])
    row = int(y_pos // data["cellSize"])
    return [row, col]


'''
drawShip(data, canvas, ship)
#3 [Check6-2]
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for cell in ship:
        x1 = (cell[1] * data["cellSize"])
        x2 = (x1 + data["cellSize"])
        y1 = (cell[0] * data["cellSize"])
        y2 = (y1 + data["cellSize"])
        canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    canvas.update()
    canvas.pack()


'''
shipIsValid(grid, ship)
#4 [Check6-2]
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship)==3:
        if checkShip(grid, ship):
            if isVertical(ship) or isHorizontal(ship):
                return True
    return False


'''
placeShip(data)
#4 [Check6-2]
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["userBoard"], data["tempShip"]):
        for cell in data["tempShip"]:
            data["userBoard"][cell[0]][cell[1]] = SHIP_UNCLICKED
        data["numberOfUserShips"]+=1
    else:
        print("Error Message: The Temporary Ship Is Invalid.")
    data["tempShip"] = []



'''
clickUserBoard(data, row, col)
#4 [Check6-2]
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["numberOfUserShips"] == 5:
        exit()
    else:
        clickedCell = [row,col]
        if (clickedCell in data["tempShip"]):
            return
        else:
            data["tempShip"].append(clickedCell)

        if len(data["tempShip"]) ==3:
            placeShip(data)

        if data["numberOfUserShips"]==5:
            print("START PLAYING THE GAME")


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
#1 [Hw6] & #3 [Hw6]
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col]==SHIP_UNCLICKED:
        board[row][col] = SHIP_CLICKED
    elif board[row][col]==EMPTY_UNCLICKED:
        board[row][col]=EMPTY_CLICKED
    if isGameOver(board):
        data["winner"]=player


'''
runGameTurn(data, row, col)
#1 [Hw6] & #2 [Hw6] & #4 [Hw6]
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if data["currentTurn"]==data["maxTurn"]:
        data["winner"] = "draw"
    else:
        if data["computerBoard"][row][col]==SHIP_CLICKED or data["computerBoard"][row][col]==EMPTY_CLICKED:
            return
        else:
            updateBoard(data, data["computerBoard"],row, col, "user")
            [com_row, com_col] = getComputerGuess(data["userBoard"])
            updateBoard(data, data["userBoard"], com_row, com_col, "comp")
            data["currentTurn"] += 1



'''
getComputerGuess(board)
#2 [Hw6]
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    board_size=len(board)
    row = random.randint(0,board_size-1)
    col = random.randint(0,board_size-1)
    while(board[row][col]==EMPTY_CLICKED or board[row][col]==SHIP_CLICKED):
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
    return [row,col]


'''
isGameOver(board)
#3 [Hw6]
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in board:
        for cell in row:
            if cell==SHIP_UNCLICKED:
                return False
    return True


'''
drawGameOver(data, canvas)
#3 [Hw6] & #4 [Hw6] & #5 [Hw6]
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    result_x = data["boardSize"]//2
    result_y = data["boardSize"]//3
    result_y2 = data["boardSize"]//2
    if data["winner"]=="user":
        canvas.create_text(result_x,result_y,fill="green",font="Times 90 bold", text="WIN")
        canvas.create_text(result_x, result_y2, fill="SeaGreen1", font="Times 40 bold",
                           text="Press Enter" + '\n' + "If Want To Play Again")
    elif data["winner"]=="comp":
        canvas.create_text(result_x, result_y, fill="pink", font="Times 90 bold", text="LOST")
        canvas.create_text(result_x, result_y2, fill="SeaGreen1", font="Times 40 bold",
                           text="Press Enter" + '\n' + "If Want To Play Again")
    elif data["winner"]=="draw":
        canvas.create_text(result_x, result_y, fill="orange", font="Times 50 bold", text="DRAW-Out of moves")
        canvas.create_text(result_x, result_y2, fill="SeaGreen1", font="Times 40 bold", text="Press Enter" + '\n' +"If Want To Play Again")
    canvas.update()
    canvas.pack()
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()

    ## Uncomment these for Week 2 ##

    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()


    ## Uncomment these for Week 3 ##

    print("\n" + "#"*15 + " WEEK 3 TESTS " +  "#" * 16 + "\n")
    test.week3Tests()
    

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
