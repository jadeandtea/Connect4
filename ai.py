import asyncio
from board import Board
import random

class AI :
    NEG_INFINITY = -999999999
    POS_INFINITY =  999999999
    def __init__(self):
        self.win = False
        self.board = Board()

    def isGame(self):
        return self.board.checkWin()

    def printBoard(self):
        self.board.printBoard()

    def opponentMove(self, column):
        if self.board.playMove('x', column) == False:
            return False
        if self.board.checkWin() != False:
            print("You have won!")
            self.win = True
            return True

        return self.makeMove()
    
    # TODO: Make the AI make an intelligent move instead 
    #       of a random move
    def searchBest(self, depth, alpha, beta, maximizing):
        for i in range(7):
            winningPlayer = self.board.winningMove(i)
            if winningPlayer == 'o':
                return (i, self.POS_INFINITY)
            elif winningPlayer == 'x':
                return (i, self.NEG_INFINITY)
        
        if self.board.isFull():
            return (False, 0)

        if depth == 0:
            return (3, self.scoreBoard())
        
        if maximizing:
            score = self.NEG_INFINITY
            bestColumn = 3
            for i in range(7):
                if self.board.playMove('o', i) == False:
                    continue
                
                nextMoveScore = self.searchBest(depth - 1, alpha, beta, False)[1]
                print (nextMoveScore)
                self.board.undoMove()

                if nextMoveScore > score:
                    score = nextMoveScore
                    alpha = score
                    bestColumn = i

                if alpha <= beta:
                    break

            return (bestColumn, score)
        else:
            score = self.POS_INFINITY
            bestColumn = 3
            for i in range(7):
                if self.board.playMove('x', i) == False:
                    continue

                nextMoveScore = self.searchBest(depth - 1, alpha, beta, True)[1]
                self.board.undoMove()

                if nextMoveScore < score:
                    score = nextMoveScore
                    alpha = score
                    bestColumn = i

                if alpha >= beta:
                    break

            return (bestColumn, score)

    def scoreBoard(self):
        score = 0
        for col in range(7):
            for row in range(self.board.currentHeight[col] + 1, 6):
                print ("checking", row, col)
                if (col == 3 and self.board.data[row][col] == 'o'):
                    score += 3
                score += self.scorePoint(row, col)
        return score

    def scorePoint(self, row, col):
        score = 0
        directions = ((1, 0), (1, 1), (1, -1), (0, -1))
        for dx, dy in directions:
            pieces = []

            for i in range(0, 4):
                if (col + (dx * i) < 0 or col + (dx * i) > 6
                    or row + (dy * i) < 0 or row + (dy * i) > 5):
                    checkPieces = False
                    break
                pieces.append(self.board.data[row + (dy*i)][col + (dx*i)])

            if pieces.count('o' == 4):
                score += 100
            elif (pieces.count('o' == 3) and pieces.count(self.board.BLANK == 1)):
                score += 5
            elif (pieces.count('o' == 2) and pieces.count(self.board.BLANK == 2)):
                score += 2
            elif (pieces.count('x' == 3) and pieces.count(self.board.BLANK == 1)):
                score -= 4
        return score

    def makeMove(self):
        nextMove, score = self.searchBest(1, self.POS_INFINITY, self.NEG_INFINITY, True)
        self.board.playMove('o', nextMove)
        return nextMove, score