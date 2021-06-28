import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.100.3"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World")
send("Hello all")
send("Hello tim")
input()
send(DISCONNECT_MESSAGE)
