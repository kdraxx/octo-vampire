import socket
import threading


HEADER=64
PORT=1000
PORT=100
FORMAT="utf-8"
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER="192.168.102.206"
def send(msg):
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


clients_status=True
while clients_status:
    msgg=input("Message:-")
    send(msgg)
    print(client.recv(64).decode(FORMAT))
    recd_msg=(client.recv(64).decode(FORMAT))
    print(recd_msg)

send(DISCONNECT_MESSAGE)


