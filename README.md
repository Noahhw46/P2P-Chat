# Peer to Peer Python Chat

This is a simple chat application based on the [Python Client Server](https://github.com/pricheal/python-client-server) project. I wanted an extremely bare-bones network-based chat program in order to learn more about reverse engineering network protocols. The only reason I didn't use the Python Client Server Project is because I wanted it to be peer to peer, rather than a chat-room style application. I didn't see a modern one that was simple enough written in Python (although I almost definitely missed some), so this is my attempt at making one.

## Usage

* To run the application, simply run `messenger.py`. It will ask if you want to run in start or connect mode (basically server or client) with the --mode option. Specify the port you want to use with the --port option. Specify the host you want to connect to with the --host option, and you're good to go. You need to have one instance of the application running in start mode and one in connect mode.

    ex.)
    python messenger.py --mode start --host localhost --port 12345

If you want to connect two seperate computers, you need to use the IP address of your computer from the interface they'll be on, i.e 10.0.0.1. 

## Future

* I'm hoping this will be an ongoing project where I try out different protocols and reverse engineering methods. I want to add basic encryption, authentication, message signing etc.
* Add cool colors
* More in-chat commands like '/help', '/quit', maybe stuff to change a future nickname, colors, etc.
* Usernames and passwords

## Note

* This project grew kind of out of hand and I stopped uploading to this repo. Contact me if you're interested in it. Otherwise, it should be a good starting point for anyone looking to do a similar thing.
