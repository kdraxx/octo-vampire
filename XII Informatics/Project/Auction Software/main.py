# IMPORTING MODULES FOR THE PROJECT
import traceback
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QLabel, QPushButton, QLineEdit, QFileDialog, QWidget, QScrollBar, QDialog, QMainWindow,
                             QMessageBox, QScrollArea, QApplication, QCalendarWidget, QTextEdit,QCheckBox)
from PyQt5.QtGui import QPixmap, QFont,QIcon,QImage
from PyQt5.QtCore import QRect, Qt
import sys
import mysql.connector as sql
import subprocess
import Main_server as server
subprocess.Popen(["python", "Main_server.py"])
# CREATING DATABASE
try:
    connection = sql.connect(host="192.168.102.206", user="root", password="sairam")
    main_cursor = connection.cursor()

    db_creating_query = "CREATE DATABASE IF NOT EXISTS aucsof_ip"
    main_cursor.execute(db_creating_query)

    selecting_db = "USE aucsof_ip"
    main_cursor.execute(selecting_db)

    creating_tbl_for_users = ("CREATE TABLE IF NOT EXISTS users("
                              "user_id VARCHAR(10),"
                              "name VARCHAR(20),"
                              "gmail VARCHAR(30),"
                              "date_of_birth DATE,"
                              "password VARCHAR(16),"
                              "active ENUM('yes','no') DEFAULT 'no')")

    main_cursor.execute(creating_tbl_for_users)

    creating_tbl_for_products = ("CREATE TABLE IF NOT EXISTS products("
                                 "product_id VARCHAR(6) ,"
                                 "product VARCHAR(50),"
                                 "last_date DATE,"
                                 "product_desc VARCHAR(500),"
                                 "status VARCHAR(6) DEFAULT 'unsold',"
                                 "base_price VARCHAR(10))")

    main_cursor.execute(creating_tbl_for_products)



    creating_tbl_for_prodimg = """
        CREATE TABLE IF NOT EXISTS IMAGES (
            image_id int,
            image LONGBLOB  
        );
        """
    main_cursor.execute(creating_tbl_for_prodimg)


    connection.commit()

except sql.Error as e:
    print(f"Error: {e}")

#CREATING LOGIN UI
class login(QDialog):
    def __init__(self):
        super(login, self).__init__()
        self.setWindowTitle("Login") #LOGIN UI TITLE
        #self.setStyleSheet("background-color:rgb(234,241,255)")
        self.setGeometry(470,200,400,300)

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 400, 70)


        self.pointsize_headingLBL=18 #SETTING  FONT SIZE FOR HEADINGS
        self.pointsize_LBL=14 #SETTING  FONT SIZE FOR LABELS

        # CREATING FONTS FOR HEADING LABELS
        self.heading_LBLfont = QFont()
        self.heading_LBLfont.setFamily(u"Palatino Linotype")
        self.heading_LBLfont.setPointSize(22)
        self.heading_LBLfont.setBold(True)
        self.heading_LBLfont.setItalic(True)
        self.heading_LBLfont.setWeight(75)

        # CREATING FONTS FOR NORMAL LABELS
        self.LBL_font = QFont()
        self.LBL_font.setFamily(u"Palatino Linotype")
        self.LBL_font.setPointSize(14)
        self.LBL_font.setBold(True)
        self.LBL_font.setItalic(True)
        self.LBL_font.setWeight(75)

        # CREATING FONTS FOR LINE EDITS
        self.LEfont=QtGui.QFont()
        self.LEfont.setPointSize(12)
        self.LEfont.setFamily("Platino Linotype")


        self.Login_LBL=QLabel(self)
        self.Login_LBL.setText("LOGIN")
        self.Login_LBL.setFont(self.heading_LBLfont)
        self.Login_LBL.setGeometry(155,20,101,31)
        self.Login_LBL.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")

        self.username_LBL=QLabel(self)
        self.username_LBL.setText("Username")
        self.username_LBL.setFont(self.LBL_font)
        self.username_LBL.setGeometry(50,110,90,23)

        self.pointsize_LBL-=6
        self.LBL_font.setItalic(False)
        self.username_LE=QtWidgets.QLineEdit(self)
        self.username_LE.setPlaceholderText("Enter your username")
        self.username_LE.setGeometry(150,110,120,25)
        self.username_LE.setFont(self.LEfont)

        self.password_LBL=QLabel(self)
        self.password_LBL.setText("Password")
        self.pointsize_LBL+=6
        self.LBL_font.setItalic(True)
        self.password_LBL.setGeometry(50,180,90,15)
        self.password_LBL.setFont(self.LBL_font)

        self.password_LE=QtWidgets.QLineEdit(self)
        self.password_LE.setPlaceholderText("Enter your password")
        self.LBL_font.setItalic(False)
        self.password_LE.setFont(self.LEfont)
        self.password_LE.setGeometry(150,175,120,25)
        self.password_LE.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_BTN = QPushButton(self)
        self.login_BTN.setText("Login")
        self.LBL_font.setItalic(True)
        self.login_BTN.setFont(self.LBL_font)
        self.login_BTN.setGeometry(130, 220, 80, 35)
        self.login_BTN.clicked.connect(self.mainpg)
        self.login_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);padding 10px")

        self.sign_up_LBL=QLabel(self)
        self.sign_up_LBL.setText("Don't have an account Signup!")
        self.LBL_font.setItalic(True)
        self.sign_up_LBL.setFont(self.LBL_font)
        self.sign_up_LBL.setGeometry(30,270,280,30)

        self.pointsize_LBL-=5
        self.showpasswordcheckbox=QCheckBox(self)
        self.showpasswordcheckbox.setFont(self.LBL_font)
        self.showpasswordcheckbox.setText("Show")
        self.showpasswordcheckbox.setGeometry(275,175,150,25)
        self.showpasswordcheckbox.stateChanged.connect(self.showpwd)

        self.sign_up_BTN=QPushButton(self)
        self.sign_up_BTN.setText("Sign up")
        self.sign_up_BTN.setFont(self.LBL_font)
        self.sign_up_BTN.setGeometry(310, 265, 80, 35)
        self.sign_up_BTN.clicked.connect(self.signup_pg)
        self.sign_up_BTN.setStyleSheet("padding 30px")

    def signup_pg(self):
        try:
            self.destroy()
            self.open_signup_pg=signup_ui()
            self.open_signup_pg.show()
        except Exception as e:
            traceback.print_exc()

    def showpwd(self):
        try:
            if self.showpasswordcheckbox.isChecked():
                self.password_LE.setEchoMode(False)
            else:
                self.password_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        except Exception as e:
            traceback.print_exc()




    #CHECKING CREDENTIALS
    def mainpg(self):
        try:
            #query=f"select user_id, password from users where user_id=%s and password=%s"
            #main_cursor.execute(query,(self.username_LE.text(),self.password_LE.text()))
            #res=main_cursor.fetchone()
            #if res:
            #    QtWidgets.QMessageBox.information(
            #        self, 'Success', 'Logged in Successfully')
                self.destroy()
                self.open_mainpg = main_ui()
                self.open_mainpg.show()

            #else:
            #    QtWidgets.QMessageBox.warning(
            #        self, 'Unsuccessful', 'Enter correct credentials!!')

        except Exception as e:
            traceback.print_exc()



    def userstodb(self):
        try:
            userinfo = self.username_LE.text()
            userpass = self.password_LE.text()
            update_tbl=f"update users set active='yes' where user_id='{userinfo}'"
            #main_cursor.execute(update_tbl)
            #connection.commit()
        except Exception as e:
            traceback.print_exc()

