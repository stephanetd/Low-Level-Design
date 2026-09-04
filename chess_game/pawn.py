from piece import Piece
from color import Color

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row, dest_col) -> bool:
        # Moves one square forward, but on its first move, it can move two squares forward.
        # It attacks (or captures) each square diagonally to the left or right.
        row_diff = dest_row - self.row # up (pawns can't go backwards)
        col_diff = abs(dest_col - self.col) # left - right

        if self.color == Color.WHITE:
            # moves one square forward vertically
            # moves two squares forward if first move
            # moves diagonally
            return ((row_diff == 1 and col_diff == 0)
                    or (self.row == 1 and row_diff == 2 and col_diff == 0)
                    or (row_diff == 1 and col_diff == 1 and board.get_piece(dest_row, dest_col) is not None))
        else:
            return ((row_diff == -1 and col_diff == 0)
                    or (self.row == 6 and row_diff == -2 and col_diff == 0)
                    or (row_diff == -1 and col_diff == 1 and board.get_piece(dest_row, dest_col) is not None))

