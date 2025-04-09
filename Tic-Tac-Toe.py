class TicTacToe:
  def __init__(self, board, player1, player2):
    self.board=[" "] * 9 #first instance variable
    self.player1 = ""  #second instance variable
    self.player2 = ""  #third instance variable
    self.current = self.player1
  #shows the board
  def TheBoard(self):
    print("n\")
    print(self.board[0], "|", self.board[1], "|", self.board[2])
    print(self.board[3], "|", self.board[4], "|", self.board[5])
    print(self.board[6], "|", self.board[7], "|", self.board[8])

   #gets a move from the player       
  def get_move(self): 
    move = int(input("pick a number 1-9"))
    if move == "1":
      return 0
    elif move == "2":
      return 1
    elif move == "3":
      return 2
    elif move == "4":
      return 3
    elif move == "5":
      return 4
    elif move == "6":
      return 5
    elif move == "7":
      return 6 
    elif move == "8":
      return 7
    elif move == "9":
      return 8
    else:
      print("Pick a different move.-- invalid number")

def update_board(self, index):
  if self.board[index] == " ":
    self.board[index] = self.current
  else:
    print(" Pick a different move.")
    new_index = self.get_move()
    self.update_board(new_index)
  
def the_winner(self):
  wins = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
  ]
  for combination in wins:
    if self.board[combination[0]] == self.board[combination[1]]:
      if self.board[combination[1]] == self.board[combination[2]]:
        if self.board[combination[0]] != " ":
          return True
  return False

def a_draw(self):
  return " " not in self.board
  
      




def switch_player(self):
  if self.current == self.player1:
    self.current = self.player2
  else:
    self.current = self.player1