#CREATING SIGN UP
class signup_ui(QDialog):
    def __init__(self):
        super(signup_ui, self).__init__()
        self.setWindowTitle("Sign up!")  # Sign up UI TITLE
        self.setGeometry(470, 200, 500, 450)

        self.pointsize_headingLBL = 18  # SETTING  FONT SIZE FOR HEADINGS
        self.pointsize_LBL = 14  # SETTING  FONT SIZE FOR LABELS

        # CREATING FONTS FOR HEADING LABELS
        self.heading_labels_font = QtGui.QFont()
        self.heading_labels_font.setPointSize(self.pointsize_headingLBL)
        self.heading_labels_font.setFamily("Platino Linotype")
        self.heading_labels_font.setBold(True)
        self.heading_labels_font.setItalic(True)
        self.heading_labels_font.setWeight(68)

        # CREATING FONTS FOR NORMAL LABELS
        self.LBL_font = QtGui.QFont()
        self.LBL_font.setPointSize(self.pointsize_LBL)
        self.LBL_font.setFamily("Platino Linotype")
        self.LBL_font.setItalic(True)

        self.calender_font = QtGui.QFont()
        self.calender_font.setPointSize(5)
        self.calender_font.setFamily("Platino Linotype")
        self.calender_font.setItalic(True)

        # CREATING FONTS FOR LINE EDITS
        self.LEfont = QtGui.QFont()
        self.LEfont.setPointSize(12)
        self.LEfont.setFamily("Platino Linotype")

        self.Signup_LBL = QLabel(self)
        self.Signup_LBL.setText("SIGN UP")
        self.Signup_LBL.setFont(self.heading_labels_font)
        self.Signup_LBL.setGeometry(200,50,120,25)

        self.userid_LBL = QLabel(self)
        self.userid_LBL.setText("Create user id")
        self.userid_LBL.setFont(self.LBL_font)
        self.userid_LBL.setGeometry(50,120,130,15)

        self.userid_LE =QtWidgets.QLineEdit(self)
        self.userid_LE.setFont(self.LEfont)
        self.userid_LE.setPlaceholderText("Username")
        self.userid_LE.setGeometry(200, 118, 150, 25)

        self.name_LBL = QLabel(self)
        self.name_LBL.setText("Name")
        self.name_LBL.setFont(self.LBL_font)
        self.name_LBL.setGeometry(50, 165, 148, 15)

        self.name_LE = QtWidgets.QLineEdit(self)
        self.name_LE.setFont(self.LEfont)
        self.name_LE.setGeometry(200, 160, 150, 25)
        self.name_LE.setPlaceholderText("Your name")

        self.gmail_LBL = QLabel(self)
        self.gmail_LBL.setText("Gmail")
        self.gmail_LBL.setFont(self.LBL_font)
        self.gmail_LBL.setGeometry(50, 210, 148, 15)

        self.gmail_LE = QtWidgets.QLineEdit(self)
        self.gmail_LE.setFont(self.LEfont)
        self.gmail_LE.setGeometry(200, 202, 200, 25)
        self.gmail_LE.setPlaceholderText("Your gmail")

        self.dob_LBL=QLabel(self)
        self.dob_LBL.setText("DOB")
        self.dob_LBL.setFont(self.LBL_font)
        self.dob_LBL.setGeometry(50, 250, 148, 15)

        self.dob_LE=QtWidgets.QLineEdit(self)
        self.dob_LE.setFont(self.LEfont)
        self.dob_LE.setGeometry(200,244,200,25)
        self.dob_LE.setPlaceholderText("YYYY-MM-DD")

        self.password_LBL=QLabel(self)
        self.password_LBL.setText("Password")
        self.password_LBL.setFont(self.LBL_font)
        self.password_LBL.setGeometry(50,290,148,15)

        self.password_LE = QtWidgets.QLineEdit(self)
        self.password_LE.setFont(self.LEfont)
        self.password_LE.setGeometry(200, 286, 200, 25)
        self.password_LE.setPlaceholderText("Set password")
        self.password_LE.setEchoMode(QtWidgets.QLineEdit.Password)

        self.confirmpassword_LBL=QLabel(self)
        self.confirmpassword_LBL.setText("Confirm Password")
        self.confirmpassword_LBL.setFont(self.LBL_font)
        self.confirmpassword_LBL.setGeometry(40,332,153,15)

        self.confirmpassword_LE = QtWidgets.QLineEdit(self)
        self.confirmpassword_LE.setFont(self.LEfont)
        self.confirmpassword_LE.setGeometry(200, 328, 200, 25)
        self.confirmpassword_LE.setPlaceholderText("Confirm password")
        self.confirmpassword_LE.setEchoMode(QtWidgets.QLineEdit.Password)


        self.signup_BTN=QPushButton(self)
        self.signup_BTN.setText("Sign up")
        self.signup_BTN.setFont(self.LBL_font)
        self.signup_BTN.clicked.connect(self.confirmation)
        self.signup_BTN.setGeometry(210,380,80,40)

        self.back_BTN=QPushButton(self)
        self.back_BTN.setText("Back")
        self.back_BTN.setFont(self.LBL_font)
        self.back_BTN.clicked.connect(self.back)

    def back(self):
        try:
            self.destroy()
            self.open=login()
            self.open.show()
        except Exception as e:
            traceback.print_exc()

    def confirmation(self):
        try:
            if self.confirmpassword_LE.text()=="" or self.confirmpassword_LE.text()=="":
                QtWidgets.QMessageBox.information(
                    self, 'Unsuccessful', 'Enter a password!')
                self.destroy()
                self.open = login()
                self.open.show()
                #self.add_user
            elif self.password_LE.text()==self.confirmpassword_LE.text():
                self.add_user()
                QtWidgets.QMessageBox.information(
                    self, 'Successful', 'Signed in Successfully!')
        except Exception as e:
            traceback.print_exc()




    def add_user(self):
        try:
            username=self.userid_LE.text()
            name=self.name_LE.text()
            gmail=self.gmail_LE.text()
            dob=self.dob_LE.text()
            password=self.password_LE.text()
            print("here")
            q1=f"insert into users values('{username}','{name}','{gmail}','{dob}','{password}','{'No'}')"
            print(q1)
            main_cursor.execute(q1)
            main_cursor.execute("commit")
        except Exception as e:
            traceback.print_exc()

