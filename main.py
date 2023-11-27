from board import Board
from ai import AI

import asyncio
import websockets

async def gameloop (socket, created):
  active = True

  while active:
    message = (await socket.recv()).split(':')
    intelligence = AI()

    match message[0]:
      case 'GAMESTART' | 'OPPONENT':
        col = intelligence.opponentMove(message[1])

        await socket.send(f'PLAY:{col}')
      case 'WIN' | 'LOSS' | 'DRAW' | 'TERMINATED':
        print(message[0])

        active = False

async def create_game (server):
  async with websockets.connect(f'ws://{server}/create') as socket:
    await gameloop(socket, True)

async def join_game(server, id):
  async with websockets.connect(f'ws://{server}/join/{id}') as socket:
    await gameloop(socket, False)

if __name__ == '__main__':
  server = input('Server IP: ').strip()
  print(server)

  protocol = input('Join game or create game? (j/c): ').strip()

  match protocol:
    case 'c':
      asyncio.run(create_game(server))
    case 'j':
      id = input('Game ID: ').strip()

      asyncio.run(join_game(server, id))
    case _:
      print('Invalid protocol!')
