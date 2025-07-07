import logging
import socket
import threading
import time
#Note : https://wiki.python.org/moin/UdpCommunication

class RemoteCommand:
    def __init__(self, p_host, p_port, p_loglevel):
        self.sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
        logging.basicConfig(level=p_loglevel.upper())
        logging.info(f"Start RemoteCommand {p_host}:{p_port}")
        self.host = p_host
        self.port = p_port

        self.thread_cmd_user = threading.Thread(target=self.send_command)
        self.thread_readport = threading.Thread(target=self.readport, daemon=True)
        self.readport = False
        self.start()

    def send_command(self):
        while True:
            try:
                cmd = input("> ")
                logging.info(f"send_command {cmd}")
                if cmd.lower() in ('exit', 'quit'):
                    self.__close()
                    break
                else:
                    logging.info(f"[snd] send_command {cmd}")
                    self.__send(cmd)
                
            except Exception as e:
                logging.error("[ERREUR ENVOI] :", e)
                break
    
    def readport(self):
        while self.readport:
            try:
                # todo 
                # data = self.sock.recv(1024)
                #if not data:
                #    print("Connexion fermée par le serveur.")
                # else:    
                # print("[REÇU] :", data.decode())
                logging.info("[REÇU] :")
                time.sleep(10)
            except Exception as e:
                logging.error("[ERREUR ENVOI] :", e)
                break
    
    def __close(self):
        logging.info(f"Exit RemoteCommand {self.host}:{self.port}")
        self.readport = False
        self.thread_readport.join()
        exit(0)

    def __send(self, p_cmd):
        logging.info(f"[snd] send_command {p_cmd}")
        # self.sock.sendto(p_cmd, (self.host, self.port))


    def start(self):
        self.readport = True
        self.thread_cmd_user.start()
        self.thread_readport.start()