import socket
import threading
import time

from Product import Product
import main

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handler_client(conn, addr):#aici primesc si trimit mesaje pe server
    print("[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
            msg=conn.recv(4096).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
                return;
            print(f"[{addr}] {msg}")
            whatHappens = main.serverRequest(msg)
            if(whatHappens=='True'):
                print('Ar trebui sa primesc')
                conn.send("True".encode(FORMAT))
                conn.close()
            elif isinstance(whatHappens, list):
                print("E lista")
                nrOfProducts=len(whatHappens)
                myString=''
                for a in whatHappens:
                    myString = myString + a.name + 'asf'
                    myString = myString + str(a.price) + 'asf'
                    myString = myString + str(a.stoc) + 'asf'
                    myString = myString + a.description + '&'
                conn.send(myString.encode(FORMAT))
                conn.close()
            elif whatHappens.__contains__('getUser'):
                print('Trimit user')
                conn.send(whatHappens.encode(FORMAT))
                conn.close
            elif whatHappens.__contains__('getProduct'):
                print('Trimit product')
                conn.send(whatHappens.encode(FORMAT))
                conn.close
            elif whatHappens.__contains__('sendCommands'):
                print('Trimit command')
                conn.send(whatHappens.encode(FORMAT))
                conn.close
            else:
                print('Nu ar trebui sa primesc')
                conn.send("False".encode(FORMAT))
            conn.close()

   # conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread=threading.Thread(target=handler_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


print("[STARTING] server is starting...")
start()