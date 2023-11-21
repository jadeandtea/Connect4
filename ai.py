from board import Board
import random

class AI :
    NEG_INFINITY = -99999999
    INFINITY = 9999999999
    def __init__(self):
        self.win = False
        self.board = Board()

    def isGame(self):
        return self.win

    def printBoard(self):
        self.board.printBoard()

    def opponentMove(self, column):
        if self.board.playMove('o', column) == False:
            return False
        if self.board.checkWin() != False:
            print("You have won!")
            self.win = True
            return True

        self.makeMove()
        return True
    
    # TODO: Make the AI make an intelligent move instead 
    #       of a random move
    def scoreBoard(self, column):
        score = 0
        return score

    def makeMove(self):
        bestScore = 0
        bestMoves = []
        for i in range(7):
            score = self.scoreBoard(i)
            print("Score for column", i, score)
            if score > bestScore:
                bestScore = score
                bestMoves.clear()
                bestMoves.append(i)
            elif score == bestScore:
                bestMoves.append(i)
            
        print(bestMoves)
        nextMove = random.randint(0, len(bestMoves) - 1)
        if (self.board.playMove('x', bestMoves[nextMove]) == False):
            self.makeMove()