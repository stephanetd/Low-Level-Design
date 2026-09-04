from piece import Piece

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row, dest_col) -> bool:
        # Moves any number of squares diagonally, horizontally, or vertically.
        # An easy way to remember how a queen can move is that it moves like a rook and a bishop combined!
        row_diff = abs(dest_row - self.row)
        col_diff = abs(dest_col - self.col)
        return (row_diff == col_diff) or (self.row== dest_row or self.col == dest_col)