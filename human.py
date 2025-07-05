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

#check เสมอหรือไม่
def even(board_state):
  if ' ' in board_state: #มีช่องว่าง
    return False
  if winning(board_state,'X') or winning(board_state,'O'): #มีฝ่ายหนึ่งชนะ
    return False
  else:
    return True

#player
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

#minimax
import math
def minimax(board,depth, ai_turn):
  if winning(board,'O'):
    return 1
  if even(board):
    return 0
  if winning(board,'X'):
    return -1
  
  if ai_turn:
    best_score = -math.inf
    for i in get_empty_cells(board):
      board[i] = 'O'  # ลองลง O
      score = minimax(board, depth + 1, False)  #ผู้เล่นเล่นต่อ
      board[i] = ' '  # ย้อนกลับ
      best_score = max(best_score, score)
    return best_score

  #พยายามเลี่ยงการแพ้
  else:
    best_score = math.inf
    for i in get_empty_cells(board):
      board[i] = 'X'  #ลง X
      score = minimax(board, depth + 1, True)  #AI เล่นต่อ
      board[i] = ' '  #ย้อนกลับ
      best_score = min(best_score, score)
    return best_score

#คอมพิวเตอร์ลงแบบฉลาด
def computer_move(board):
  best_score = -math.inf
  best_move = None
  for i in get_empty_cells(board):
    board[i] = 'O'  #ลง O
    score = minimax(board, 0, False)  #ผู้เล่นตอบกลับ
    board[i] = ' '  #ย้อนกลับ

    if score > best_score:
      best_score = score
      best_move = i

  # ลงจริงที่ตำแหน่งดีที่สุด
  board[best_move] = 'O'
  print(f"คอมพิวเตอร์ลงที่ช่อง {best_move}")

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

    computer_move(board_state)
    draw_board(board_state)
    if winning(board_state, 'O'):
      print("คอมชนะ")
      break
    if not get_empty_cells(board_state):
      print("เสมอกัน")
      break


play_test()
