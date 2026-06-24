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


st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        max-width: 1500px;
    }

    div[data-testid="stButton"] > button {
        min-height: 58px;
        font-size: 16px;
        border-radius: 10px;
        border: 1px solid rgba(120, 120, 120, 0.35);
        padding: 4px 4px;
        white-space: pre-line;
    }

    div[data-testid="stButton"] > button:hover {
        border: 2px solid #4f8cff;
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True
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

    if "message" not in st.session_state:
        st.session_state.message = "Beyaz başlar. Bir taşa tıkla."


def reset_game():
    st.session_state.board = create_starting_position()
    st.session_state.selected_square = None
    st.session_state.turn = "white"
    st.session_state.move_log = []
    st.session_state.message = "Yeni oyun başladı. Beyaz başlar."


def change_turn():
    if st.session_state.turn == "white":
        st.session_state.turn = "black"
    else:
        st.session_state.turn = "white"


def turn_name():
    if st.session_state.turn == "white":
        return "Beyaz"
    return "Siyah"


def square_button_label(square):
    piece = st.session_state.board.get(square)

    if piece is None:
        return f"\n{square}"

    return f"{piece_symbol(piece)}\n{square}"


def handle_square_click(square):
    board = st.session_state.board
    selected = st.session_state.selected_square
    clicked_piece = board.get(square)

    # Hiçbir şey seçili değilse
    if selected is None:
        if clicked_piece is None:
            st.session_state.message = "Boş kare seçemezsin. Önce kendi taşına tıkla."
            return

        if clicked_piece["color"] != st.session_state.turn:
            st.session_state.message = f"Sıra {turn_name()} tarafında. Rakip taşı seçemezsin."
            return

        st.session_state.selected_square = square
        piece_name = PIECE_NAMES_TR.get(clicked_piece["type"], clicked_piece["type"])
        st.session_state.message = f"{piece_name} seçildi: {square}"
        return

    # Aynı kareye tekrar tıklarsan seçimi kaldır
    if selected == square:
        st.session_state.selected_square = None
        st.session_state.message = "Seçim kaldırıldı."
        return

    # Kendi başka taşına tıklarsan seçimi değiştir
    if clicked_piece is not None and clicked_piece["color"] == st.session_state.turn:
        st.session_state.selected_square = square
        piece_name = PIECE_NAMES_TR.get(clicked_piece["type"], clicked_piece["type"])
        st.session_state.message = f"Seçim değişti: {piece_name} / {square}"
        return

    moved_board, success = move_piece(board, selected, square)

    if success:
        moving_piece = board.get(selected)
        piece_name = PIECE_NAMES_TR.get(moving_piece["type"], moving_piece["type"])

        st.session_state.board = moved_board
        st.session_state.move_log.append(
            f"{turn_name()}: {piece_name} {selected} → {square}"
        )

        st.session_state.selected_square = None
        change_turn()

        st.session_state.message = f"Hamle yapıldı: {piece_name} {selected} → {square}"
    else:
        st.session_state.message = "Bu hamle şu an geçersiz."


def draw_square(square):
    selected = st.session_state.selected_square
    piece = st.session_state.board.get(square)

    label = square_button_label(square)

    if selected == square:
        label = f"🔵 SEÇİLİ\n{label}"

    if st.button(label, key=f"square_{square}", use_container_width=True):
        handle_square_click(square)
        st.rerun()


def draw_palace(square):
    selected = st.session_state.selected_square
    piece = st.session_state.board.get(square)

    if piece is None:
        label = f"🏯\n{square}"
    else:
        label = f"🏯 {piece_symbol(piece)}\n{square}"

    if selected == square:
        label = f"🔵 SARAY\n{label}"

    if st.button(label, key=f"square_{square}", use_container_width=True):
        handle_square_click(square)
        st.rerun()


def draw_board():
    st.subheader("Tahta")

    # Üst koordinatlar
    header_cols = st.columns(13)

    with header_cols[0]:
        st.write("")

    for index, file_name in enumerate(FILES):
        with header_cols[index + 1]:
            st.markdown(f"**{file_name}**")

    with header_cols[12]:
        st.write("")

    # Siyah taraf üstte görünsün diye 9'dan 0'a çiziyoruz.
    for rank in range(9, -1, -1):
        cols = st.columns(13)

        # Sol saray: x2
        with cols[0]:
            if rank == 8:
                draw_palace("x2")
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
                draw_palace("x1")
            else:
                st.write("")


def draw_sidebar():
    st.sidebar.title("Timur Satrancı")

    st.sidebar.write(f"**Sıra:** {turn_name()}")

    if st.session_state.selected_square is None:
        st.sidebar.write("**Seçili kare:** Yok")
    else:
        st.sidebar.write(f"**Seçili kare:** {st.session_state.selected_square}")

    st.sidebar.info(st.session_state.message)

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
            Bu sürümde amaç tahta sistemini çalıştırmak.

            Şu anda:
            - Taşlar seçilip taşınabilir.
            - Sıra sistemi vardır.
            - Kendi taşını yiyemezsin.
            - Saraya sadece şah girebilir.
            - Taşlar geçici emoji/sembol görünümündedir.

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
