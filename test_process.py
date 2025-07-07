import subprocess
import time

command = [
    'python', '-m', 'remotecommand',
    '--host', '123.0.0.1',
    '--port', '12345'
]

def readProcess():
    # Lancer et lire stdout/stderr en temps réel
    # Lance la commande
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # Combine stdout et stderr
        text=True,                 # Pour avoir des chaînes (pas des bytes)
        bufsize=1                  # Pour forcer le flush ligne par ligne
    )

    # Lit la sortie ligne par ligne en temps réel
    try:
        for line in process.stdout:
            print("REMOTE >>", line.strip())
    finally:
        process.stdout.close()
        process.wait()

def writecommand():
    process = subprocess.Popen(
    command,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
    )

    # Envoie une commande
    stdout, stderr = process.communicate(input='quit\n')

    print("Output:", stdout)
    print("Errors:", stderr)

def autretest():
    # Lance le processus
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1  # Ligne par ligne
    )
    # Liste de commandes à envoyer automatiquement
    commands_to_send = [
        'whoami\n',
        'ls\n',
        'exit\n'    
    ]
    # Fonction pour lire la sortie en temps réel
    def read_output(proc):
        for line in proc.stdout:
            print("REMOTE >>", line.strip())
            # Envoie les commandes une par une
    for cmd in commands_to_send:
        print(f"Sending: {cmd.strip()}")
        process.stdin.write(cmd)
        process.stdin.flush()
        time.sleep(1)  # Pause pour laisser la commande s'exécuter

    # Ferme les flux
    process.stdin.close()
    read_output(process)
    process.wait()

autretest()