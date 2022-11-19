import socket
import threading
import time
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Messenger")
    parser.add_argument("--host", help="Host to connect to", type=str, default="localhost")
    parser.add_argument("--port", help="Port to connect to", type=int, required=True)
    parser.add_argument("--timeout", help="Timeout for connection", type=int, default=10)
    parser.add_argument("--mode", help="Mode to run in, either 'start' or 'connect'", default="connect")
    return parser.parse_args()


def get_connect(host, port, timeout):
    start = time.time()
    while time.time() - start < timeout:
        time.sleep(1)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
        except:
            print("Could not make a connection to that client\n")
        else:
            print("Connection made")
            return sock
    print("Connection timed out")

def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break

def start(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f"Listening on {host}:{port}")
    return sock


def new_connection(socket):
    while True:
        sock, address = socket.accept()
        print("Connection made at {}".format(address))
        receiveThread = threading.Thread(target = receive, args = (sock, True))
        receiveThread.start()
        while True:
            message = input()
            sock.sendall(str.encode(message))





def main():
    args = parse_args()
    if args.mode == "connect":
        sock = get_connect(args.host, args.port, args.timeout)
        receiveThread = threading.Thread(target = receive, args = (sock, True))
        receiveThread.start()
        while True:
            message = input()
            sock.sendall(str.encode(message))
    elif args.mode == "start":
        sock = start(args.host, args.port)
        new_connection(sock)


main()




    
    
