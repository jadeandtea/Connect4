class Board :
    # Handles the connect 4 board. The board
    # is represented by a 2d list with 6 rows and 7 columns.
    # 
    # each function is self-explanatory
    BLANK = '-'

    def __init__(self):
        self.data = []
        for i in range(6):
            self.data.append([self.BLANK for x in range(7)])
        self.currentHeight = [5, 5, 5, 5, 5, 5, 5]
        self.previousMoves = []

    def printBoard(self):
        for x in self.data:
            print(x)

    def printBackend(self):
        print("Blank character:", self.BLANK)
        print("Current column heights:", self.currentHeight)
        print("Move Order:", self.previousMoves)

    def playMove(self, player, column):
        if self.currentHeight[column] == -1:
            return False
        self.data[self.currentHeight[column]][column] = player
        self.currentHeight[column] -= 1
        self.previousMoves.append(column)
        return True
    
    def undoMove(self):
        if len(self.previousMoves) == 0:
            return
        column = self.previousMoves.pop()
        self.data[self.currentHeight[column] + 1][column] = self.BLANK
        self.currentHeight[column] += 1

    # Loops through every placed piece to see if there are 3 of the 
    # same type piece in the five directions below it.
    def checkWin(self):
        for col in range(7):
            if self.currentHeight[col] == 5:
                continue
            for row in range(self.currentHeight[col] + 1, 6):
                status = self.inARow(row, col)
                if status != False:
                    return status
        return False

    # Checks left, right, downleft, down, and downright for a 
    # four in a row starting at (rowStart, colStart)
    # Returns the player if someone has won and False if there isn't a 
    # winner yet.
    def inARow(self, rowStart, colStart):
        directions = ((1, 0), (-1, 0), (1, 1), (0, 1), (-1, 1))
        for k, (dx, dy) in enumerate(directions):
            found = True
            player = self.data[rowStart][colStart]
            for i in range(1, 4):
                if (colStart + (dx * i) < 0 or colStart + (dx * i) > 6
                    or rowStart + (dy * i) < 0 or rowStart + (dy * i) > 5):
                    found = False
                    break
                if (self.data[rowStart + (dy*i)][colStart + (dx*i)] != player):
                    found = False
                    break
            if found:
                return player
        return False
    
    def winningMove(self, column):
        colStart = column
        rowStart = self.currentHeight[column]
        if rowStart == -1:
            return False

        directions = ((1, 1), (1, 0), (1, -1), (0, -1), (0, 1), (-1, 1), (-1, -1))
        for dx, dy in directions:
            found = True
            for i in range(1, 4):
                if (colStart + (dx * i) < 0 or colStart + (dx * i) > 6
                    or rowStart + (dy * i) < 0 or rowStart + (dy * i) > 5):
                    found = False
                    break
                player = self.data[rowStart + dy][colStart + dx]
                if player == self.BLANK:
                    found = False
                    break
                if (self.data[rowStart + (dy*i)][colStart + (dx*i)] != player):
                    found = False
                    break
            if found:
                return player
        return False
            
    def isFull(self):
        fullBoard = [-1, -1, -1, -1, -1, -1, -1]
        return self.currentHeight == fullBoard

    def copyBoard(self):
        return self.data.copy()