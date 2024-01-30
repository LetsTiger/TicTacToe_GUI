import GUI.Codes.ui_TTT_Hub as GUI_HUB
import GUI.Codes.ui_TTT_Hub as GUI_HOST
import GUI.Codes.ui_TTT_Hub as GUI_JOIN
import GUI.Codes.ui_TTT_Game as GUI_GAME

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QRunnable
import sys
import Module.ttt_engine as engine
from functools import partial


class Worker(QRunnable):
    def __init__(self, function, args, kwargs):
        super(Worker, self).__init__()
        self.args = args
        self.kwargs = kwargs

    #@pyqtSlot
    def run(self):
        self.function(*self.args, **self.kwargs)

def game():
    """
    Generator Funktion des Spiels
    zum Nutzen einmal next(<Generatorname>) ausführen, diese gibt den aktuellen Spielstand
    für alle weiteren Züge <Generatorname>.send(<Spielzug>) aufrufen (gibt auch aktuellen Spielstand)

    Wenn der Status 4, 5 oder 6 ist, ist ein Spielende erreicht. Für erneuten Spielstart wieder mit next() beginnen.

    Codierung:
        4: Spieler in variable player hat gewonnen
        5: unentschieden
        6: ungültiges Ende
    
    yields:
        (status: int, player: str, board.board: list[str]) : aktueller Spielstand 
    """
    # wenn der Generator nach Spielende nochmal aufgerufen wird fängt das Spiel von vorne an
    while True:
        board = engine.TicTacToeBoard() # Neues Board erstellen
        if "player" in locals():    # wenn die variable player existiert
            board.current_player = board.players[(board.players.index(player) + 1) % 2] # setze den beginnenden Spieler auf den Verlierer der Vorrunde
        
        status = 0  # zu Spielbeginn ist das Spiel noch in gültigem Zustand

        while board.is_winner() is None and not board.is_board_full(): # Spiel geht solange es keinen Gewinner gibt und das Board nicht voll ist
            player = board.current_player
            chosen_position = (yield (status, player, board.board)) # Spielzug annehmen undaktuellen Spielstand zurückgeben
            status = board.make_move(chosen_position) # Übergabe an Engine

        # Spielenden zurückgeben
        if (winner := board.is_winner()) is not None: # Überprüfung ob es einen Gewinner gibt
            yield (4, winner, board.board)
        elif board.is_board_full(): # Überprüfung ob das Board voll ist -> Unentschieden
            yield (5, player, board.board)
        else:
            yield (6, player, board.board)

def set_board(board, buttons):
    """
    setzt eingegebene buttons auf die Werte aus der Liste board

    Parameter:
        board: list[str] : Liste der Positionen
        buttons: list : Liste der Buttons
    """
    for board_spot, button_spot in zip(board, buttons):
        button_spot.setText(board_spot)

def move_handler_local(window_game, game, move):
    """
    schickt Spielzüge an den Spielgenerator und setzt das Spielfeld je nach Eingabe

    Parameter:
        window_game : Qt-Fenster des Spielfelds
        game : Spielgenerator
        move : Spielzug
    """
    status = -1
    try:
        status, current_player, board = game.send(move) # Versuch Eingabe an den Generator zu schicken
    except StopIteration:   # wenn das Ende des Generators erreicht wurde
        return
    
    # Abarbeitung der Verschiedenen Spielmeldungen
    if status == -1:
        # Anderer Error
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "Error während des Spielzuges", None))
    elif status == 0:
        # Zug gültig
        window_game.ui.label_3.setText(QCoreApplication.translate("MainWindow", f"{current_player} ist an der Reihe", None))
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "", None))
    elif status == 1:
        # Eingebe keine Ganzzahl
        window_game.ui.label_3.setText(QCoreApplication.translate("MainWindow", "Eingabe ist keine Ganzzahl", None))
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "", None))
    elif status == 2:
        # Eingabe nicht 1-9
        window_game.ui.label_3.setText(QCoreApplication.translate("MainWindow", "Eingabe nicht zwischen 1-9", None))
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "", None))
    elif status == 3:
        # Nicht frei
        window_game.ui.label_3.setText(QCoreApplication.translate("MainWindow", "Wähle einen freien Platz", None))
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "", None))
    elif status == 4:
        # Gewinner
        window_game.ui.label_3.setText(QCoreApplication.translate("MainWindow", f"{current_player} hat gewonnen!", None))
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "", None))
    elif status == 5:
        # Unentschieden
        window_game.ui.label_3.setText(QCoreApplication.translate("MainWindow", "Unentschieden!", None))
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "", None))
    elif status == 6:
        # Ungültiges Ende
        window_game.ui.label_3.setText(QCoreApplication.translate("MainWindow", "Invalid end", None))
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "Invalid end", None))

    # board setzten
    set_board(board, window_game.buttons_spots)

