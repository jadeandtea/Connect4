from board import Board
from ai import AI

import asyncio
import websockets

POS_INFINITY =  999999999
NEG_INFINITY = -999999999

async def gameloop (socket, created):
  active = True
  intelligence = AI()

  while active:
    message = (await socket.recv()).split(':')
    print (message)

    match message[0]:
      case 'GAMESTART':
        col = 3
        await socket.send(f'PLAY:{col}')
      case 'OPPONENT':
        intelligence.opponentMove(int(message[1]))

        column, score = intelligence.makeMove()
        print(score)

        await socket.send(f'PLAY:{column}')
      case 'ERROR':
        errMsg = message[1]
        if errMsg == 'not current turn':
          continue
        column = intelligence.makeRandomMove()

        await socket.send(f'PLAY:{column}')
      case 'WIN' | 'LOSS' | 'DRAW' | 'TERMINATED':
        print(message[0])

        active = False

async def create_game ():
  async with websockets.connect(f'ws://localhost:5000/create') as socket:
    await gameloop(socket, True)

async def join_game(id):
  #async with websockets.connect(f'ws://neumaa2.stu.rpi.edu:5000/join/{id}') as socket:
  async with websockets.connect(f'ws://localhost:5000/join/{id}') as socket:
    await gameloop(socket, False)

async def local_loop():
  opponent = AI()
  while not opponent.isGame():
    opponent.board.printBackend()
    inputString = input("Enter a column: ")
    if (inputString == "exit"):
        exit()
    playerColumn = int(inputString)
    opponent.board.playMove('x', playerColumn)
    AIColumn, score = opponent.makeMove()
    print(AIColumn)
    print(score)
    opponent.printBoard()

if __name__ == '__main__':
  protocol = input('Join game or create game? (j/c): ').strip()

  match protocol:
    case 'c':
      asyncio.run(create_game())
    case 'j':
      id = input('Game ID: ').strip()
      
      asyncio.run(join_game(id))
    case 'm':
      asyncio.run(local_loop())

    case _:
      print('Invalid protocol!')
