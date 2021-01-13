#! /bin/python3

import socket
import argparse
import sys

def server(l_port):


    HEAD_LENGTH = 10
    HEAD_LIMIT = 10

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client = ("localhost", l_port)
    s.bind(tcp_client)
    s.listen(5)

    while True:

        client_socket, client_address = s.accept()
        print("Connection from {client_address} has been established.")

        msg = "Welcome to the server!"
        msg = f'{len(msg):<{HEAD_LENGTH}}'+msg
        client_socket.send(bytes(msg, "utf-8"))

    return

def client(server_port, server_address):
    
    HEAD_LENGTH = 10
    HEAD_LIMIT = 10
    buff_size = 16

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server = (server_address, server_port)
    s.connect(tcp_server)

    while True:
        full_msg = ''
        new_msg = True
        
        while True:
            msg = s.recv(buff_size)
            if new_msg:
                print(f"New message length: {msg[:HEAD_LENGTH]}")
                msglen = int(msg[:HEAD_LENGTH])
                new_msg = False
            full_msg += msg.decode("utf-8")

            if len(full_msg) - HEAD_LENGTH == msglen:
                print("full msg recvd")
                print(full_msg[HEAD_LENGTH:])
                new_msg =  True
                full_msg = ''

        print(full_msg)

    return

def user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("--listen", "-l", help="listen for port number", type=int, required=False)
    parser.add_argument("hostname", help="List hostname", nargs='?')
    parser.add_argument("portNumber", help="List port number", nargs='?', type=int)
    args = parser.parse_args()

    if args.listen and not args.hostname and not args.portNumber:
        l_port = args.listen
        server(l_port)
    if args.hostname and args.portNumber and not args.listen:
        hostname, port = args.hostname, args.portNumber
        client(port, hostname)
    else:
        sys.stderr.write("Something went wrong. Please check arguments and try again.\nUsage: ./pycat [--listen LISTEN] ["
                         "hostname] [portNumber]\n")
        exit()

if __name__ == "__main__":
    user_input()
