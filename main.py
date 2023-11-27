from board import Board
from ai import AI

import asyncio
import websockets

async def gameloop (socket, created):
  active = True
  intelligence = AI()

  while active:
    message = (await socket.recv()).split(':')

    match message[0]:
      case 'GAMESTART':
        col = intelligence.makeMove()
        await socket.send(f'PLAY:{col}')
      case 'OPPONENT':
        col = intelligence.opponentMove(int(message[1]))

        await socket.send(f'PLAY:{col}')
      case 'WIN' | 'LOSS' | 'DRAW' | 'TERMINATED':
        print(message[0])

        active = False

async def create_game ():
  async with websockets.connect(f'ws://neumaa2.stu.rpi.edu:5000/create') as socket:
    await gameloop(socket, True)

async def join_game(id):
  async with websockets.connect(f'ws://neumaa2.stu.rpi.edu:5000/join/{id}') as socket:
    await gameloop(socket, False)

if __name__ == '__main__':
  protocol = input('Join game or create game? (j/c): ').strip()

  match protocol:
    case 'c':
      asyncio.run(create_game())
    case 'j':
      id = input('Game ID: ').strip()

      asyncio.run(join_game(id))
    case _:
      print('Invalid protocol!')
