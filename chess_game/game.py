from board import Board
from player import Player
from color import Color
from move import Move

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(Color.WHITE), Player(Color.BLACK)]
        self.current_player = 0

    def start(self):
        # Game loop
        while not self._is_game_over():
            player = self.players[self.current_player]
            print(f"{player.color.name}'s turn")

            # Get move from the player
            move = self._get_player_move(player)

            # Make the move on the board
            player.make_move(self.board, move)

            # Switch to next player
            self.current_player = (self.current_player + 1) % 2

        # Display the result of the match
        self._display_result()

    def _is_game_over(self) -> bool:
        return (self.board.is_check_mate(Color.WHITE) or self.board.is_stalemate(Color.WHITE)
                or self.board.is_check_mate(Color.BLACK) or self.board.is_stalemate(Color.BLACK))

    def _get_player_move(self, player) -> Move:
        # TODO: Implement logic to get a valid move from the player
        source_row = int(input("Enter the source row of the piece you which to move"))
        source_col = int(input("Enter the source col of the piece you which to move"))
        dest_row = int(input("Enter the destination row of the piece you which to move"))
        dest_col = int(input("Enter the source destination of the piece you which to move"))

        piece = self.board.get_piece(source_row, source_col)

        move = Move(piece, dest_row, dest_col)
        if piece is None or piece.color != player.color:
            raise Exception("Invalid piece selection!")
        return move

    def _display_result(self) -> None:
        if self.board.is_check_mate(Color.WHITE):
            print("Black wins by checkmate!")
        elif self.board.is_check_mate(Color.BLACK):
            print("White wins by checkmate!")
        elif self.board.is_stalemate(Color.WHITE) or self.board.is_stalemate(Color.BLACK):
            print("The game ends in a stalemate!")
