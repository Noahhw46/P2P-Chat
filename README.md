# Peer to Peer Python Chat

This is a simple chat application heavily based on the [Python Client Server](https://github.com/pricheal/python-client-server) project. I wanted a simple chat application with an extremebly barebones protocol. I also wanted to learn more about the Python socket library. The only reason I didn't use the Python Client Server Project is because I wanted it to be peer to peer, rather than a chat-room style application. 

## Usage

* To run the application, simply run `messenger.py`. It will ask if you want to run in start or connect mode (basically server or client) with the --mode option. Specify the port you want to use with the --port option. Specify the host you want to connect to with the --host option, and you're good to go. You need to have one instance of the application running in start mode and one in connect mode.

    ex.)
    python messenger.py --mode start --host localhost --port 12345

One thing to note is that if you want to connect to a computer on the same network, you need to use the IP address of your computer on the interface you want to use. 

