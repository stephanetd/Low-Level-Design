from board import Board
from move import Move

class Player:
    def __init__(self, color):
        self.color = color

    def make_move(self, board: Board, move: Move) -> None:
        piece = move.piece
        dest_row = move.dest_row
        dest_col = move.dest_col

        if board.is_move_valid(piece, dest_row, dest_col):
            source_row = piece.row
            source_col = piece.col
            board.set_piece(piece, dest_row, dest_col)
            board.set_piece(None, source_col, source_row)
            piece.row = dest_row
            piece.col = dest_col
        else: raise Exception("Invalid move!")