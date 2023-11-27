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

        return self.makeMove()
    
    # TODO: Make the AI make an intelligent move instead 
    #       of a random move
    def scoreBoard(self, column):
        score = 0
        # Simulate a move
        if self.board.playMove('x', column):
            # If win, good
            if self.board.checkWin() == True:
                return self.INFINITY
            
            for i in range(7):
                self.board.playMove('o', i)
                for k in range(7):
                    opponentMoveScore = self.scoreBoard(k)
                    if opponentMoveScore == False:
                        return self.NEG_INFINITY
                    score += opponentMoveScore
                print(self.board.previousMoves)
                self.board.printBoard()
                self.board.undoMove()

            # Reset board for further play
            self.board.undoMove()

            return score 
        
        # Cannot simulate move
        else:
            return False

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
            
        nextMove = random.randint(0, len(bestMoves) - 1)
        return bestMoves[nextMove]