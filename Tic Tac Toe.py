import GUI.Codes.ui_TTT_Hub as GUI_HUB
import GUI.Codes.ui_TTT_Hub as GUI_HOST
import GUI.Codes.ui_TTT_Hub as GUI_JOIN
import GUI.Codes.ui_TTT_Game as GUI_GAME

from PySide6.QtCore import QCoreApplication
import sys
import Module.ttt_engine as engine
from functools import partial


def game():
    """
    beim aufrufen immer:
        zuerst: next()
        danach: .send()

    am Ende (wenn status 4, 5 oder 6) spiel beenden

    Codierung:
        4: winner is player
        5: tie
        6: invalid end
    """
    board = engine.TicTacToeBoard() # Neues Board erstellen
    status = 0

    while board.is_winner() is None and not board.is_board_full(): # Spiel geht solange es keinen Gewinner gibt und das Board nicht voll ist
        player = board.current_player
        yield (status, player, board.board)

        chosen_position = (yield (status, player, board.board))

        status = board.make_move(chosen_position) # Übergabe an Engine

    if (winner := board.is_winner()) is not None: # Überprüfung ob es einen Gewinner gibt
        yield (4, winner, board.board)
    elif board.is_board_full(): # Überprüfung ob das Board voll ist -> Unentschieden
        yield (5, player, board.board)
    yield (6, player, board)

def set_board(board, buttons):
    for board_spot, button_spot in zip(board, buttons):
        button_spot.setText(board_spot)

def move_handler(window_game, game, move):
    print(int(move))
    game.send(move)

    status, current_player, board = next(game)

    print(status, current_player, board)

    # print board
    set_board(board, window_game.buttons_spots)

    if status == 4:
        winner = current_player
        change_error_message(f"Winner: {winner}")
    elif status == 5:
        # no winner, tie
        change_error_message("tie")
    elif status == 6:
        # invalid end
        change_error_message("invalid end")

    if status in (4, 5, 6):
        game.close()
        window_game.close()


def change_error_message(message):
    window_ui.label_5.setText(f"{message}")

def start_local_session():
    try:
        game_gen = game()

        window_game = GUI_GAME.MainWindow()
        for i in range(len(window_game.buttons_spots)):
            window_game.buttons_spots[i].clicked.connect(partial(move_handler, window_game, game_gen, i))
        
        status, current_player, board = next(game_gen)
        # print board
        set_board(board, window_game.buttons_spots)

    except Exception as e:
        change_error_message(e)

def host_remote_session():
    try:
        pass # Host a remote game
    except Exception as e:
        change_error_message(e)

def join_remote_session():
    try:
        pass # Join a remote game
    except Exception as e:
        change_error_message(e)

if __name__ == "__main__":
    hub = GUI_HUB.QApplication(sys.argv)

    window = GUI_HUB.MainWindow()
    window.show()

    window_ui = window.ui
    change_error_message("")

    window_ui.pushButton.clicked.connect(start_local_session)
    window_ui.pushButton_2.clicked.connect(host_remote_session)
    window_ui.pushButton_3.clicked.connect(join_remote_session)

    sys.exit(hub.exec())
