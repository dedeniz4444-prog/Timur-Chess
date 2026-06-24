FILES = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
RANKS = list(range(10))

PALACES = {
    "x1": {
        "owner": "white",
        "side": "right",
        "near_rank": 1,
    },
    "x2": {
        "owner": "black",
        "side": "left",
        "near_rank": 8,
    },
}


def make_square(file_name, rank):
    return f"{file_name}{rank}"


def all_board_squares():
    squares = []

    for rank in RANKS:
        for file_name in FILES:
            squares.append(make_square(file_name, rank))

    return squares


def is_normal_square(square):
    return square in all_board_squares()


def is_palace(square):
    return square in PALACES


def is_valid_square(square):
    return is_normal_square(square) or is_palace(square)
