from piece import Piece

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def can_move(self, board, dest_row, dest_col) -> bool:
        # Moves any number of squares horizontally or vertically.
        # It can move as many squares as it likes left or right horizontally,
        # or as many squares as it likes up or down vertically (as long as it isn't blocked by other pieces)
        return self.col == dest_row or self.col == dest_col