#CREATING HOME PAGE UI
class main_ui(QMainWindow):
    def __init__(self):
        super(main_ui,self).__init__()
        self.setWindowTitle("Auction Software")
        self.setGeometry(100,100,800,500)

        self.setStyleSheet("background-color:rgb(234,241,255)")

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 791, 90)

        self.pointsize_LBL = 40  # SETTING  FONT SIZE FOR LABELS
        self.LBL_font = QtGui.QFont()
        self.LBL_font.setPointSize(self.pointsize_LBL)
        self.LBL_font.setFamily("Platino Linotype")
        self.LBL_font.setItalic(True)
        self.LBL_font.setBold(True)
        self.LBL_font.setWeight(65)

        self.label_font = QtGui.QFont()
        self.label_font.setPointSize(14)
        self.label_font.setFamily("Lucida Handwrting")

        self.home_btn=QPushButton(self)
        self.home_btn.setText("Home")
        self.home_btn.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
        self.home_btn.setGeometry(5,25,120,41)
        self.home_btn.setFont(self.label_font)
        #self.home_btn.setAttribute(Qt.WA_TranslucentBackground)

        self.auction_BTN = QPushButton(self)
        self.auction_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
        self.auction_BTN.setText("Auction")
        self.auction_BTN.setGeometry(129, 25, 120, 41)
        self.auction_BTN.setFont(self.label_font)
        self.auction_BTN.clicked.connect(self.connecto_auction)

        self.products_BTN = QPushButton(self)
        self.products_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
        self.products_BTN.setText("Products")
        self.products_BTN.setFont(self.label_font)
        self.products_BTN.setGeometry(253, 25, 120, 41)
        self.products_BTN.clicked.connect(self.connectto_products)

        self.add_item_BTN = QPushButton(self)
        self.add_item_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
        self.add_item_BTN.setText("Add Item")
        self.add_item_BTN.setFont(self.label_font)
        self.add_item_BTN.setGeometry(375, 25, 120, 41)
        self.add_item_BTN.clicked.connect(self.connec_to_additem)

        self.bids_BTN = QPushButton(self)
        self.bids_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
        self.bids_BTN.setText("Bids")
        self.bids_BTN.setFont(self.label_font)
        self.bids_BTN.setGeometry(500,25,120,41)
        self.bids_BTN.clicked.connect(self.connecto_bids)


        self.profile_BTN = QPushButton(self)
        self.profile_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
        self.profile_BTN.setText("Profile")
        self.profile_BTN.setFont(self.label_font)
        self.profile_BTN.setGeometry(625, 25, 120, 41)
        self.profile_BTN.clicked.connect(self.connecto_profile)

        self.exit_btn=QPushButton(self)
        self.exit_btn.setIcon(QIcon("C:/Users/XII Info/Desktop/Project!/Pictures/exitpg2.png"))
        self.exit_btn.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
        self.exit_btn.setGeometry(750,25,40,40)
        self.exit_btn.clicked.connect(self.backtologin)


        self.auction_software_LBL=QLabel(self)
        self.auction_software_LBL.setFont(self.LBL_font)
        self.auction_software_LBL.setText("Auction Software")
        self.auction_software_LBL.setGeometry(50,200,500,100)

        self.hslogo_LBL=QLabel(self)
        self.hslogo_pic=QPixmap("finallogo_using.png")
        self.hslogo_LBL.setPixmap(self.hslogo_pic)
        self.hslogo_LBL.setGeometry(550,175,195,180)

    def connec_to_additem(self):
        try:
            self.destroy()
            self.openadditm_ui= add_item_ui()
            self.openadditm_ui.show()
        except Exception as e:
            traceback.print_exc()

    def connecto_auction(self):
        try:
            self.destroy()
            self.openproduct_ui=auction_ui()
            self.openproduct_ui.show()
        except Exception as e:
            traceback.print_exc()

    def connecto_bids(self):
        try:
            self.destroy()
            self.openproduct_ui=bids_()
            self.openproduct_ui.show()
        except Exception as e:
            traceback.print_exc()

    def connectto_products(self):
        try:
            self.destroy()
            self.openprofile=products_()
            self.openprofile.show()
        except Exception as e:
            traceback.print_exc()

    def connecto_profile(self):
        try:
            self.destroy()
            self.opensettings=profile_ui()
            self.opensettings.show()
        except Exception as e:
            traceback.print_exc()
    def backtologin(self):
        try:
            reply=QMessageBox.question(self, 'Logout Confirmation',
                                 'Are you sure you want to log out?',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply==QMessageBox.Yes:
                self.destroy()
                self.oplogin=login()
                self.oplogin.show()

        except Exception as e:
            traceback.print_exc()

class auction_ui(QDialog):
    def __init__(self):
        super(auction_ui,self).__init__()
        self.setWindowTitle("Profile")
        self.setGeometry(100,100,800,500)

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 791, 80)

        self.LBL_font = QFont()
        self.LBL_font.setFamily(u"Palatino Linotype")
        self.LBL_font.setPointSize(14)
        self.LBL_font.setBold(True)
        self.LBL_font.setItalic(True)
        self.LBL_font.setWeight(75)

        self.LEfont = QtGui.QFont()
        self.LEfont.setPointSize(12)
        # self.LEfont.setBold(True)
        self.LEfont.setItalic(True)
        self.LEfont.setFamily(u"Platino Linotype")

        self.heading_LBLfont = QFont()
        self.heading_LBLfont.setFamily(u"Palatino Linotype")
        self.heading_LBLfont.setPointSize(22)
        self.heading_LBLfont.setBold(True)
        self.heading_LBLfont.setItalic(True)
        self.heading_LBLfont.setWeight(75)

        '''self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(5, 100, 783, 380))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 759, 359))

        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(760, 0, 16, 362))
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)'''

        self.auctionheading_LBL = QLabel(self)
        self.auctionheading_LBL.setText("Auction")
        self.auctionheading_LBL.setGeometry(350, 20, 100, 31)
        self.auctionheading_LBL.setFont(self.heading_LBLfont)
        self.auctionheading_LBL.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")

        self.prod_img = QLabel(self)
        self.prod_img.setGeometry(5, 110, 100, 100)
        self.prod_img.setStyleSheet("border: 1px solid black;")

        self.prod_idLBL = QLabel(self)
        self.prod_idLBL.setText("Product Id:")
        self.prod_idLBL.setFont(self.LBL_font)
        self.prod_idLBL.setGeometry(225, 120, 100, 30)

        self.prod_idLE = QLineEdit(self)
        self.prod_idLE.setPlaceholderText("ID")
        self.prod_idLE.setFont(self.LEfont)
        self.prod_idLE.setGeometry(330, 125, 150, 25)
        self.prod_idLE.editingFinished.connect(self.gettingprodinfo)

        self.product_name = QLabel(self)
        self.product_name.setText("Product Name:-")
        self.product_name.setFont(self.LBL_font)
        self.product_name.setGeometry(195, 170, 130, 30)

        self.productname_LE = QLineEdit(self)
        self.productname_LE.setPlaceholderText("Product Name")
        self.productname_LE.setFont(self.LEfont)
        self.productname_LE.setGeometry(330, 175, 400, 25)

        self.due_date = QLabel(self)
        self.due_date.setText("Due date:")
        self.due_date.setFont(self.LBL_font)
        self.due_date.setGeometry(195, 225, 90, 30)


        self.duedate_LE = QLineEdit(self)
        self.duedate_LE.setFont(self.LEfont)
        self.duedate_LE.setPlaceholderText("Due date")
        self.duedate_LE.setGeometry(300, 225, 220, 25)
        # self.duedate_LE.editingFinished().connect()

        self.prod_descLBL = QLabel(self)
        self.prod_descLBL.setText("Product Description")
        self.prod_descLBL.setWordWrap(True)
        self.prod_descLBL.setFont(self.LBL_font)
        self.prod_descLBL.setGeometry(195, 270, 150, 50)

        self.prod_descLE = QTextEdit(self)
        self.prod_descLE.setPlaceholderText("Description")
        self.prod_descLE.setFont(self.LEfont)
        self.prod_descLE.setGeometry(300, 275, 400, 50)

        self.baseprice_LBL = QLabel(self)
        self.baseprice_LBL.setFont(self.LBL_font)
        self.baseprice_LBL.setText("Base Price")
        self.baseprice_LBL.setGeometry(195, 340, 90, 30)

        self.baseprice_LE = QLineEdit(self)
        self.baseprice_LE.setPlaceholderText("Base Price")
        self.baseprice_LE.setFont(self.LEfont)
        self.baseprice_LE.setGeometry(300, 345, 100, 25)

        self.startauc_BTN=QPushButton(self)
        self.startauc_BTN.setFont(self.LBL_font)
        self.startauc_BTN.setText("Start Auction")
        self.startauc_BTN.setGeometry(240,390,150,30)
        self.startauc_BTN.clicked.connect(self.mainauctionfn)

        self.back_BTN=QPushButton(self)
        self.back_BTN.setText("Back")
        self.back_BTN.setFont(self.LBL_font)
        self.back_BTN.setGeometry(700,0,100,50)
        self.back_BTN.clicked.connect(self.going_back)
        self.back_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")

    def gettingprodinfo(self):
        prod_id=self.prod_idLE.text()
        try:
            connection = sql.connect(host="192.168.102.206", user="root", password="sairam", database="aucsof_ip")
            main_cursor = connection.cursor()

            query=f"select product,last_date,product_desc,base_price from products where product_id={prod_id}"
            query1=f"select image from images where image_id={prod_id}"
            main_cursor.execute(query)
            result = main_cursor.fetchall()
            main_cursor.execute(query1)
            data=main_cursor.fetchone()
            if data is not None:
                image_data = data[0]
                # print(image_data)
                with open(image_data, 'rb') as file:
                    image = file.read()
                self.temp = QPixmap()
                self.temp.loadFromData(image)
                # print(self.temp)
                self.resized = self.temp.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
                self.prod_img.setPixmap(self.resized)
            self.productname_LE.setText(result[0][0])
            self.duedate_LE.setText(str(result[0][1]))
            self.prod_descLE.setText(result[0][2])
            self.baseprice_LE.setText(result[0][3])

        except Exception as e:
            traceback.print_exc()

    def mainauctionfn(self):
        try:
            server.
        except Exception as e:
            traceback.print_exc()




    def going_back(self):
        try:
            self.destroy()
            self.main_uiobj=main_ui()
            self.main_uiobj.show()
        except Exception as e:
            traceback.print_exc()




