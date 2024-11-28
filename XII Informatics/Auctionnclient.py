import socket
import threading
import sys
import traceback
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import json


class AuctionClient(QDialog):
    def __init__(self):
        super(AuctionClient,self).__init__()
        self.setWindowTitle("Auction Client")
        self.setGeometry(300, 200, 800, 500)

        self.LBL_font = QFont("Palatino Linotype", 14, QFont.Bold, italic=True)
        self.txt_font = QFont("Palatino Linotype", 12, QFont.Bold, italic=True)
        self.heading_LBLfont = QFont("Palatino Linotype", 22, QFont.Bold, italic=True)

        self.layout = QVBoxLayout()

        self.prodhead = QLabel(self)
        self.prodhead.setFont(self.heading_LBLfont)
        self.prodhead.setGeometry(10, 10, 700, 50)
        self.prodhead.setStyleSheet("color: black;")
        self.layout.addWidget(self.prodhead)

        # Product description
        self.desc_label = QLabel(self)
        self.desc_label.setFont(self.txt_font)
        self.desc_label.setWordWrap(True)
        self.desc_label.setGeometry(10, 100, 450, 150)
        self.desc_label.setStyleSheet("color: black;")
        self.layout.addWidget(self.desc_label)

        # Base price
        self.price_label = QLabel(self)
        self.price_label.setFont(self.txt_font)
        self.price_label.setGeometry(10, 250, 300, 40)
        self.price_label.setStyleSheet("color: black;")
        self.layout.addWidget(self.price_label)

        self.minnextbid = QLabel(self)
        self.minnextbid.setFont(self.LBL_font)
        self.minnextbid.setGeometry(10, 360, 300, 40)
        self.layout.addWidget(self.minnextbid)

        # Due date
        self.due_date_label = QLabel(self)
        self.due_date_label.setFont(self.txt_font)
        self.due_date_label.setGeometry(10, 300, 300, 40)
        self.due_date_label.setStyleSheet("color: black;")
        self.layout.addWidget(self.due_date_label)

        self.chat_box = QTextEdit(self)
        self.chat_box.setReadOnly(True)
        self.chat_box.setFont(QFont("Platino Linotype", 12))
        self.layout.addWidget(self.chat_box)

        self.message_bar = QLineEdit(self)
        self.message_bar.setFont(QFont("Arial", 10))
        self.layout.addWidget(self.message_bar)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

        self.HOST = '192.168.102.206'
        self.PORT = 65432
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.HOST, self.PORT))
            self.chat_box.append("Connected to server.")

            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()

        except ConnectionRefusedError:
            self.chat_box.append("Failed to connect to the server. Please check the server IP and port.")
        except Exception as e:
            self.chat_box.append(f"Error connecting to server: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    try:
                        self.chat_box.append(message)
                        auction_details = json.loads(message)  # Attempt to parse JSON
                        self.update_auction_details(auction_details)
                        print(auction_details)
                    except json.JSONDecodeError:
                        # If not JSON, treat it as a normal chat message
                        self.chat_box.append(f"Server: {message}")
            except Exception as e:
                self.chat_box.append("Error receiving message from server.")
                traceback.print_exc()
                break

    def send_message(self):
        message = self.message_bar.text().strip()
        if message:
            try:
                self.client_socket.sendall(message.encode('utf-8'))
                self.chat_box.append(f"You: {message}")
                self.message_bar.clear()
            except BrokenPipeError:
                self.chat_box.append("Error: Connection to server lost.")
            except Exception as e:
                self.chat_box.append(f"Error sending message: {e}")

    def update_auction_details(self, details):
        self.prodhead.setText(f"Product: {details['Product Name']}")
        self.desc_label.setText(f"Description: {details['Product Description']}")
        self.price_label.setText(f"Base Price: ${details['Base Price']}")
        self.due_date_label.setText(f"Due Date: {details['Due Date']}")
        self.minnextbid.setText(f"Minimum Next Bid: ${details['Minimum Next Bid']}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    client = AuctionClient()
    client.show()
    sys.exit(app.exec_())

