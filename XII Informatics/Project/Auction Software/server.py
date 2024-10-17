import socket, pickle, threading

def server():
    HOST = '192.168.102.218'
    PORT = 1404
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.listen()
    allclients = []
    try:
        server.bind((HOST,PORT))
        print(f'Created Server {HOST} {PORT}')
    except:
        print('Error creating server. Check IP address.')



    def send_to_all(message):
        for client in allclients:
            client.sendall(pickle.dumps(message))
    def receive(client,address):
        while True:
            try:message = pickle.loads(client.recv(2048))

            except:
                allclients.pop(allclients.index(client))
                print(f'{address[0]} left the server.')
                break
            if message != '':
                send_to_all(f'{address[0]} : {message}')

    def getclient():
        while True:
            client,address = server.accept()
            print(f'Connected to {address[0]} with {PORT}')
            allclients.append(client)
            send_to_all(f'server:{address[0]} has joined.')
            threading.Thread(target=receive,args=(client,address)).start()
    getclient()