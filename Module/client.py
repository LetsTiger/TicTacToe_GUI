
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#           LAN TTT - Client              #
#                                         #
#                                         #
#  Author: Diego Zetre & Lukas Malleier   #
#                                         #
#      Newest Version: Stable V 1.2       #
#                                         #
#                © 2024                   #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

from Module.sock_comm import SocketCommunication
import socket

# (optional) Hostadresse und Port festlegen
HOST = '127.0.0.1'
PORT = 61111

class TicTacToeClient(SocketCommunication):
    """
    Klasse für alle Daten des Client-Spielers

    Methoden:
        start_game() -> None: Hauptspielloop
    
    """
    def __init__(self, connection):
        super().__init__(connection)    # parent initialisieren
    
    def start_game(self):
        """
        kümmert sich um den Hauptspielloop
        hört auf der angegebenen Schnittstelle und bearbeitet empfangene Daten
        """
        while True:
            rec = self.socket_communication("recieve")
            
            # Socket geschlossen
            if rec == None:
                print("Socket geschlossen!")
                break
            # übertragenes Spielfeld ausgeben
            elif isinstance(rec, list): 
                for line in rec:
                    print(line)
            # Fehler: kein String
            elif not isinstance(rec, str):
                print("Unerwarteter Fehler")
                break
            # Spielzug
            elif rec[1:4] == "Gib":
                move = input(rec)
                if move == "exit":
                    break
                self.socket_communication("send", move)
            # Spielende
            elif rec == "gameend":
                break
            # Infos (z.B.: Anderer Spieler an der Reihe)
            else:
                print(rec)


if "__main__" == __name__:
    print("Willkommen bei TicTacToe")

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket erstellen

    # Verbindungsversuch mit festgelegten Werten
    try:
        connection.connect((HOST, PORT))
    except Exception as ex:
        print("Manuell eingeben:")
        ok = False
    else:
        ok = True

    # nach korrekter Serversocket fragen bis es stimmt oder der Nutzer abbricht
    while not ok:
        serversocket = input("Serverip/URL und Port eingeben <ip|url:port>: ")
        if serversocket == "exit":
            exit()
        serversocket = serversocket.split(":")  # am Doppelpunkt teilen
        try:
            serversocket[1] = int(serversocket[1])  # Port auf integer umwandeln
            connection.connect(tuple(serversocket)) # Verbindungsversuch
        except Exception as ex: # jegliche Fehler wie ValueError oder Error in Verbindung abfangen
            print("Eingabe überprüfen!")
            continue
        else:   # Falls kein Fehler auftritt wird ok auf True gesetzt -> Schleife stoppt
            ok = True
        
    # TicTacToe-Client-Klasse instanziieren
    client = TicTacToeClient(connection)

    # Spiel-Loop starten
    client.start_game()

    connection.close()
    
    input("<Enter> zum schließen")
