from game.board import is_valid_square, is_palace


def can_move_piece(board, from_square, to_square):
    if from_square == to_square:
        return False

    if not is_valid_square(from_square):
        return False

    if not is_valid_square(to_square):
        return False

    moving_piece = board.get(from_square)

    if moving_piece is None:
        return False

    target_piece = board.get(to_square)

    # Kendi taşını yiyemezsin.
    if target_piece is not None:
        if target_piece["color"] == moving_piece["color"]:
            return False

    # Saraylara şimdilik sadece şah girebilir.
    if is_palace(to_square):
        if moving_piece["type"] != "king":
            return False

    return True
