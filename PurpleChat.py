#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import purple 
purpleEnc = purple.Purple(8,0,2,3,1,5,0,'AEIOUYBCDFGHJKLMNPQRSTVWXZ','ASFHBJNAWFKMWAFMWAKF')


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected" % client_address)
        client.send(bytes("Greetings Now type your name and press enter", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    encryptedname= client.recv(BUFSIZ).decode("utf8")
    purpleEnc.changeText(encryptedname)
    encryptedname = purpleEnc.decrypt()
    name = encryptedname
    welcome = 'Welcome %s If you ever want to quit type {quit} to exit' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ).decode("utf8")
        purpleEnc.changeText(msg)
        msg = purpleEnc.decrypt()
        print(msg)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat" % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        print("this is the msg:", msg)
        if(type(msg) is str):
            sock.send(bytes(prefix, "utf8") + bytes(msg, "utf8"))
        else:
            sock.send(bytes(prefix, "utf8") + msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()