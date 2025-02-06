import socket
import threading
import pickle
import traceback
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

# Global Variables for Client Logic
HOST = '192.168.102.206'
PORT = 55444
client_socket = None
update_ui_callback = None

def connect_to_server():
    """Connect to the server and start the receiving thread."""
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        if update_ui_callback:
            update_ui_callback("chat", "Connected to server.")

        # Start a thread to receive messages
        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

    except ConnectionRefusedError:
        if update_ui_callback:
            update_ui_callback("chat", "Failed to connect to the server. Please check the server IP and port.")
    except Exception as e:
        if update_ui_callback:
            update_ui_callback("chat", f"Error connecting to server: {e}")

def receive_messages():
    global client_socket
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                if update_ui_callback:
                    update_ui_callback("chat", "Disconnected from server.")
                break

            if message.startswith(b'PICKLE'):
                try:
                    auction_details = pickle.loads(message[6:])
                    if update_ui_callback:
                        update_ui_callback("auction", auction_details)
                except pickle.UnpicklingError:
                    update_ui_callback("chat", "Failed to decode auction details.")
            else:
                text_message = message.decode('utf-8')
                if update_ui_callback:
                    update_ui_callback("chat", f"Server: {text_message}")
        except Exception as e:
            if update_ui_callback:
                update_ui_callback("chat", f"Error receiving message: {e}")
            break




def send_message(message):
    global client_socket
    try:
        client_socket.send(message.encode('utf-8'))
    except BrokenPipeError:
        if update_ui_callback:
            update_ui_callback("chat", "Error: Connection to server lost.")
    except Exception as e:
        if update_ui_callback:
            update_ui_callback("chat", f"Error sending message: {e}")


class AuctionClientUI(QDialog):
    def __init__(self):
        super(AuctionClientUI, self).__init__()
        self.showMaximized()
        self.setWindowTitle("Auction Client")
        self.setStyleSheet("""
            background-color: #f4f6f9; 
            font-family: 'Arial';
            color: #333;
        """)

        # Fonts
        self.LBL_font = QFont("Arial", 14, QFont.Bold)
        self.txt_font = QFont("Arial", 16,QFont.Bold)
        self.heading_LBLfont = QFont("Arial", 22, QFont.Bold)

        # Layout
        self.layout = QVBoxLayout()
        #self.layout.setSpacing(20)

        # Heading
        self.prodhead = QLabel("Product: Not Available", self)
        self.prodhead.setFont(self.heading_LBLfont)
        self.prodhead.setStyleSheet("color: #007bff;")
        self.layout.addWidget(self.prodhead, alignment=Qt.AlignCenter)

        # Product description
        self.desc_label = QLabel("Description: Not Available", self)
        self.desc_label.setFont(self.txt_font)
        self.desc_label.setWordWrap(True)
        self.layout.addWidget(self.desc_label)

        # Base price
        self.price_label = QLabel("Base Price: $0", self)
        self.price_label.setFont(self.txt_font)
        self.layout.addWidget(self.price_label)

        # Due date
        self.due_date_label = QLabel("Due Date: Not Set", self)
        self.due_date_label.setFont(self.txt_font)
        self.layout.addWidget(self.due_date_label)

        # Minimum next bid
        self.minnextbid = QLabel("Minimum Next Bid: $0", self)
        self.minnextbid.setFont(self.LBL_font)
        self.layout.addWidget(self.minnextbid)

        # Auction started status
        self.auction_status = QLabel("Auction Status: Not Started", self)
        self.auction_status.setFont(self.LBL_font)
        self.auction_status.setStyleSheet("color: #555;")
        self.layout.addWidget(self.auction_status)

        # Chat box
        self.chat_box = QTextEdit(self)
        self.chat_box.setReadOnly(True)
        self.chat_box.setFont(QFont("Arial", 14))
        self.chat_box.setStyleSheet("""
            background-color: #ffffff; 
            color: #333; 
            border: 1px solid #ccc; 
            border-radius: 5px; 
            padding: 10px;
        """)
        self.layout.addWidget(self.chat_box, stretch=2)

        # Message bar
        self.message_bar = QLineEdit(self)
        self.message_bar.setPlaceholderText("Type your message here...")
        self.message_bar.setFont(QFont("Arial", 16,))
        self.message_bar.setStyleSheet("""
            border: 1px solid #ccc; 
            border-radius: 5px; 
            padding: 10px;
        """)
        self.layout.addWidget(self.message_bar)

        # Send button
        self.send_button = QPushButton("Send", self)
        self.send_button.setStyleSheet("""
            background-color: #007bff; 
            color: white; 
            padding: 10px 20px; 
            border: none; 
            border-radius: 5px; 
            font-size: 16px; 
            font-weight: bold;
        """)
        self.send_button.setCursor(Qt.PointingHandCursor)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button, alignment=Qt.AlignRight)

        self.setLayout(self.layout)

        # Register the UI callback
        global update_ui_callback
        update_ui_callback = self.update_ui

        # Connect to the server
        connect_to_server()

    def send_message(self):
        """Send a message via the client logic."""
        message = self.message_bar.text().strip()
        if message:
            send_message(message)
            self.chat_box.append(f"You: {message}")
            self.message_bar.clear()

    def update_ui(self, update_type, data):
        """Update the UI based on the message type."""
        if update_type == "chat":
            self.chat_box.append(data)
        elif update_type == "auction":
            self.prodhead.setText(f"Product: {data['Product Name']}")
            self.desc_label.setText(f"Description: {data['Product Description']}")
            self.price_label.setText(f"Base Price: ${data['Base Price']}")
            self.due_date_label.setText(f"Due Date: {data['Due Date']}")
            self.minnextbid.setText(f"Minimum Next Bid: ${data['Minimum Next Bid']}")
            self.auction_status.setText(
                "Auction Status: Active" if data.get("Auction Started") else "Auction Status: Not Started"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    client_ui = AuctionClientUI()
    client_ui.show()
    sys.exit(app.exec_())