from piece import Piece

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row, dest_col) -> bool:
        # Moves one square in any direction.
        # The king is not a very powerful piece, as it can only move (or capture) one square in any direction.
        # Please note that the king cannot be captured! When a king is attacked, it is called "check."
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        return row_diff <= 1 and col_diff <= 1