import socket
import threading
import argparse
import sys
import os

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

    # This is a method for messenger objects in start mode - it binds the socket to the host and port and listens for connections
    def start(self): 
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Listening on {self.host}:{self.port}")
        return self.sock
 
    # This is a method for messenger objects in connect mode - it connects to the host and port 
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

    # This method receives messages from the socket and prints them to the screen
    def receive(self, socket, signal): 
        while signal:
            try:
                data = socket.recv(32)
                print(str(data.decode("utf-8")))
            except KeyboardInterrupt:
                print("You have been disconnected from the server")
                signal = False
                break

    # This is horribly disorganized, but it seems to work. 
    # It creates a new thread for each connection and runs the receive method in that thread. 
    # The reason it's so disorganized is because I'm lazy and the threading for objects in start mode is different than the threading for objects in connect mode.
    def new_connection(self, socket):
        self.sock, self.address = socket.accept()
        print("Connection made at {}".format(self.address))
        receiveThread = threading.Thread(target = self.receive, args = (self.sock, True))
        receiveThread.start()

    # This method sends messages to the socket
    # I assume I could have used something other than sendall, like sendto, but then I would have had to keep track of the address and port of the client, and this was simple enough
    def send(self):
        while True:
            message = input()
            if message == "/quit":
                os._exit(os.X_OK)
            self.sock.sendall(str.encode(message))
        




def main():  
    args = parse_args()
    messenger = Messenger(args.host, args.port, args.mode) #Create a messenger object with the arguments passed in
    if args.mode == "start": 
        sock = messenger.start()
        messenger.new_connection(sock)
        messenger.send()
    elif args.mode == "connect":
        sock = messenger.get_connect()
        recieveThread = threading.Thread(target = messenger.receive, args = (sock, True)) #Create a thread for receiving messages. 
        recieveThread.start() #This is necessary because the receive method will run until a message is received or the connection is closed, and we don't want the program to hang while waiting for a message, since we want to be able to send messages as well.
        messenger.send()
    else:
        print("Invalid mode")
        sys.exit(1)


main()




    
    
