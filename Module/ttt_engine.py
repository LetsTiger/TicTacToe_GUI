
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#           LAN TTT - Engine              #
#                                         #
#                                         #
#  Author: Diego Zetre & Lukas Malleier   #
#                                         #
#      Newest Version: Stable V 1.2       #
#                                         #
#                © 2024                   #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

import random

# TicTacToe Engine
class TicTacToeBoard:
    """
    Die Klasse 'TicTacToeBoard' repräsentiert das Board für Tic-Tac-Toe.

    Attributes:
        board (list): Eine Liste, die den Zustand des Boards repräsentiert.
        players (list): Eine Liste der Spielerzeichen ('X' und 'O').
        current_player (str): Das Zeichen des aktuellen Spielers.

    Methods:
        __init__(): Initialisiert das Board mit leeren Feldern, definiert die Spielerzeichen und wählt zufällig den Startspieler aus.
        make_move(position): Platziert das Zeichen des aktuellen Spielers an der angegebenen Position auf dem Board.
        is_winner(): Überprüft, ob es einen Gewinner gibt und gibt das Zeichen des Gewinners zurück.
        is_board_full(): Überprüft, ob das Board voll ist.
        display_board(): Zeigt das aktuelle Board an.
    """
    def __init__(self):
        """
        Initialisiert ein neues Tic-Tac-Toe-Spielbrett.

        Parameters:
            None

        Returns:
            None
        """
        self.board = [' ' for _ in range(9)] # Board leer erstellen
        self.players = ['X','O'] # Spieler Zeichen definieren
        self.current_player = random.choice(self.players) # Zufälligen Spieler der anfangen soll auswählen

    # Funktion um ein Zeichen auf dem Board zu platzieren
    def make_move(self, position):
        """
        Platziert das Zeichen des aktuellen Spielers an der angegebenen Position auf dem Board.

        Parameters:
            position (int): Die Position auf dem Board, an der das Zeichen platziert werden soll.

        Returns:
            str: Bestätigungsmeldung für einen erfolgreichen Zug oder eine Fehlermeldung.
        """
        # Überprüfen ob die eingegebene Position eine Ganzzahl ist - wenn nicht Fehlermeldung zurück
        try:
            position = int(position)
        except:
            return "\nBitte gib eine Ganzzahl ein."
        
        # Überprüfen ob die eingegebene Position zwischen 1 und 9 liegt - wenn nicht Fehlermeldung zurück
        if not (1 <= position <= 9):
            return "\nBitte gib nur eine Zahl zwischen 1 und 9 ein."
        
        # Überprüfen ob die Position bereits belegt ist - wenn ja Fehlermeldung zurück
        if self.board[position - 1] != ' ':
            return f"\nDieses Feld ({position}) ist bereits belegt! Bitte wähl eine anderes Feld."
        
        # Falls alle vorherigen Tests erfolgreich - Zeichen des aktuellen Spielers an die Position im Board setzen
        self.board[position - 1] = self.current_player

        # Aktuellen Spieler wechseln
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        elif self.current_player == self.players[1]:
            self.current_player = self.players[0]
        else:
            return "Es ist ein Fehler aufgetreten bitte starte das Spiel neu!"
        
        # Wenn alles geklappt hat bestätigen, dass der Zug erfolgreich war
        return "positive move"

    # Funktion zur Überprüfung ob es einen Gewinner gibt
    def is_winner(self):
        """
        Überprüfung ob es einen Gewinner gibt.

        Parameters:
            None

        Returns:
            str or None: Das Zeichen des Gewinners oder None, wenn es keinen Gewinner gibt.
        """
        # Horizontale Überprüfung 
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != ' ':
                return self.board[i] # Rückgabe des Spielers der gewonnen hat

        # Vertikale Überprüfung
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                return self.board[i] # Rückgabe des Spielers der gewonnen hat

        # Diagonale Überprüfung
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0] # Rückgabe des Spielers der gewonnen hat
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2] # Rückgabe des Spielers der gewonnen hat

        # Kein Gewinner gefunden
        return None

    # Funktion zur Überprüfung ob das Board voll ist
    def is_board_full(self):
        """
        Überprüft, ob das Board voll ist.

        Parameters:
            None

        Returns:
            bool: True, wenn das Board voll ist, False sonst.
        """
        if ' ' in self.board:
            return False # Board nicht voll
        else:
            return True # Board voll

    # Funktion um das aktuelle Board anzuzeigen
    def display_board(self, action='print'):
        """
        Zeigt das aktuelle Board an oder gibt eine Dictionary mit dem Board zurück.

        Parameters:
            action (str, optional): Die Aktion, die durchgeführt werden soll. 
            - 'print': (Standard) Das Board wird auf der Konsole ausgegeben.
            - 'send': eine Liste mit der strukturierten Darstellung des Boards

        Returns:
            None or dict: 
                - Wenn 'action == print', dann wird das Board auf der Konsole ausgegeben und 'None' zurückgegeben.
                - Wenn 'action == send', dann wird eine Liste mit der strukturierten Darstellung des Boards zurückgegeben
                - Bei ungültiger 'action' wird 'None' zurückgegeben.
        """
        # Eine Liste mit dem Board erstellen
        board_to_display = [
                f"\n",
                f" {self.board[0]} | {self.board[1]} | {self.board[2]} ",
                f"---|---|---",
                f" {self.board[3]} | {self.board[4]} | {self.board[5]} ",
                f"---|---|---",
                f" {self.board[6]} | {self.board[7]} | {self.board[8]} "
        ]

        board_to_send = [self.board[0],self.board[1],self.board[2],self.board[3],self.board[4],self.board[5],self.board[6],self.board[7],self.board[8]]

        # Überprüfen welche action ausgewählt wurde
        if action == "print":
            # Ausgabe des Boards
            for i in board_to_display: 
                print(i)
        elif action == "send":
            # Liste zurückgeben
            return board_to_display
        elif action == "gui":
            return board_to_send
        else:
            return None

def local_game():
    return
    new_board = TicTacToeBoard() # Neues Board erstellen

    while new_board.is_winner() is None and not new_board.is_board_full(): # Spiel geht solange es keinen Gewinner gibt und das Board nicht voll ist

        new_board.display_board() # Board das erste mal anzeigen (leer)
        status = None

        while not status == 'positive move': # Überprüfung ob aktueller Zug möglich ist
            chocen_position = input(f"\nGib das Feld (1-9) ein auf dem du deine Markierung ({new_board.current_player}) platzieren willst: ") # Eingabe des aktuellen Spielers
            
            status = new_board.make_move(chocen_position) # Übergabe an Engine
            if status != 'positive move': # Rückgabe Überprüfung (falls erfolgreich soll nicht 'positive move angezeigt werden')
                print(status) # Falls eine Fehlermeldung vorhanden ist wird diese ausgegeben

        if new_board.is_winner() is not None: # Überprüfung ob es einen Gewinner gibt
            new_board.display_board() # Board mit komplettem Spiel anzeigen
            print(f"\n{new_board.is_winner()} hat diese Runde gewonnen.") # Ausgabe des Spielausgangs
        elif new_board.is_board_full(): # Überprüfung ob das Board voll ist -> Unentschieden
            new_board.display_board() # Board mit komplettem Spiel anzeigen
            print(f"\nDiese Runde endet unentschieden.") # Ausgabe des Spielausgangs