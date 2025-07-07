import socket
import threading
import time

# Adresse et port du serveur distant (à adapter si besoin)
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Créer la socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Fonction de lecture depuis la socket
def lire_socket():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Connexion fermée par le serveur.")
                break
            print("[REÇU] :", data.decode())
        except Exception as e:
            print("[ERREUR LECTURE] :", e)
            break

# Fonction d'envoi de commandes (saisie utilisateur)
def envoyer_commandes():
    while True:
        try:
            cmd = input("> ")
            if cmd.lower() in ('exit', 'quit'):
                client_socket.close()
                break
            client_socket.sendall(cmd.encode())
        except Exception as e:
            print("[ERREUR ENVOI] :", e)
            break

# Création des threads
thread_lecture = threading.Thread(target=lire_socket, daemon=True)
thread_envoi = threading.Thread(target=envoyer_commandes)

# Démarrage des threads
thread_lecture.start()
thread_envoi.start()

# Attendre la fin du thread envoi (celui qui quitte en premier)
thread_envoi.join()

print("Client terminé.")