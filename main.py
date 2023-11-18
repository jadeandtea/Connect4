from ai import AI

if __name__ == "__main__":
    opponent = AI()

    while True:
        # Main loop:
        #   Take in a column and play it onto the AI's board
        #   The AI class handles the board
        #   
        #   NOTE: If the input is not an integer, the program 
        #   exits by crashing. If the input is exit, the program 
        #   exits without a crash

        inputString = input("Enter a column: ")
        if (inputString == "exit"):
            break
        column = int(inputString)

        if (opponent.opponentMove(column) == False):
            print("Invalid Move")
        else:
            opponent.printBoard()