class products_(QDialog):
    def __init__(self):
        super(products_, self).__init__()
        self.setWindowTitle("Products")
        self.setGeometry(100, 100, 800, 500)

        self.desc=[]
        self.readm=[]

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 791, 80)

        self.LBL_font = QFont()
        self.LBL_font.setFamily("Palatino Linotype")
        self.LBL_font.setPointSize(14)
        self.LBL_font.setBold(True)
        self.LBL_font.setItalic(True)
        self.LBL_font.setWeight(75)

        self.txt_font = QFont()
        self.txt_font.setFamily("Palatino Linotype")
        self.txt_font.setPointSize(12)
        self.txt_font.setBold(True)
        self.txt_font.setItalic(True)
        self.txt_font.setWeight(75)

        self.heading_LBLfont = QFont()
        self.heading_LBLfont.setFamily("Palatino Linotype")
        self.heading_LBLfont.setPointSize(22)
        self.heading_LBLfont.setBold(True)
        self.heading_LBLfont.setItalic(True)
        self.heading_LBLfont.setWeight(75)

        # Setting up the scroll area
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(QRect(20, 120, 761, 361))
        self.scrollArea.setWidgetResizable(True)

        # Creating a widget to hold the scroll area's contents
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        try:
            connection = sql.connect(host="192.168.102.206", user="root", password="sairam", database="aucsof_ip")
            main_cursor = connection.cursor()

            self.desc_query = "SELECT product, product_desc FROM products order by product_id;"
            main_cursor.execute(self.desc_query)
            self.desc = main_cursor.fetchall()

            b, j = 10, 130
            max_height = 0

            for i in range(1, len(self.desc) + 1):
                prodname = self.desc[i - 1][0]
                proddesc = self.desc[i - 1][1]
                totalinf = f"{prodname}\n{proddesc}"

                self.prod_img = QLabel(self.scrollAreaWidgetContents)
                self.prod_img.setGeometry(5, b, 100, 100)
                self.prod_img.setStyleSheet("border: 1px solid black;")

                query1 = """select image from images where image_id =""" + str(i)
                #print(query1)

                try:
                    main_cursor.execute(query1)
                    data = main_cursor.fetchone()

                    if data is not None:
                        image_data = data[0]
                        #print(image_data)
                        with open(image_data, 'rb') as file:
                            image = file.read()
                        self.temp=QPixmap()
                        self.temp.loadFromData(image)
                        #print(self.temp)
                        self.resized = self.temp.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
                        self.prod_img.setPixmap(self.resized)

                    else:
                        self.prod_img.setText("Image not found.")

                except Exception as img_err:
                    #print(f"Error fetching image for product {prodname}: {img_err}")
                    traceback.print_exc()
                #self.prod_img.setPixmap(pixmap)


                self.product_desc = QLabel(self.scrollAreaWidgetContents)
                self.product_desc.setFont(self.txt_font)
                self.product_desc.setText(totalinf)
                self.product_desc.setWordWrap(True)
                self.product_desc.setGeometry(120, b + 10, 500, 80)
                self.desc.append(self.product_desc)

                self.readmore_BTN = QPushButton(self.scrollAreaWidgetContents)
                self.readmore_BTN.setFont(self.txt_font)
                self.readmore_BTN.setText("Read More")
                self.readmore_BTN.setGeometry(650, b + 60, 90, 25)
                self.readmore_BTN.clicked.connect(self.openingreadmore)
                self.readm.append(self.readmore_BTN)

                b += 130
                j += 135
                max_height = j + 20

            self.scrollAreaWidgetContents.setMinimumHeight(max_height)

        except Exception as err:
            print(f"Database Error: {err}")
            traceback.print_exc()
        finally:
            if connection:
                connection.close()

        self.productsheading_LBL = QLabel(self)
        self.productsheading_LBL.setText("Products")
        self.productsheading_LBL.setGeometry(350, 20, 120, 31)
        self.productsheading_LBL.setFont(self.heading_LBLfont)
        self.productsheading_LBL.setStyleSheet("background-color: rgba(255, 255, 255, 10); color: white")

        self.back_BTN = QPushButton(self)
        self.back_BTN.setText("Back")
        self.back_BTN.setFont(self.LBL_font)
        self.back_BTN.setGeometry(700, 0, 100, 50)
        self.back_BTN.clicked.connect(self.going_back)
        self.back_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10); color: white")

    def openingreadmore(self):
        try:
            self.descreadm=self.sender()
            retrivindesc=self.readm.index(self.descreadm)+1
            print(self.descreadm)
            print(retrivindesc)

            self.destroy()
            self.op=readmore(retrivindesc)
            self.op.show()
        except Exception as e:
            traceback.print_exc()

    def going_back(self):
        try:
            self.close()
            self.main_uiobj = main_ui()
            self.main_uiobj.show()
        except Exception as e:
            traceback.print_exc()


