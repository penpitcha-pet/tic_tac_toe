def draw_board(board_state):
  print(board_state[0] + '|' + board_state[1] + '|' + board_state[2])
  print('-+-+-')
  print(board_state[3] + '|' + board_state[4] + '|' + board_state[5])
  print('-+-+-')
  print(board_state[6] + '|' + board_state[7] + '|' + board_state[8])


def get_empty_cells(board_state):
  assert(len(board_state) == 9) # make sure that there are exactly 9 cells in the board
  empty_cells = []
  for index in range(9):
    if board_state[index] == ' ':
      empty_cells.append(index)
  return empty_cells

def winning(board_state,player):
  w = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
  return any(board_state[i]==board_state[j]==board_state[k]==player for i,j,k in w)

def even(board_state):
  if ' ' in board_state:
    return False
  if winning(board_state,'X') or winning(board_state,'O'):
    return False
  else:
    return True

import math
#minimax
def minimax(board,depth,ai_turn):
  if winning(board,'O'):
    return 1
  if even(board):
    return 0
  if winning(board,'X'):
    return -1
  
  if ai_turn:
    best_score = -math.inf
    for i in get_empty_cells(board): #ai=o
      board[i] = 'O'
      score = minimax(board,depth+1,False)
      board[i] = ' '
      best_score = max(score,best_score)
    return best_score
  else:
    best_score = math.inf
    for i in get_empty_cells(board): #ai=x
      board[i] = 'X'
      score = minimax(board,depth+1,True)
      board[i] = ' '
      best_score = min(score,best_score)
    return best_score

#ai move
def ai_move(board,player):
  best_score = -math.inf if player == 'O' else math.inf
  best_move = None

  for i in get_empty_cells(board):
    board[i] = player
    score = minimax(board, 0, player == 'X')
    board[i] = ' '

    if player == 'O':
      if score > best_score:
        best_score = score
        best_move = i
    else:
      if score < best_score:
        best_score = score
        best_move = i

  board[best_move] = player
  print(f"AI ({player}) ลงที่ช่อง {best_move}")
  draw_board(board)

#test
def play_ai_vs_ai():
  board_state = [' '] * 9
  draw_board(board_state)

  turn = 'X'
  while True:
    ai_move(board_state, turn)
    if winning(board_state, turn):
      print(f"AI ({turn}) ชนะ")
      break
    if even(board_state):
      print("เสมอกัน")
      break
    turn = 'O' if turn == 'X' else 'X'

play_ai_vs_ai()





