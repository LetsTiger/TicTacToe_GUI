
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#           LAN TTT - Server              #
#                                         #
#                                         #
#  Author: Diego Zetre & Lukas Malleier   #
#                                         #
#      Newest Version: Stable V 1.2       #
#                                         #
#                © 2024                   #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

import socket
from Module.ttt_engine import TicTacToeBoard
from Module.sock_comm import SocketCommunication

# Hostadresse und Port angeben
HOST = ''
PORT = 61111

class TicTacToeServer(SocketCommunication):
    """
    Klasse für alle Daten des Server-Spielers und des Spielablaufs

    Attribute:
        engine -> TicTacToeBoard: die Hauptengine des Spiels

    Methoden:
        get_move(first: bool) -> str: holt Spielzug
        start_game() -> None: Hauptspielloop
    """
    def __init__(self, sock: socket.socket, addr):
        super().__init__(sock)  # parent initialisieren
        self.engine = TicTacToeBoard()  # Engine erstellen
        print("Verbunden mit:", addr)

    def get_move(self, first: bool) -> str:
        """
        holt Spielzug von Client-Spieler oder Server-Spieler (local über stdin)

        Parameters:
            first -> bool: True wenn es der erste Versuch einer richtigen Eingabe ist

        Returns:
            str: Eingabe des Spielers
        """
        engine = self.engine

        # Prüfung des aktiven Spielers
        if engine.current_player == engine.players[1]:
            # einmal pro Spielzug Info und Spielfeld an nicht aktiven Spieler senden
            if first:
                board_to_send = engine.display_board('send')
                self.socket_communication('send', board_to_send)
                self.socket_communication("send", "\nAnderer Spieler an der Reihe")

            engine.display_board() 
            # Eingabe des aktuellen Spielers
            chosen_position = input(f"\nGib das Feld (1-9) ein auf dem du deine Markierung ({engine.current_player}) platzieren willst: ")
        else:
            # einmal pro Spielzug Info und Spielfeld für nicht aktiven Spieler ausgeben
            if first:
                engine.display_board("print")
                print("\nAnderer Spieler an der Reihe")

            board_to_send = engine.display_board('send')
            self.socket_communication('send', board_to_send)
            # Client-Spieler um Eingabe bitten
            self.socket_communication('send', f"\nGib das Feld (1-9) ein auf dem du deine Markierung ({engine.current_player}) platzieren willst: ")
            # Eingabe des aktuellen Spielers
            chosen_position = self.socket_communication("recieve")

        return chosen_position

    def start_game(self):
        """
        Kümmert sich um den Ablauf des gesamten Spiels.
        Überprüft ob das Spiel noch läuft und wer der Gewinner ist

        """
        engine = self.engine    # reduziert nachfolgende Schreibaufwand: 'self.engine' auf 'engine'
        first = True
        while engine.is_winner() is None and not engine.is_board_full(): # Überprüfung ob das Spiel noch läuft
            chosen_position = self.get_move(first)  # Spielzug des Spielers

            if chosen_position == None: # Wenn keine Position vorhanden ist, ist der Gegenüber nicht mehr verbunden
                print("Verbindung geschlossen")
                return

            status = engine.make_move(chosen_position)  # Aufruf an die engine mit der Position

            if status != 'positive move':   # ungültige Eingabe
                first = False
                if engine.current_player == engine.players[1]:
                    print(status)
                else:
                    self.socket_communication("send", status)
            else:
                # bei richtiger Eingabe wird die first-try Variable rückgesetzt
                first = True

        # Ablauf des Spielendes:

        # Spielfeld anzeigen
        engine.display_board()
        board = engine.display_board("send")
        self.socket_communication("send", board)

        # Gewinner wird ermittelt
        if winner := engine.is_winner():
            if winner == engine.players[1]:
                print(f"\nDu ({winner}) hast diese Runde gewonnen.")
                self.socket_communication("send", f"Du ({engine.players[0]}) hast diese Runde verloren")
            else:
                print(f"\nDu ({engine.players[1]}) hast diese Runde verloren.")
                self.socket_communication("send", f"Du ({winner}) hast diese Runde gewonnen")
        # Falls das Spielfeld voll ist -> unentschieden
        elif engine.is_board_full():
            message = f"\nDiese Runde endet unentschieden."
            print(message)
            self.socket_communication("send", message)
        self.socket_communication("send", "gameend")


if __name__ == "__main__":
    # Socket erstellen
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    
    # auf Client-Verbindung warten
    print(f"\nServer bereit. Warte auf Client.")
    clientsocket, address = s.accept()

    # TicTacToeServer initialisieren
    server = TicTacToeServer(clientsocket, address)

    # Spiel starten
    server.start_game()

    s.close()

    input("<Enter> zum schließen")