class readmore(QWidget):
    def __init__(self,retrivindesc):
        super(readmore, self).__init__()
        self.setWindowTitle("Read more")
        self.setGeometry(100, 100, 800, 500)

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 791, 80)

        self.LBL_font = QFont()
        self.LBL_font.setFamily("Palatino Linotype")
        self.LBL_font.setPointSize(14)
        self.LBL_font.setBold(True)
        self.LBL_font.setItalic(True)
        self.LBL_font.setWeight(75)

        self.txt_font = QFont()
        self.txt_font.setFamily("Palatino Linotype")
        self.txt_font.setPointSize(12)
        self.txt_font.setBold(True)
        self.txt_font.setItalic(True)
        self.txt_font.setWeight(75)

        self.heading_LBLfont = QFont()
        self.heading_LBLfont.setFamily("Palatino Linotype")
        self.heading_LBLfont.setPointSize(22)
        self.heading_LBLfont.setBold(True)
        self.heading_LBLfont.setItalic(True)
        self.heading_LBLfont.setWeight(75)

        try:
            connection = sql.connect(host="192.168.102.206", user="root", password="sairam", database="aucsof_ip")
            main_cursor = connection.cursor()

            self.query=f"select product,product_desc from products where product_id={retrivindesc} order by product_id"
            main_cursor.execute(self.query)
            self.result=main_cursor.fetchall()
            self.prodhead=QLabel(self)
            self.prodhead.setFont(self.heading_LBLfont)
            self.prodhead.setText(self.result[0][0])
            self.prodhead.setGeometry(0,0,700,80)
            self.prodhead.setStyleSheet("background-color: rgba(255, 255, 255, 10); color: white")

        except sql.Error as err:
            print(f"Database Error: {err}")

        self.back_BTN = QPushButton(self)
        self.back_BTN.setText("Back")
        self.back_BTN.setFont(self.LBL_font)
        self.back_BTN.setGeometry(700, 0, 100, 50)
        self.back_BTN.clicked.connect(self.going_back)
        self.back_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10); color: white")

    def going_back(self):
        try:
            self.close()
            self.products_uiobj = products_()
            self.products_uiobj.show()
        except Exception as e:
            traceback.print_exc()


