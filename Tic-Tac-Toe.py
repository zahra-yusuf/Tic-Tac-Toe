#Group project CIS 121
# GEU AGUEK, NATALIE DEHWE, ZAHRA YUSUF

'''This program is a TicTacToe game. 
How it works: 
There are two players in each game.User enters a number between 1 and 9.
These numbers represent the position in which each player can place their X or O on the game board. 
If a position is already taken, a player will have to find another position.
Game ends once there is a winner or draw. The winner has 3 of their X's of O's aligned on the game board.
Once game is over, the players can decide if they want to play again.'''




class TicTacToe:
  #Initializing the Players, Board and Score
  def __init__(self, player1, player2):
    self.board=[" "] * 9 #Nine empty spaces
    self.player1 = player1
    self.player2 = player2
    self.symbols ={self.player1: 'X', self.player2: "O"}
    self.current = self.player1
    self.scoreboard = {self.player1: 0, self.player2: 0}
    self.rounds_played = 0

#Resets all spots back to blanks
  def resetboard(self):
    self.board = [" "] * 9
    self.current = self.player1
  
  #Creates the board to be more clearer
  def TheBoard(self):  
    print("\n")
    print(self.board[0], "|", self.board[1], "|", self.board[2])
    print("-------------")
    print(self.board[3], "|", self.board[4], "|", self.board[5])
    print("-------------")
    print(self.board[6], "|", self.board[7], "|", self.board[8])

   #gets a move from the player       
  def get_move(self): 
    while True:
        try:                                                        #exception handling
            move = int(input("Pick a number between 1 and 9: ")) - 1
            if 0 <= move <= 8:
              if self.board[move] == " ":
                return move
              else: 
                print("Pick a different spot. Spot is already taken")
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a number.")
     
#Places current players symbol down
  def update_board(self, index):
    if self.board[index] == " ":
      self.board[index] = self.symbols[self.current]
    else:
      print(" Pick a different move.")
      self.update_board(self.get_move())

  #Checks if board has winning combination
  def the_winner(self):
    wins = [
      (0, 1, 2), (3, 4, 5), (6, 7, 8),
      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
      (0, 4, 8), (2, 4, 6)
    ]
  #winning combinations 
    for combination in wins:
      if self.board[combination[0]] == self.board[combination[1]]:
        if self.board[combination[1]] == self.board[combination[2]]:
          if self.board[combination[0]] != " ":
            return True
    return False
    
#Checks if board is full with no winners
  def a_draw(self):
    return " " not in self.board 
#Switches turn between players
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
          
#I/O file that writes the results of the game
        self.switch_player()
    with open("TicTacToe.txt", "a") as file:
      file.write("Player, Result, Score\n")
      if self.the_winner():
        file.write(f"{self.current}, Win, {self.scoreboard[self.current]}\n\n")
      elif self.a_draw():
        file.write(f"{self.current}, Draw, {self.scoreboard[self.current]}\n\n")
      file.write(f"Final Scoreboard: {self.scoreboard}\n\n")

#calling the class in the main program
game = TicTacToe("X", "O")
while True:
  game.play_game()
  #asks player if they want to play again
  choice = input("Play again? (y/n): ").lower()
  if choice == 'y':
    game.resetboard()
  else:
    print("Thanks for playing!")
    print("Final scores:", game.scoreboard)
    break
  
