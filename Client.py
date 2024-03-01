import socket

HEADER=64
PORT=100
FORMAT="utf-8"
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER="192.168.102.206"
ADDR=(SERVER,PORT)

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b" "*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

clients_status=True
while clients_status:
    msgg=input("Message:-")
    send(msgg)
    recd_msg=(client.recv(64).decode(FORMAT))

    print(recd_msg)
