from piece import Piece

class Knight(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row, dest_col) -> bool:
        # Moves in an ‘L-shape,’ two squares in a straight direction, and then one square perpendicular to that.
        # The knight is the only piece in chess that can jump over another piece!
        # The knight can capture only what it lands on, not what it jumps over!
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)