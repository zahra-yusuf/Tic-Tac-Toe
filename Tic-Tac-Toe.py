class TicTacToe:
  def __init__(self, board, player1, player2):
    self.board=[" "] *9
    self.player1 = ""
    self.player2 = ""

  def TheBoard(self):
    print("n\")
    print(self.board[0], "|", self.board[1], "|", self.board[2])

