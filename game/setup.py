from game.pieces import create_piece


def create_starting_position():
    board = {}

    # White pieces
    white_row_0 = {
        "a0": "alfil",
        "c0": "camel",
        "e0": "dabbaba",
        "g0": "dabbaba",
        "i0": "camel",
        "k0": "alfil",
    }

    white_row_1 = {
        "a1": "rook",
        "b1": "knight",
        "c1": "talia",
        "d1": "giraffe",
        "e1": "ferz",
        "f1": "king",
        "g1": "wazir",
        "h1": "giraffe",
        "i1": "talia",
        "j1": "knight",
        "k1": "rook",
    }

    white_pawns = {
        "a2": "pawn_pawn",
        "b2": "pawn_dabbaba",
        "c2": "pawn_camel",
        "d2": "pawn_alfil",
        "e2": "pawn_ferz",
        "f2": "pawn_king",
        "g2": "pawn_wazir",
        "h2": "pawn_giraffe",
        "i2": "pawn_talia",
        "j2": "pawn_knight",
        "k2": "pawn_rook",
    }

    # Black pieces
    black_row_9 = {
        "a9": "alfil",
        "c9": "camel",
        "e9": "dabbaba",
        "g9": "dabbaba",
        "i9": "camel",
        "k9": "alfil",
    }

    black_row_8 = {
        "a8": "rook",
        "b8": "knight",
        "c8": "talia",
        "d8": "giraffe",
        "e8": "ferz",
        "f8": "king",
        "g8": "wazir",
        "h8": "giraffe",
        "i8": "talia",
        "j8": "knight",
        "k8": "rook",
    }

    black_pawns = {
        "a7": "pawn_pawn",
        "b7": "pawn_dabbaba",
        "c7": "pawn_camel",
        "d7": "pawn_alfil",
        "e7": "pawn_ferz",
        "f7": "pawn_king",
        "g7": "pawn_wazir",
        "h7": "pawn_giraffe",
        "i7": "pawn_talia",
        "j7": "pawn_knight",
        "k7": "pawn_rook",
    }

    for square, piece_type in white_row_0.items():
        board[square] = create_piece(piece_type, "white")

    for square, piece_type in white_row_1.items():
        board[square] = create_piece(piece_type, "white")

    for square, piece_type in white_pawns.items():
        board[square] = create_piece(piece_type, "white")

    for square, piece_type in black_row_9.items():
        board[square] = create_piece(piece_type, "black")

    for square, piece_type in black_row_8.items():
        board[square] = create_piece(piece_type, "black")

    for square, piece_type in black_pawns.items():
        board[square] = create_piece(piece_type, "black")

    return board
