from piece import Piece

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row, dest_col) -> bool:
        # Moves any number of squares diagonally.
        # It can capture an enemy piece by moving to the occupied square where the piece is located.
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        return row_diff == col_diff