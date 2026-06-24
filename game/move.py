from game.rules import can_move_piece


def move_piece(board, from_square, to_square):
    if not can_move_piece(board, from_square, to_square):
        return board, False

    new_board = board.copy()
    moving_piece = new_board[from_square]

    new_board[to_square] = moving_piece
    del new_board[from_square]

    return new_board, True
