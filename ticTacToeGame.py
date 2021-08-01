#Simple Tic Tac Toe Game

board = ['#','','','','','','','','','']

def display_board(board):
  print(board[1]+'|'+board[2]+'|'+board[3])
  print(board[4]+'|'+board[5]+'|'+board[6])
  print(board[7]+'|'+board[8]+'|'+board[9])


def player_input():
  marker = ''
  while marker not in ['X', 'O']:
    marker = input('Player 1, choose X or O: ').upper()
  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')


def place_marker(board,marker,position):
  board[position] = marker


def win_check(board,mark):
  return ((board[7] == mark and board[8] == mark and board[9] == mark) or
  (board[4] == mark and board[5] == mark and board[6] == mark) or
  (board[1] == mark and board[2] == mark and board[3] == mark) or
  (board[7] == mark and board[4] == mark and board[1] == mark) or
  (board[8] == mark and board[5] == mark and board[2] == mark) or
  (board[9] == mark and board[6] == mark and board[3] == mark) or 
  (board[7] == mark and board[5] == mark and board[3] == mark) or
  (board[9] == mark and board[5] == mark and board[1] == mark))


import random

def choose_first():
  flip = random.radiant(0,1)
  if flip == 0:
    return 'Player 1'
  else:
    return 'Player 2'


def space_check(board,position):
  return board[position] == ''


def full_board_check(board):
  for i in range(1,10):
    if space_check(board,i):
      return False
  return True


def player_choice(board):
  position = 0
  while position not in range(1,9) or not space_check(board,position):
    position = int(input('Choose a position (1-9): '))
  return position


def replay():
  play_again = input('Play again? (Y or N): ').upper()
  return play_again == 'Y'


print('Welcome to Tic Tac Toe!')
