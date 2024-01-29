import GUI.Codes.ui_TTT_Hub as GUI_HUB
import GUI.Codes.ui_TTT_Hub as GUI_HOST
import GUI.Codes.ui_TTT_Hub as GUI_JOIN
import GUI.Codes.ui_TTT_Hub as GUI_GAME

from PySide6.QtCore import QCoreApplication
import sys
import Module.ttt_engine as engine

def change_error_message(message):
    window_ui.label_5.setText(f"{message}")

def start_local_session():
    try:
        sys.exit()
        engine.local_game()
        pass # Start a local game
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
