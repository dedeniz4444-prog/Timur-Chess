import streamlit as st

from game.board import FILES
from game.setup import create_starting_position
from game.pieces import piece_symbol, PIECE_NAMES_TR
from game.move import move_piece


st.set_page_config(
    page_title="Timur Satrancı",
    page_icon="♟️",
    layout="wide"
)


def init_game():
    if "board" not in st.session_state:
        st.session_state.board = create_starting_position()

    if "selected_square" not in st.session_state:
        st.session_state.selected_square = None

    if "turn" not in st.session_state:
        st.session_state.turn = "white"

    if "move_log" not in st.session_state:
        st.session_state.move_log = []


def reset_game():
    st.session_state.board = create_starting_position()
    st.session_state.selected_square = None
    st.session_state.turn = "white"
    st.session_state.move_log = []


def change_turn():
    if st.session_state.turn == "white":
        st.session_state.turn = "black"
    else:
        st.session_state.turn = "white"


def square_button_label(square):
    piece = st.session_state.board.get(square)

    if piece is None:
        return " "

    return piece_symbol(piece)


def handle_square_click(square):
    board = st.session_state.board
    selected = st.session_state.selected_square
    clicked_piece = board.get(square)

    # Hiçbir şey seçili değilse
    if selected is None:
        if clicked_piece is None:
            return

        if clicked_piece["color"] != st.session_state.turn:
            return

        st.session_state.selected_square = square
        return

    # Aynı kareye tekrar tıklarsan seçimi kaldır
    if selected == square:
        st.session_state.selected_square = None
        return

    moved_board, success = move_piece(board, selected, square)

    if success:
        moving_piece = board.get(selected)
        piece_name = PIECE_NAMES_TR.get(moving_piece["type"], moving_piece["type"])

        st.session_state.board = moved_board
        st.session_state.move_log.append(
            f"{st.session_state.turn}: {piece_name} {selected} → {square}"
        )
        st.session_state.selected_square = None
        change_turn()
    else:
        # Eğer kendi taşına tıklarsa seçimi değiştir
        if clicked_piece is not None and clicked_piece["color"] == st.session_state.turn:
            st.session_state.selected_square = square
        else:
            st.session_state.selected_square = None


def draw_square(square):
    selected = st.session_state.selected_square
    piece = st.session_state.board.get(square)

    label = square_button_label(square)

    if selected == square:
        label = f"🔵{label}"

    if piece is not None:
        if piece["color"] == "white":
            label = f"⚪ {label}"
        else:
            label = f"⚫ {label}"

    if st.button(label, key=f"square_{square}", use_container_width=True):
        handle_square_click(square)


def draw_board():
    st.subheader("Tahta")

    # Siyah taraf üstte görünsün diye 9'dan 0'a çiziyoruz.
    for rank in range(9, -1, -1):
        cols = st.columns(13)

        # Sol saray: x2
        with cols[0]:
            if rank == 8:
                palace_label = "🏯 x2"
                if st.button(palace_label, key="square_x2", use_container_width=True):
                    handle_square_click("x2")
            else:
                st.write("")

        # Ana 11 sütun
        for index, file_name in enumerate(FILES):
            square = f"{file_name}{rank}"

            with cols[index + 1]:
                draw_square(square)

        # Sağ saray: x1
        with cols[12]:
            if rank == 1:
                palace_label = "🏯 x1"
                if st.button(palace_label, key="square_x1", use_container_width=True):
                    handle_square_click("x1")
            else:
                st.write("")


def draw_sidebar():
    st.sidebar.title("Timur Satrancı")

    turn_text = "Beyaz" if st.session_state.turn == "white" else "Siyah"
    st.sidebar.write(f"**Sıra:** {turn_text}")

    if st.session_state.selected_square is None:
        st.sidebar.write("**Seçili kare:** Yok")
    else:
        st.sidebar.write(f"**Seçili kare:** {st.session_state.selected_square}")

    if st.sidebar.button("Yeni oyun"):
        reset_game()
        st.rerun()

    st.sidebar.divider()

    st.sidebar.subheader("Hamle geçmişi")

    if len(st.session_state.move_log) == 0:
        st.sidebar.write("Henüz hamle yok.")
    else:
        for move_text in reversed(st.session_state.move_log[-20:]):
            st.sidebar.write(move_text)


def draw_rules_note():
    with st.expander("Bu sürümde ne var?"):
        st.write(
            """
            Bu ilk sürümde amaç tahta sistemini çalıştırmak.

            Şu anda:
            - Taşlar seçilip taşınabilir.
            - Sıra sistemi vardır.
            - Kendi taşını yiyemezsin.
            - Saraya sadece şah girebilir.

            Henüz yok:
            - Gerçek Timur satrancı hamle kuralları
            - Şah çekme
            - Mat / pat
            - Piyon terfileri
            - Şahın özel yer değiştirme hakkı
            """
        )


init_game()

st.title("♟️ Timur Satrancı")
st.caption("Az bilinen tarihî bir satranç türünü dijitale taşıma projesi.")

draw_sidebar()
draw_rules_note()
draw_board()
