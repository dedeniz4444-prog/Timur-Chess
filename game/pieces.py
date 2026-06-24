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
    "king": "👑",
    "wazir": "🛡️",
    "ferz": "⚔️",
    "giraffe": "🦒",
    "talia": "📐",
    "knight": "🐴",
    "rook": "🏰",
    "alfil": "🐘",
    "camel": "🐫",
    "dabbaba": "⚙️",

    "pawn_pawn": "♟️",
    "pawn_dabbaba": "♟️⚙️",
    "pawn_camel": "♟️🐫",
    "pawn_alfil": "♟️🐘",
    "pawn_ferz": "♟️⚔️",
    "pawn_king": "♟️👑",
    "pawn_wazir": "♟️🛡️",
    "pawn_giraffe": "♟️🦒",
    "pawn_talia": "♟️📐",
    "pawn_knight": "♟️🐴",
    "pawn_rook": "♟️🏰",
}


COLOR_MARKS = {
    "white": "⚪",
    "black": "⚫",
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

    color_mark = COLOR_MARKS.get(color, "")
    symbol = PIECE_SYMBOLS.get(piece_type, "?")

    return f"{color_mark} {symbol}"
