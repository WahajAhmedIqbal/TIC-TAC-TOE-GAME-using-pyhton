from django.http import HttpResponse

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

game_still_going = True

winner = None 

current_player = "X"


def func():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
  # dispaly_game
  func()

  while game_still_going:
    hundle_turn(current_player)

    check_if_game_over()

    flip_player()


  if winner == "X" or winner == "O":
    print(winner + "won.")
  elif winner == None:
    print("Tie.")


def hundle_turn(player):

  print(player + "'s turn.'")
  position = input("Choose a position form 1-9: " )

  valid = False
  while not valid:
    
    
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Choose a position form 1-9: " )
     
     
    position = int(position) - 1
     
     
    if board[position] == "-":
      valid = True
    else:
      print("go again ")
  
  board[position] = player
  func()

def check_if_game_over():
  check_if_win()
  check_if_tie()


def check_if_win():
  global winner
  
  row_winner = check_rows()
  cloum_winner = check_colums()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif cloum_winner:
    winner = cloum_winner 
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None 
  
  return

def check_rows():
  global game_still_going
  # check if any row value is same
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False
  if  row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  
  return

def check_colums():
  global game_still_going
  # check if any row value is same
  colum_1 = board[0] == board[3] == board[6] != "-"
  colum_2 = [1] == board[4] == board[7] != "-"
  colum_3 = board[2] == board[5] == board[8] != "-"

  if colum_1 or colum_2 or colum_3:
    game_still_going = False
  if  colum_1:
    return board[0]
  elif colum_2:
    return board[1]
  elif colum_3:
    return board[2]
  return

def check_diagonals():
  global game_still_going
  # check if any row value is same
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = [6] == board[4] == board[2] != "-"
  

  if diagonals_1 or diagonals_2 :
    game_still_going = False
  if  diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False

  return 


def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return




play_game()
