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

#test
board_state = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X']
draw_board(board_state)

if winning(board_state, 'X'):
  print("X ชนะ")
elif winning(board_state, 'O'):
  print("O ชนะ")

print("---------------------------------------")

board_state = ['O', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'X']
draw_board(board_state)

if winning(board_state, 'X'):
  print("X ชนะ")
elif winning(board_state, 'O'):
  print("O ชนะ")

#player,computer
def human_move(board_state):
  while True:
    move = input("ใส่เลขในช่อง 0-8 : ")
    move = int(move)
    if move < 0 or move > 8:
      print("ใส่เลข 0-8 เท่านั้น")
    elif board_state[move] != ' ':
      print("ช่องนี้ได้ทำการเลือกแล้ว")
    else:
      board_state[move] = 'X'
      break

import random
def bot_move(board_state):
  available = get_empty_cells(board_state)
  computer_move = random.choice(available)
  board_state[computer_move] = 'O'
  print("คอมพิวเตอร์ลง")

#test
def play_test():
  board_state = [' '] * 9
  draw_board(board_state)
  while True:
    human_move(board_state)
    draw_board(board_state)
    if winning(board_state, 'X'):
      print("คุณชนะ")
      break
    if not get_empty_cells(board_state):
      print("เสมอกัน")
      break

    bot_move(board_state)
    draw_board(board_state)
    if winning(board_state, 'O'):
      print("คอมชนะ")
      break
    if not get_empty_cells(board_state):
      print("เสมอกัน")
      break

play_test()