def change_error_message(message):
    window_ui.label_5.setText(f"{message}")

def start_local_session():
    """
    Hauptfunktion für das Spielen auf lokalem Rechner

    """
    try:
        game_gen = game()   # Generator mit der Funktion game erstellen

        window_game = GUI_GAME.MainWindow() # Spielfenster initialisieren
        # Buttons initialisieren
        for i in range(len(window_game.buttons_spots)): 
            window_game.buttons_spots[i].clicked.connect(partial(move_handler_local, window_game, game_gen, i+1))
        
        window_game.ui.pushButton_10.clicked.connect(window_game.close)
        
        # erster Aufruf des Spiels um aktuelle Daten zu bekommen
        status, current_player, board = next(game_gen)
        # print board
        set_board(board, window_game.buttons_spots)
        
        # Meldungen rücksetzen
        window_game.ui.label_3.setText(QCoreApplication.translate("MainWindow", f"{current_player} ist an der Reihe", None))
        window_game.ui.label_5.setText(QCoreApplication.translate("MainWindow", "", None))

    except Exception as e:
        window_game.close()
        change_error_message(e)

class ServerGame:
    def __init__(self, window_game, game, connection):
        self.window_game = window_game
        self.game = game
        self.status, self.current_player, self.board = next(game)
        self.starting_player = self.current_player
        self.connection = connection

        self.done = False

        set_board(self.board, self.window_game.buttons_spots)
        self.send_to_client(self.status, self.current_player, self.board)

    def get_remote_move(self):
        while not self.done:
            # recieve move
            rdata = ""
            while True:
                rdata += self.connection.recv(1024)

                if rdata[-3:] == b"END":
                    break

            data = rdata.split(b"END")[-2]

            try:
                move = int(data.decode())
            except Exception as ex:
                change_error_message("Remote" + ex)
                self.connection.send(f"8{self.current_player}{self.board}".encode() + b"END")
                continue

            # right player
            if self.current_player == self.starting_player:
                change_error_message("Remote" + "not their turn")
                self.connection.send(f"7{self.current_player}{''.join(self.board)}".encode() + b"END")
                continue

            # try move
            self.status, self.current_player, self.board = self.game.send(move)

            # send response
            self.connection.send(f"{self.status}{self.current_player}{''.join(self.board)}".encode() + b"END")

            set_board(self.board, self.window_game.buttons_spots)
            # set messages

    def remote_game_local_move(self, move):
        if self.current_player == self.starting_player:
            status, current_player, board = self.game.send(move)
            if status == 0:
                self.connection.send(f"{self.status}{self.current_player}{''.join(self.board)}".encode() + b"END")
            else:
                change_error_message(status)
        else:
            change_error_message("not your turn")

class ClientGame:
    def __init__(self, window_game, connection):
        self.connection = connection
        self.window_game = window_game
        self.myTurn = False
        self.board = []
        self.symbol = ""

        self.done = False

    def remote_game_client_move(self, move):
        if isinstance(move, int) and 1 <= move <= 9 and self.myTurn:
            self.connection.send(str(move).encode() + b"END")

    def get_and_update(self):
        first = True
        while True:
            rdata = ""
            while True:
                rdata += self.connection.recv(1024)

                if rdata[-3:] == b"END":
                    break

            if first:
                # get initial conditions
                data = rdata.split(b"END")[0]
            else:
                data = rdata.split(b"END")[-2]

            try:
                status, current_player, board_str = data[0], data[1], data[2:11]
                board = board_str.split("")
                if first:
                    self.symbol = current_player
            except:
                print("test")
                # send invalid input to provoke another message of current game state
                self.connection.send("0".encode() + b"END")
                continue

            if self.symbol == current_player:
                self.myTurn = True

            first = False

            set_board(board, self.window_game.buttons_spots)
            change_error_message(status + " | " + current_player)
            #TODO:: set messages from data



def host_remote_session():
    try:
        # open socket
        # bind address

        window_game = GUI_GAME.MainWindow()

        host_game = ServerGame(window_game, game, connection)

        # Buttons initialisieren
        for i in range(len(window_game.buttons_spots)): 
            window_game.buttons_spots[i].clicked.connect(partial(move_handler_local, window_game, game_gen, i+1))
        
        window_game.ui.pushButton_10.clicked.connect(window_game.close)
        
        # start game
        host_game_loop = Worker(host_game.get_remote_move)

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
