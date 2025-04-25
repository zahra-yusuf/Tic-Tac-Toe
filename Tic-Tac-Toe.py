class TicTacToe:
  def __init__(self, player1, player2):
    self.board=[" "] * 9 #Nine empty spaces
    self.player1 = player1
    self.player2 = player2
    self.symbols ={self.player1: 'X', self.player2: "O"}
    self.current = self.player1
    self.scoreboard = {self.player1: 0, self.player2: 0}
    self.rounds_played = 0
  def resetboard(self):
    self.board = [" "] * 9
    self.current = self.player1
  #shows the board
  def TheBoard(self):  
    print("\n")
    print(self.board[0], "|", self.board[1], "|", self.board[2])
    print("--------------------")
    print(self.board[3], "|", self.board[4], "|", self.board[5])
    print("--------------------")
    print(self.board[6], "|", self.board[7], "|", self.board[8])

   #gets a move from the player       
  def get_move(self): 
    while True:
        try:
            move = int(input("Pick a number (1-9): ")) - 1
            if 0 <= move <= 8:
              if self.board[move] == " ":
                return move
              else: 
                print("Pick a different spot. Spot is already taken")
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a number.")
     
#updates the board with the current players move. 
  def update_board(self, index):
    if self.board[index] == " ":
      self.board[index] = self.symbols[self.current]
    else:
      print(" Pick a different move.")
      self.update_board(self.get_move())
  
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
            self.scoreboard[self.current] += 1
            break

        if self.a_draw():
            print("It's a draw!")
            break

        self.switch_player()
with open("TicTacToe.txt", "a") as a file:
  if self._thewinner:
    file.write(f"{self.current} wins!\n")
  if a_draw:
    file.write(f"It's a draw!\n")
  file.write(f"Final Scoreboard: {self.scoreboard}\n\n")
#calling the class in the main program
game = TicTacToe("X", "O")
game.play_game()