class add_item_ui(QDialog):
    def __init__(self):
        super(add_item_ui,self).__init__()
        self.setWindowTitle("Add Items")
        self.setGeometry(100,100,800,500)

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 791, 80)

        self.LBL_font = QFont()
        self.LBL_font.setFamily(u"Palatino Linotype")
        self.LBL_font.setPointSize(14)
        self.LBL_font.setBold(True)
        self.LBL_font.setItalic(True)
        self.LBL_font.setWeight(75)

        self.LEfont = QtGui.QFont()
        self.LEfont.setPointSize(12)
        # self.LEfont.setBold(True)
        self.LEfont.setItalic(True)
        self.LEfont.setFamily(u"Platino Linotype")

        self.heading_LBLfont = QFont()
        self.heading_LBLfont.setFamily(u"Palatino Linotype")
        self.heading_LBLfont.setPointSize(22)
        self.heading_LBLfont.setBold(True)
        self.heading_LBLfont.setItalic(True)
        self.heading_LBLfont.setWeight(75)

        self.addtitm_uiheading_LBL = QLabel(self)
        self.addtitm_uiheading_LBL.setText("Add Items")
        self.addtitm_uiheading_LBL.setGeometry(340, 20, 133, 31)
        self.addtitm_uiheading_LBL.setFont(self.heading_LBLfont)
        self.addtitm_uiheading_LBL.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")

        self.prod_img = QLabel(self)
        self.prod_img.setGeometry(5, 110, 110, 110)
        self.prod_img.setStyleSheet("border: 1px solid black;")

        self.addimg_BTN=QPushButton(self)
        self.addimg_BTN.setText("Add Image")
        self.addimg_BTN.clicked.connect(self.openingfiledialogue)
        self.addimg_BTN.setGeometry(15,225,75,25)

        self.prod_idLBL=QLabel(self)
        self.prod_idLBL.setText("Product Id:")
        self.prod_idLBL.setFont(self.LBL_font)
        self.prod_idLBL.setGeometry(225,120,100,30)

        self.prod_idLE = QLineEdit(self)
        self.prod_idLE.setPlaceholderText("New ID")
        self.prod_idLE.setFont(self.LEfont)
        self.prod_idLE.setGeometry(330, 125, 150, 25)
        try:
            connection = sql.connect(host="192.168.102.206", user="root", password="sairam", database="aucsof_ip")
            main_cursor = connection.cursor()
            q1="select max(product_id) from products;"
            main_cursor.execute(q1)
            temp=main_cursor.fetchall()
            print(temp[0][0])
            self.prod_idLE.setText(str(temp[0][0]+1))
            self.prod_idLE.setEnabled(False)
        except Exception as e:
            traceback.print_exc()

        self.product_name=QLabel(self)
        self.product_name.setText("Product Name:-")
        self.product_name.setFont(self.LBL_font)
        self.product_name.setGeometry(195,170,130,30)

        self.productname_LE = QLineEdit(self)
        self.productname_LE.setPlaceholderText("Product Name")
        self.productname_LE.setFont(self.LEfont)
        self.productname_LE.setGeometry(330, 175, 150, 25)

        self.due_date=QLabel(self)
        self.due_date.setText("Due date:")
        self.due_date.setFont(self.LBL_font)
        self.due_date.setGeometry(195,225,90,30)

        #self.duewid_LE=QLineEdit(self)
        #self.duewid_LE.setFont(self.LEfont)
        #self.duewid_LE.setGeometry(520,225,220,150)

        self.duedate_LE=QLineEdit(self)
        self.duedate_LE.setFont(self.LEfont)
        self.duedate_LE.setPlaceholderText("Due date")
        self.duedate_LE.setGeometry(300,225,220,25)
        #self.duedate_LE.editingFinished().connect()

        self.due_datewid=QCalendarWidget(self)
        #self.due_datewid.resize(self.duedate_LE.size())
        self.due_datewid.hide()
        self.due_datewid.clicked.connect(self.getdate)

        self.prod_descLBL=QLabel(self)
        self.prod_descLBL.setText("Product Description")
        self.prod_descLBL.setWordWrap(True)
        self.prod_descLBL.setFont(self.LBL_font)
        self.prod_descLBL.setGeometry(195,270,150,50)

        self.prod_descLE = QTextEdit(self)
        self.prod_descLE.setPlaceholderText("Enter your description here.... Min 30 words")
        self.prod_descLE.setFont(self.LEfont)
        self.prod_descLE.setGeometry(300, 275, 220, 50)

        self.baseprice_LBL=QLabel(self)
        self.baseprice_LBL.setFont(self.LBL_font)
        self.baseprice_LBL.setText("Base Price")
        self.baseprice_LBL.setGeometry(195,340,90,30)

        self.baseprice_LE = QLineEdit(self)
        self.baseprice_LE.setPlaceholderText("Base Price")
        self.baseprice_LE.setFont(self.LEfont)
        self.baseprice_LE.setGeometry(300, 345, 100, 25)

        self.additm_BTN=QPushButton(self)
        self.additm_BTN.setFont(self.LBL_font)
        self.additm_BTN.setText("Add item")
        self.additm_BTN.setGeometry(240,390,100,30)
        self.additm_BTN.clicked.connect(self.addproduct)

        self.back_BTN = QPushButton(self)
        self.back_BTN.setText("Back")
        self.back_BTN.setFont(self.LBL_font)
        self.back_BTN.setGeometry(700, 0, 100, 50)
        self.back_BTN.clicked.connect(self.going_back)
        self.back_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")

        self.remove_itm_BTN = QPushButton(self)
        self.remove_itm_BTN.setText("Delete Items")
        self.remove_itm_BTN.setFont(self.LBL_font)
        self.remove_itm_BTN.setGeometry(700, 80, 200, 50)
        self.remove_itm_BTN.clicked.connect(self.rem_ui)
        self.remove_itm_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")



    def enterEvent(self, event):
        self.due_datewid.show()
        self.due_datewid.setGeometry(520, 225, 250, 150)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.due_datewid.hide()
        self.due_datewid.setGeometry(520, 225, 220, 150)
        super().leaveEvent(event)

    def getdate(self):
        self.getdatefrmwid = self.due_datewid.selectedDate().toPyDate()
        try:
            self.duedate_LE.setText(str(self.getdatefrmwid))
            print(self.getdatefrmwid)
        except Exception as e:
            traceback.print_exc()

    def openingfiledialogue(self):
        options = QFileDialog.Options()
        fileName,_ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                  "Images (*.png *.xpm *.jpg);;All Files (*)", options=options)

        if fileName:
            try:
                self.image_path = fileName
                print(self.image_path)
                self.pixmapimg_prod = QPixmap(fileName)
                self.prod_img.setPixmap(self.pixmapimg_prod.scaled(self.prod_img.size(), aspectRatioMode=True))
            except Exception as e:
                traceback.print_exc()

    def addproduct(self):
        try:
            product_id = int(self.prod_idLE.text())
            productname = self.productname_LE.text()
            lastdate = self.duedate_LE.text()
            product_desc = self.prod_descLE.toPlainText()
            baseprice = self.baseprice_LE.text()

            '''if not all([product_id, productname, lastdate, product_desc, baseprice, self.image_path]):
                QtWidgets.QMessageBox.warning(self, 'Error', 'All fields must be filled, including the image.')
                return'''

            connection = sql.connect(host="192.168.102.206", user="root", password="sairam", database="aucsof_ip")
            main_cursor = connection.cursor()

            # Insert image into the images table and get the image_id
            with open(self.image_path, 'rb') as file:
                img_data = file.read()
            addprod_query = """
                            INSERT INTO products (product_id, product, last_date, product_desc, status, base_price)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """
            print(addprod_query)
            main_cursor.execute(addprod_query, (product_id, productname, lastdate, product_desc, "unsold", baseprice))


            insert_image_query = "INSERT INTO images (image_id,image) VALUES (%s,%s)"
            print(self.image_path)
            main_cursor.execute(insert_image_query, (product_id,self.image_path))
            image_id = main_cursor.lastrowid  # Get the last inserted image_id


            connection.commit()

            QtWidgets.QMessageBox.information(self, 'Success', 'Item added successfully.')
            self.productname_LE.clear()
            self.duedate_LE.clear()
            self.prod_img.setPixmap(None)
            self.prod_descLE.clear()
            self.baseprice_LE.clear()
        except Exception as e:
            traceback.print_exc()
            QtWidgets.QMessageBox.information(self, 'Error 404', 'Item could not be added!.')
        finally:
            connection.close()

    def rem_ui(self):
        try:
            self.destroy()
            removeitmobj=removeitem()
            removeitmobj.show()

        except Exception as e:
            traceback.print_exc()




    def going_back(self):
        try:
            self.close()
            self.main_uiobj = main_ui()
            self.main_uiobj.show()
        except Exception as e:
            traceback.print_exc()

