
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#     LAN TTT - Socket Communication      #
#                                         #
#                                         #
#  Author: Diego Zetre & Lukas Malleier   #
#                                         #
#      Newest Version: Stable V 1.2       #
#                                         #
#                © 2024                   #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

import pickle
from typing import Literal

class SocketCommunication:
    """
    Die Klasse 'SocketCommunication' ermöglicht die Kommunikation über einen Socket.

    Attributes:
        connection: Die Socket-Verbindung.
        BUFFER (list): Eine Liste zum Zwischenspeichern von Daten.

    Methods:
        send(data): Sendet Daten über die Socket-Verbindung.
        receive(): Empfängt Daten über die Socket-Verbindung.
        socket_communication(action, data=None): Führt Socket-Kommunikationsaktionen durch (senden oder empfangen).
    """
    def __init__(self, connection) -> None:
        """
        Initialisiert eine SocketCommunication-Instanz.

        Parameters:
            connection: Die Socket-Verbindung.

        Returns:
            None
        """
        self.connection = connection
        self.BUFFER = list()

    def send(self, data):
        """
        Sendet Daten über die Socket-Verbindung.

        Parameters:
            data: Die zu sendenden Daten.

        Returns:
            None, falls ein Fehler auftritt.
        """
        # Versuch die Daten zu senden
        try:
            s_data = pickle.dumps(data) # Daten serialisieren
            self.connection.send(s_data) # Daten senden
            self.connection.send(b'EOT') # Fügt Suffix zu den Daten hinzu
        except Exception as ex:
            return None # Sollte ein Fehler auftreten, wird dieser hier abgefangen

    def receive(self):
        """
        Empfängt Daten über die Socket-Verbindung.

        Returns:
            Die empfangenen Daten, falls erfolgreich, andernfalls None.
        """
        # Wenn der BUFFER nicht leer ist
        if self.BUFFER:
            return_data = self.BUFFER[0] # Die ersten gespeicherten Daten im BUFFER abrufen
            self.BUFFER = self.BUFFER[1:] # Die gespeicherten Daten aus dem BUFFER entfernen
            return pickle.loads(return_data) # Deserialisieren und zurückgeben

        # Falls BUFFER leer
        r_data = b'' 

        while True:
            # Versuch Daten zu empfangen
            try:
                r_data += self.connection.recv(1024) # Bereit etwas zu empfangen
                if not r_data: # Falls r_data ungültig ist
                    raise ValueError
            except Exception:
                return None  # Sollte ein Fehler auftreten, wird dieser hier abgefangen

            # Falls die letzten drei Bytes der empfangenen Daten der EndOfTransmit-Flag entsprechen (= Ende der Übertragung)
            if r_data[-3:] == b"EOT":
                break
        
        data = r_data.split(b"EOT")[:-1] # Teile die Daten am EndOfTransmit-Flag; Entferne das leere '' am Ende
        self.BUFFER = data[1:] # BUFFER mit verbleibenden Daten (nach dem split) aktualisieren
        return pickle.loads(data[0]) # Deserialisieren und erste Daten zurückgeben
        

    def socket_communication(self, action: Literal["send", "recieve"], data=None):
        """
        Führt Socket-Kommunikationsaktionen durch (senden oder empfangen).

        Parameters:
            action (Literal["send", "recieve"]): Die auszuführende Aktion (senden oder empfangen).
            data: Die zu sendenden Daten (nur erforderlich, wenn action == "send").

        Returns:
            Die empfangenen Daten (falls action == "recieve") oder None bei einem Fehler oder ungültiger Aktion.
        """

        # Überprüfung, ob beim Senden der Methode Daten mitgegeben wurden
        if action == "send" and not data:
            return None
        
        # Überprüfung, ob etwas gesendet werden soll (falls ja -> auch Überprüfung, ob Daten mitgegeben wurden)
        if action == "send":
            return self.send(data)

        # Überprüfung, ob etwas gesendet werden soll
        if action == "recieve":
            return self.receive()
