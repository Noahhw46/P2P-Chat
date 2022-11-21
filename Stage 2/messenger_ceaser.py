import socket
import threading
import argparse
import sys
import os



def ceaser_cipher(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) + key - 65) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message


def parse_args():
    parser = argparse.ArgumentParser(description="Messenger: type /quit to exit the program during a connection")
    parser.add_argument("--host", help="Host to connect to", type=str, default="localhost")
    parser.add_argument("--port", help="Port to connect to", type=int, required=True)
    parser.add_argument("--timeout", help="Timeout for connection", type=int, default=10)
    parser.add_argument("--mode", help="Mode to run in, either 'start' or 'connect'", default="connect")

    return parser.parse_args()


class Messenger:

    def __init__(self, host, port, mode):
        self.host = host
        self.port = port
        self.mode = mode
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def start(self): 
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Listening on {self.host}:{self.port}")
        return self.sock
 

    def get_connect(self): 
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
        except:
            print("Could not make a connection to that client\n")
        else:
            print("Connection made")
            return self.sock
        print("Connection timed out")


    def receive(self, socket, signal, key): 
        while signal:
            try:
                data = socket.recv(32)
                message = ceaser_cipher(str(data.decode("utf-8")), key)
                print(message)
            except KeyboardInterrupt:
                print("You have been disconnected from the server")
                signal = False
                break

    def new_connection(self, socket, key):
        self.sock, self.address = socket.accept()
        print("Connection made at {}".format(self.address))
        receiveThread = threading.Thread(target = self.receive, args = (self.sock, True, key))
        receiveThread.start()

    def send(self, key):
        while True:
            message = input()
            if message == "/quit":
                os._exit(os.X_OK)
            else:
                message = ceaser_cipher(message, key)
                self.sock.send(message.encode("utf-8"))
        




def main():  
    args = parse_args()
    messenger = Messenger(args.host, args.port, args.mode) 
    if args.mode == "start": 
        sock = messenger.start()
        key = int(input("Enter a key: "))
        messenger.new_connection(sock, -key)
        messenger.send(key)
    elif args.mode == "connect":
        sock = messenger.get_connect()
        key = int(input("Enter a key: "))
        recieveThread = threading.Thread(target = messenger.receive, args = (sock, True, -key))
        recieveThread.start()
        messenger.send(key)
    else:
        print("Invalid mode")
        sys.exit(1)


main()




    
    