class removeitem(QDialog):
    def __init__(self):
        super(removeitem,self).__init__()
        self.setWindowTitle("Remove Item")
        self.setGeometry(100,100,800,500)

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 791, 80)

        self.LBL_font = QFont()
        self.LBL_font.setFamily(u"Palatino Linotype")
        self.LBL_font.setPointSize(14)
        self.LBL_font.setBold(True)
        self.LBL_font.setItalic(True)
        self.LBL_font.setWeight(75)

        self.heading_LBLfont = QFont()
        self.heading_LBLfont.setFamily(u"Palatino Linotype")
        self.heading_LBLfont.setPointSize(22)
        self.heading_LBLfont.setBold(True)
        self.heading_LBLfont.setItalic(True)
        self.heading_LBLfont.setWeight(75)

        self.LEfont = QtGui.QFont()
        self.LEfont.setPointSize(12)
        # self.LEfont.setBold(True)
        self.LEfont.setItalic(True)
        self.LEfont.setFamily(u"Platino Linotype")

        self.prod_img = QLabel(self)
        self.prod_img.setGeometry(5, 110, 100, 100)
        self.prod_img.setStyleSheet("border: 1px solid black;")

        self.prod_idLBL = QLabel(self)
        self.prod_idLBL.setText("Product Id:")
        self.prod_idLBL.setFont(self.LBL_font)
        self.prod_idLBL.setGeometry(225, 120, 100, 30)

        self.prod_idLE = QLineEdit(self)
        self.prod_idLE.setPlaceholderText("ID")
        self.prod_idLE.setFont(self.LEfont)
        self.prod_idLE.setGeometry(330, 125, 150, 25)
        self.prod_idLE.editingFinished.connect(self.gettingprodinfo)

        self.product_name = QLabel(self)
        self.product_name.setText("Product Name:-")
        self.product_name.setFont(self.LBL_font)
        self.product_name.setGeometry(195, 170, 130, 30)

        self.productname_LE = QLineEdit(self)
        self.productname_LE.setPlaceholderText("Product Name")
        self.productname_LE.setFont(self.LEfont)
        self.productname_LE.setGeometry(330, 175, 400, 25)

        self.due_date = QLabel(self)
        self.due_date.setText("Due date:")
        self.due_date.setFont(self.LBL_font)
        self.due_date.setGeometry(195, 225, 90, 30)

        self.duedate_LE = QLineEdit(self)
        self.duedate_LE.setFont(self.LEfont)
        self.duedate_LE.setPlaceholderText("Due date")
        self.duedate_LE.setGeometry(300, 225, 220, 25)
        # self.duedate_LE.editingFinished().connect()

        self.prod_descLBL = QLabel(self)
        self.prod_descLBL.setText("Product Description")
        self.prod_descLBL.setWordWrap(True)
        self.prod_descLBL.setFont(self.LBL_font)
        self.prod_descLBL.setGeometry(195, 270, 150, 50)

        self.prod_descLE = QTextEdit(self)
        self.prod_descLE.setPlaceholderText("Description")
        self.prod_descLE.setFont(self.LEfont)
        self.prod_descLE.setGeometry(300, 275, 400, 50)

        self.baseprice_LBL = QLabel(self)
        self.baseprice_LBL.setFont(self.LBL_font)
        self.baseprice_LBL.setText("Base Price")
        self.baseprice_LBL.setGeometry(195, 340, 90, 30)

        self.baseprice_LE = QLineEdit(self)
        self.baseprice_LE.setPlaceholderText("Base Price")
        self.baseprice_LE.setFont(self.LEfont)
        self.baseprice_LE.setGeometry(300, 345, 100, 25)

        self.removeitmheading_LBL = QLabel(self)
        self.removeitmheading_LBL.setText("Delete Items")
        self.removeitmheading_LBL.setGeometry(330, 20, 62, 31)
        self.removeitmheading_LBL.setFont(self.heading_LBLfont)
        self.removeitmheading_LBL.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")

        self.back_BTN = QPushButton(self)
        self.back_BTN.setText("Back")
        self.back_BTN.setFont(self.LBL_font)
        self.back_BTN.setGeometry(700, 0, 100, 50)
        self.back_BTN.clicked.connect(self.going_back)
        self.back_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")

    def gettingprodinfo(self):
        prod_id = self.prod_idLE.text()
        try:
            connection = sql.connect(host="192.168.102.206", user="root", password="sairam", database="aucsof_ip")
            main_cursor = connection.cursor()

            query = f"select product,last_date,product_desc,base_price from products where product_id={prod_id}"
            query1 = f"select image from images where image_id={prod_id}"
            main_cursor.execute(query)
            result = main_cursor.fetchall()
            main_cursor.execute(query1)
            data = main_cursor.fetchone()
            if data is not None:
                image_data = data[0]
                # print(image_data)
                with open(image_data, 'rb') as file:
                    image = file.read()
                self.temp = QPixmap()
                self.temp.loadFromData(image)
                # print(self.temp)
                self.resized = self.temp.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
                self.prod_img.setPixmap(self.resized)
            self.productname_LE.setText(result[0][0])
            self.duedate_LE.setText(str(result[0][1]))
            self.prod_descLE.setText(result[0][2])
            self.baseprice_LE.setText(result[0][3])
        except Exception as e:
            traceback.print_exc()

