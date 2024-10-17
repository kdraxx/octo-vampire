import socket
import threading
import random

HEADER=64
HEADER2=2048
PORT=random.randint(1000,10000)
SERVER= "192.168.102.206"

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)


ADDR=(SERVER,PORT)
FORMAT="utf-8"
DISCONNECT_MESSAGE="!LOGOUT"
s.bind(ADDR)

def handleclient(client, addr):
    print(f"[CONNECTED] {addr} connected to the server")
    connected=True
    while connected:
        msg_length=client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=client.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
                client.send("You have been disconnected by the host ".encode(FORMAT))
            print(f"Recieved from{addr}\nMessage:-{msg}")
            client.send("Server has recieved message".encode(FORMAT))
            send_msg = input("Enter the message to the client:")
            client.send(send_msg.encode(FORMAT))

    client.close()

def start():
    s.listen()
    print(f"[LISTENING] Server is listening...{SERVER}")
    while True:
        client,addr=s.accept()
        thread=threading.Thread(target=handleclient,args=(client,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")



start()
