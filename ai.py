from board import Board
import random

class AI :
    def __init__(self):
        self.board = Board()

    def printBoard(self):
        self.board.printBoard()

    def opponentMove(self, column):
        if self.board.playMove('o', column) == False:
            return False
        if self.board.checkWin() != False:
            print("You have won!")
            return True

        self.makeMove()
        return True
    
    # TODO: Make the AI make an intelligent move instead 
    #       of a random move
    def makeMove(self):
        if (self.board.playMove('x', random.randint(0,6)) == False):
            self.makeMove()