class bids_(QDialog):
    def __init__(self):
        super(bids_,self).__init__()
        self.setWindowTitle("Bids")
        self.setGeometry(100,100,800,500)

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 791, 80)

        self.LBL_font = QFont()
        self.LBL_font.setFamily(u"Palatino Linotype")
        self.LBL_font.setPointSize(14)
        self.LBL_font.setBold(True)
        self.LBL_font.setItalic(True)
        self.LBL_font.setWeight(75)

        self.heading_LBLfont = QFont()
        self.heading_LBLfont.setFamily(u"Palatino Linotype")
        self.heading_LBLfont.setPointSize(22)
        self.heading_LBLfont.setBold(True)
        self.heading_LBLfont.setItalic(True)
        self.heading_LBLfont.setWeight(75)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 120, 761, 361))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 759, 359))

        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(740, 0, 16, 351))
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.bidsheading_LBL = QLabel(self)
        self.bidsheading_LBL.setText("Bids")
        self.bidsheading_LBL.setGeometry(330, 20, 62, 31)
        self.bidsheading_LBL.setFont(self.heading_LBLfont)
        self.bidsheading_LBL.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")

        self.back_BTN=QPushButton(self)
        self.back_BTN.setText("Back")
        self.back_BTN.setFont(self.LBL_font)
        self.back_BTN.setGeometry(700,0,100,50)
        self.back_BTN.clicked.connect(self.going_back)
        self.back_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")



    def going_back(self):
        try:
            self.destroy()
            self.main_uiobj=main_ui()
            self.main_uiobj.show()
        except Exception as e:
            traceback.print_exc()


class profile_ui(QDialog):
    def __init__(self):
        super(profile_ui,self).__init__()
        self.setWindowTitle("Settings")
        self.setGeometry(100,100,800,500)

        self.tabsbg_LBL = QLabel(self)
        self.tabsbg_LBL.setStyleSheet("background-color:rgba(0,12,95,205)")
        self.tabsbg_LBL.setGeometry(0, 0, 791, 80)

        self.LBL_font = QFont()
        self.LBL_font.setFamily(u"Palatino Linotype")
        self.LBL_font.setPointSize(14)
        self.LBL_font.setBold(True)
        self.LBL_font.setItalic(True)
        self.LBL_font.setWeight(75)

        self.heading_LBLfont = QFont()
        self.heading_LBLfont.setFamily(u"Palatino Linotype")
        self.heading_LBLfont.setPointSize(22)
        self.heading_LBLfont.setBold(True)
        self.heading_LBLfont.setItalic(True)
        self.heading_LBLfont.setWeight(75)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 120, 761, 361))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 770, 359))

        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(740, 0, 16, 351))
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.profileheading_LBL = QLabel(self)
        self.profileheading_LBL.setText("Profile")
        self.profileheading_LBL.setGeometry(350, 20, 90, 40)
        self.profileheading_LBL.setFont(self.heading_LBLfont)

        self.back_BTN=QPushButton(self)
        self.back_BTN.setText("Back")
        self.back_BTN.setFont(self.LBL_font)
        self.back_BTN.setGeometry(700,0,100,50)
        self.back_BTN.clicked.connect(self.going_back)

        self.profileheading_LBL.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
        self.back_BTN.setStyleSheet("background-color: rgba(255, 255, 255, 10);color : white")
    def going_back(self):
        try:
            self.destroy()
            self.main_uiobj=main_ui()
            self.main_uiobj.show()
        except Exception as e:
            traceback.print_exc()

if __name__=="__main__":
    app = QApplication(sys.argv)
    l = login()
    l.show()
    app.exec_()

