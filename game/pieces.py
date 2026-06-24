PIECE_NAMES_TR = {
    "king": "Şah",
    "wazir": "Vezir",
    "ferz": "General",
    "giraffe": "Zürafa",
    "talia": "Kazık",
    "knight": "At",
    "rook": "Kale",
    "alfil": "Alfil",
    "camel": "Deve",
    "dabbaba": "Savaş Motoru",

    "pawn_pawn": "Piyon Piyonu",
    "pawn_dabbaba": "Savaş Motoru Piyonu",
    "pawn_camel": "Deve Piyonu",
    "pawn_alfil": "Alfil Piyonu",
    "pawn_ferz": "General Piyonu",
    "pawn_king": "Şah Piyonu",
    "pawn_wazir": "Vezir Piyonu",
    "pawn_giraffe": "Zürafa Piyonu",
    "pawn_talia": "Kazık Piyonu",
    "pawn_knight": "At Piyonu",
    "pawn_rook": "Kale Piyonu",
}


PIECE_SYMBOLS = {
    "white": {
        "king": "♔",
        "wazir": "V",
        "ferz": "G",
        "giraffe": "Z",
        "talia": "T",
        "knight": "A",
        "rook": "K",
        "alfil": "F",
        "camel": "D",
        "dabbaba": "M",

        "pawn_pawn": "p",
        "pawn_dabbaba": "m",
        "pawn_camel": "d",
        "pawn_alfil": "f",
        "pawn_ferz": "g",
        "pawn_king": "ş",
        "pawn_wazir": "v",
        "pawn_giraffe": "z",
        "pawn_talia": "t",
        "pawn_knight": "a",
        "pawn_rook": "k",
    },
    "black": {
        "king": "♚",
        "wazir": "v",
        "ferz": "g",
        "giraffe": "z",
        "talia": "t",
        "knight": "a",
        "rook": "k",
        "alfil": "f",
        "camel": "d",
        "dabbaba": "m",

        "pawn_pawn": "P",
        "pawn_dabbaba": "M",
        "pawn_camel": "D",
        "pawn_alfil": "F",
        "pawn_ferz": "G",
        "pawn_king": "Ş",
        "pawn_wazir": "V",
        "pawn_giraffe": "Z",
        "pawn_talia": "T",
        "pawn_knight": "A",
        "pawn_rook": "K",
    }
}


def create_piece(piece_type, color):
    return {
        "type": piece_type,
        "color": color,
    }


def piece_symbol(piece):
    if piece is None:
        return ""

    piece_type = piece["type"]
    color = piece["color"]

    return PIECE_SYMBOLS[color].get(piece_type, "?")
