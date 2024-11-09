import socket
import threading
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QTextEdit, QLineEdit, QPushButton


class AuctionClient(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auction Client")
        self.setGeometry(300, 200, 400, 300)

        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.message_input = QLineEdit(self)
        self.layout.addWidget(self.message_input)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

        self.HOST = '127.0.0.1'
        self.PORT = 65432
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server in a new thread
        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.HOST, self.PORT))
            self.chat_display.append("Connected to server.")
            threading.Thread(target=self.receive_messages).start()
        except ConnectionRefusedError:
            self.chat_display.append("Failed to connect to the server.")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.chat_display.append(f"Server: {message}")
            except:
                break

    def send_message(self):
        message = self.message_input.text()
        if message:
            self.client_socket.sendall(message.encode('utf-8'))
            self.chat_display.append(f"You: {message}")
            self.message_input.clear()