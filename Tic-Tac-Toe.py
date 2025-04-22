class TicTacToe:
  def __init__(self, board, player1, player2):
    self.board=[" "] * 9 
    self.player1 = player1
    self.player2 = player2
    self.current = self.player1
  
  def TheBoard(self):
    print("\n")
    print(self.board[0], "|", self.board[1], "|", self.board[2])
    print(self.board[3], "|", self.board[4], "|", self.board[5])
    print(self.board[6], "|", self.board[7], "|", self.board[8])

   #gets a move from the player       
  def get_move(self): 
    while True:
        try:
            move = int(input("Pick a number (1-9): ")) - 1
            if 0 <= move <= 8:
                return move
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a number.")
     

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

#method that controls the whole game flow
  def play_game(self):
    print("Welcome to Tic Tac Toe!")
    self.TheBoard()

    while True:
        print(f"{self.current}'s turn.")
        move = self.get_move()
        self.update_board(move)
        self.TheBoard()

        if self.the_winner():
            print(f"Congratulations {self.current}, you win!")
            break

        if self.a_draw():
            print("It's a draw!")
            break

        self.switch_player()

#calling the class in the main program
game = TicTacToe("X", "O")
game.play_game()
