try:
    import sys
    import logging
    import traceback
    from PyQt5 import QtWidgets

    from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QComboBox, QLabel,
                                 QFormLayout, QHBoxLayout, QSpinBox, QPushButton, QDialog,
                                 QLineEdit, QDialogButtonBox, QTableWidget, QHeaderView,
                                 QMessageBox)
    from PyQt5 import QtGui
    from PyQt5.QtGui import (QFont,QPixmap)

    from PyQt5.QtCore import Qt
    import mysql.connector
    from mysql.connector import Error


    '''class Database:
        def __init__(self):
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='sairam',
                database='dream_holidays'
                )
            self.cursor=connection.cursor()

            self.name_qry="select name from packages where pid=2 "
            self.cursor.execute(self.name_qry)
            nq1=self.cursor.fetchone()'''









    class MainWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Dream Holidays')
            self.setGeometry(100, 100,700, 600)
            self.setStyleSheet("background-color:#FFE5B4")
            self.setStyleSheet("""
                 QWidget {
                    background-color: #FFE5B4;
                    border-radius: 10px;
                }
                 QPushButton:hover {
                    background-color:#33ff77;
                }

            """)

            self.title_LBL=QLabel(self)
            self.title_LBL.setText("DREAM HOLIDAYS")
            self.title_LBL.setGeometry(170,50,350,50)
            self.title_LBL.setStyleSheet("font-size: 36px; color:#00ccff; font-weight:bold")

            self.logo_lbl=QLabel(self)
            pixmap = QtGui.QPixmap("C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/logo4.png")
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio)
            self.logo_lbl.setPixmap(pixmap)
            self.logo_lbl.setGeometry(200, 90, 900, 400)

            self.continue_btn=QPushButton(self)
            self.continue_btn.setText("Continue")
            self.continue_btn.setGeometry(265,450,100,40)
            self.continue_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px; background-color:#66ffff; font-family: Ariel")
            self.continue_btn.clicked.connect(self.main)
            
            

        def main(self):
            self.h = HomePage()
            self.h.show()
            self.hide()


    class HomePage(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Dream Holidays')
            self.setGeometry(200, 200, 1350, 750)

            self.setStyleSheet("""
                 QWidget {
                    
                    border-radius: 10px;
                }
                 QPushButton:hover {
                    background-color: #0056b3;
                }
                QDialog {
                    background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/background);
                }
                
            """)



            self.home_button = QPushButton( self)
            self.home_button.setGeometry(100, 60, 200, 40)
            self.home_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 14px;background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/logo2);")



            self.tours_button = QPushButton("Tours", self)
            self.tours_button.setGeometry(330, 60, 170, 50)
            self.tours_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.tours_button.clicked.connect(self.temp)



            self.fli_button = QPushButton("Flights", self)
            self.fli_button.setGeometry(530, 60, 170, 50)
            self.fli_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.fli_button.clicked.connect(self.flights)

            self.hotel_btn=QPushButton("Hotels",self)
            self.hotel_btn.setGeometry(730,60,170,50)
            self.hotel_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.hotel_btn.clicked.connect(self.hotels)

            self.abt_btn = QPushButton("About US", self)
            self.abt_btn.setGeometry(950, 60, 170, 50)
            self.abt_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")



            self.tagline_lbl=QLabel("Where Dreams take Flight",self)
            self.tagline_lbl.setGeometry(50,90,700,150)
            self.tagline_lbl.setStyleSheet("font-size:55px;color:white;font-weight: bold")
            self.tagline_lbl.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed"))

            self.intro_lbl=QLabel("At Dream Holidays, we are passionate about helping people explore the world.\nOur mission is to make travel accessible and enjoyable for everyone.",self)
            self.intro_lbl.setGeometry(20,150,850,200)
            self.intro_lbl.setStyleSheet("font-size:25px;color:white;font-weight: bold")
            self.intro_lbl.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed"))

            self.discover_lbl=QLabel("Discover",self)
            self.discover_lbl.setGeometry(20,350,500,70)
            self.discover_lbl.setStyleSheet("font-size:65px;color:white;font-weight: bold;text-decoration:underline")
            self.discover_lbl.setFont(QtGui.QFont("Felix Titling"))

            self.tours_lbl=QLabel("Best chance to enjoy\nBig Savings", self)
            self.tours_lbl.setGeometry(50, 660, 300, 70)
            self.tours_lbl.setStyleSheet("font-size:30px;color:white;")
            self.tours_lbl.setFont(QtGui.QFont("Bodoni MT"))

            self.tours_img_btn=QPushButton(self)
            self.tours_img_btn.setGeometry(50, 450, 300, 200)
            self.tours_img_btn.setStyleSheet("background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/eiffel_tower);")
            self.tours_img_btn.clicked.connect(self.temp)

            self.flight_lbl=QLabel("Discounts You wont find\nanywhere else", self)
            self.flight_lbl.setGeometry(360, 670, 310, 70)
            self.flight_lbl.setStyleSheet("font-size:30px;color:white;")
            self.flight_lbl.setFont(QtGui.QFont("Bodoni MT"))

            self.flights_img_btn=QPushButton(self)
            self.flights_img_btn.setGeometry(360, 450, 300, 200)
            self.flights_img_btn.setStyleSheet("background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/best_offers);")

            self.hotels_img_btn=QPushButton(self)
            self.hotels_img_btn.setGeometry(670,450,300,200)
            self.hotels_img_btn.setStyleSheet("background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/hotels);")

            self.hotels_lbl=QLabel("Unbeatable Rates for \nUnforgettable Stays",self)
            self.hotels_lbl.setGeometry(680,660,300,70)
            self.hotels_lbl.setStyleSheet("font-size:30px;color:white;")
            self.hotels_lbl.setFont(QtGui.QFont("Bodoni MT"))


            self.abt_img_lbl=QLabel(self)
            self.abt_img_lbl.setGeometry(1000,450,300,200)
            self.abt_img_lbl.setStyleSheet("background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/logo1);")

            self.abt_lbl = QLabel("Crafting Memories, \nOne Trip at a Time", self)
            self.abt_lbl.setGeometry(1000, 660, 300, 70)
            self.abt_lbl.setStyleSheet("font-size:30px;color:white;")
            self.abt_lbl.setFont(QtGui.QFont("Bodoni MT"))


        def temp(self):
            try:
                self.pkg=Tours()
                self.pkg.show()
                self.hide()
            except Exception as e:
                traceback.print_exc()

        def flights(self):
            self.f=Flights()
            self.f.show()
            self.hide()

        def hotels(self):
            self.ho = Hotels()
            self.ho.show()
            self.hide()


    imageindex = 0
    lid_list = []


    class Tours(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Dream Holidays')
            self.setGeometry(200, 200, 1350, 750)
            self.setStyleSheet("background-color:#FFE5B4")
            self.setStyleSheet("""
                    QWidget {
                       background-color: #FFE5B4;
                       border-radius: 10px;
                   }
                    QPushButton:hover {
                       background-color: #0056b3;
                   }

               """)

            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='sairam',
                database='dream_holidays'
            )
            self.cursor = self.connection.cursor()

            self.cursor.execute("Select con_name from continents")

            selectedpid = self.cursor.fetchall()

            self.cb1 = QComboBox(self)
            self.cb1.setGeometry(100, 160, 200, 70)

            for i in selectedpid:
                self.cb1.addItem(i[0])

            self.cb1.setEditable(True)
            font = QtGui.QFont("Bahnschrift Light SemiCondensed", 15)
            self.cb1.setFont(font)
            self.cb1.lineEdit().setFont(font)
            self.cb1.setEditable(False)
            self.cb1.activated.connect(self.country_name)

            self.cb2 = QComboBox(self)
            self.cb2.setGeometry(320, 160, 225, 70)
            self.cb2.setFont(font)
            self.cb2.activated.connect(self.pkg)

            self.cursor.execute("select country_name from countries")
            lids = self.cursor.fetchall()

            for i in lids:
                self.cb2.addItem(i[0])

            self.cb3 = QComboBox(self)
            self.cb3.setGeometry(560, 160, 500, 70)
            self.cb3.activated.connect(self.pkg_ele)
            self.cb3.setFont(font)

            self.cursor.execute("select name from packages")
            selectedpid2 = self.cursor.fetchall()

            for i in selectedpid2:
                self.cb3.addItem(i[0])

            self.con_lbl = QLabel("Continents", self)
            self.con_lbl.setGeometry(100, 100, 150, 50)
            self.con_lbl.setFont(font)
            self.con_lbl.setStyleSheet("color:Spring Gr")

            self.c_lbl = QLabel("Countries", self)
            self.c_lbl.setGeometry(320, 100, 150, 50)
            self.c_lbl.setFont(font)
            self.c_lbl.setStyleSheet("color:Mint")

            self.pkg_name_lbl = QLabel(self)
            self.pkg_name_lbl.setGeometry(100, 240, 500, 50)
            self.pkg_name_lbl.setStyleSheet("font:25px; text-decoration: underline")

            self.pkg_des_lbl = QLabel(self)
            self.pkg_des_lbl.setGeometry(100, 280, 500, 300)
            self.pkg_des_lbl.setStyleSheet("font:20px")

            self.pkg_price_lbl = QLabel(self)
            self.pkg_price_lbl.setGeometry(620, 330, 130, 30)
            self.pkg_price_lbl.setStyleSheet("font:15px")

            self.pkg_dur_lbl = QLabel(self)
            self.pkg_dur_lbl.setGeometry(620, 360, 100, 50)
            self.pkg_dur_lbl.setStyleSheet("font:15px")

            self.pkg_img_lbl = QLabel(self)
            self.pkg_img_lbl.setGeometry(790, 330, 500, 250)

            self.select_btn = QPushButton("Select", self)
            self.select_btn.setGeometry(500, 710, 100, 50)
            self.select_btn.setStyleSheet("Qpushbutton:Hover {background-color: Null}")
            self.select_btn.clicked.connect(self.temp)
            self.select_btn.hide()

            self.prev_btn = QPushButton(self)
            self.prev_btn.setGeometry(690, 600, 130, 50)
            self.prev_btn.setStyleSheet(
                "background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/background);")
            # self.prev_btn.setText("zdfbg")
            self.prev_btn.clicked.connect(self.prev)
            self.prev_btn.hide()

            self.next_btn = QPushButton(self)
            self.next_btn.setGeometry(1300, 430, 30, 50)
            self.prev_btn.setStyleSheet(
                "background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/back_img-removebg-preview)")

            self.next_btn.clicked.connect(self.next)
            self.next_btn.hide()

            self.home_button = QPushButton(self)
            self.home_button.setGeometry(100, 60, 200, 40)
            self.home_button.setStyleSheet(
                "padding: 10px;border-radius: 5px;font-size: 14px;background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/logo2);")
            # self.home_button.clicked.connect(self.Home)

            self.tours_button = QPushButton("Tours", self)
            self.tours_button.setGeometry(330, 60, 170, 50)
            self.tours_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            # self.tours_button.clicked.connect(self.tours)

            self.fli_button = QPushButton("Flights", self)
            self.fli_button.setGeometry(530, 60, 170, 50)
            self.fli_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            # self.fli_button.clicked.connect(self.flights)

            self.hotel_btn = QPushButton("Hotels", self)
            self.hotel_btn.setGeometry(730, 60, 170, 50)
            self.hotel_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            # self.hotel_btn.clicked.connect(self.hotels)

            self.abt_btn = QPushButton("About US", self)
            self.abt_btn.setGeometry(950, 60, 170, 50)
            self.abt_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")

        def country_name(self):
            try:
                self.cursor.close()
                a = self.cb1.currentText()
                self.cursor = self.connection.cursor()
                self.cursor.execute(f"select cid from continents where con_name='{a}'")
                d1 = self.cursor.fetchall()

                d2 = str(d1[0][0])
                d3 = int(d2)
                self.cursor.execute(f"select country_name from countries where cid={d3}")
                d4 = self.cursor.fetchall()
                self.cb2.clear()
                for i in d4:
                    self.cb2.addItem(i[0])


            except Exception as e:
                print(e)
                traceback.print_exc()

        def pkg(self):
            try:
                self.cursor.close()
                cn = self.cb2.currentText()
                self.cursor = self.connection.cursor()
                self.cursor.execute(
                    f"select distinct pid from location,countries where location.con_id=countries.con_id and country_name='{cn}'")
                r = self.cursor.fetchall()

                self.cb3.clear()
                for i in r:
                    t = str(i[0])
                    t1 = int(t)
                    self.cursor.execute(f"select name from packages where pid={t1}")
                    r1 = self.cursor.fetchall()
                    for i in r1:
                        self.cb3.addItem(i[0])

                self.cursor.execute(
                    f"select con_name from countries,continents where countries.cid=continents.cid and country_name='{cn}'")
                # self.cb1.lineEdit().clear()
                c = self.cursor.fetchall()
                c1 = str(c[0][0])
                self.cb1.setCurrentText(c1)


            except Exception as e:
                print(e)
                traceback.print_exc()

        def get_img(self):
            try:
                global imageindex
                global lid_list
                self.pkg_img_lbl.clear()
                lid_list = []
                query1 = f" select pid from packages where name='{self.cb3.currentText()}'"
                self.cursor.execute(query1)
                selectedpid = self.cursor.fetchone()[0]

                self.cursor.execute(f"select lid from location where pid={selectedpid}")
                lids = self.cursor.fetchall()

                for i in lids:
                    w = str(i[0])
                    w1 = int(w)
                    lid_list.append(w)

                if imageindex == 0:
                    imageindex = lid_list[0]
                    imageindex = int(imageindex)

                a = str(imageindex)
                if a not in lid_list:
                    imageindex = lid_list[0]
                    imageindex = int(imageindex)

                self.cursor.execute(f"select image from location where lid={imageindex}")
                selectedimage = self.cursor.fetchone()[0]
                image = QtGui.QImage.fromData(selectedimage)
                pixmap = QPixmap.fromImage(image)
                self.pkg_img_lbl.setPixmap(pixmap)
                self.pkg_img_lbl.setPixmap(pixmap.scaled(self.pkg_img_lbl.width(), self.pkg_img_lbl.height()))

            except Exception as e:
                print(e)
                traceback.print_exc()

        def prev(self):
            try:
                global imageindex
                global lid_list
                imageindex -= 1
                a = lid_list[0]
                a = int(a)
                b = lid_list[-1]
                b = int(b)
                if imageindex == a:
                    self.prev_btn.setDisabled(True)

                if imageindex != b:
                    self.next_btn.setDisabled(False)
                # print(imageindex)
                self.get_img()

            except Exception as e:
                print(e)
                traceback.print_exc()

        def next(self):
            try:
                global imageindex
                global lid_list
                imageindex += 1

                a = lid_list[-1]
                a = int(a)
                b = lid_list[0]
                b = int(b)

                if imageindex == a:
                    self.next_btn.setDisabled(True)

                if imageindex != b:
                    self.prev_btn.setDisabled(False)

                self.get_img()


            except Exception as e:
                print(e)
                traceback.print_exc()

        def pkg_ele(self):
            try:

                self.prev_btn.show()
                self.next_btn.show()
                self.select_btn.show()

                global imageindex
                self.cursor.close()
                pkg_name = self.cb3.currentText()

                self.cursor = self.connection.cursor()
                self.cursor.execute(f"select description from packages where name='{pkg_name}'")
                d = self.cursor.fetchall()
                d1 = str(d[0][0])

                self.pkg_des_lbl.clear()
                self.pkg_des_lbl.setText(d1)
                self.pkg_des_lbl.setWordWrap(True)
                self.cursor.execute(f"select price from packages where name='{pkg_name}'")
                p = self.cursor.fetchall()
                p1 = str(p[0][0])
                self.pkg_price_lbl.clear()
                self.pkg_price_lbl.setText(f"Price-{p1}")

                self.cursor.execute(f"select duration from packages where name='{pkg_name}'")
                t = self.cursor.fetchall()
                t1 = str(t[0][0])
                self.pkg_dur_lbl.setText(f"duration-{t1}")
                self.pkg_name_lbl.setText(pkg_name)

                self.cursor.execute(f"select pid from packages where name='{pkg_name}'")
                pid1 = self.cursor.fetchall()
                pid = pid1[0][0]

                self.cursor.execute(f"select con_id from location where pid={pid}")
                con_id1 = self.cursor.fetchall()
                con_id = con_id1[0][0]
                self.cursor.execute(f"select country_name from  countries where con_id={con_id}")
                con_name1 = self.cursor.fetchall()
                con_name = str(con_name1[0][0])
                self.cb2.setCurrentText(con_name)

                self.cursor.execute(f"select cid from countries where con_id={con_id}")
                cid1 = self.cursor.fetchall()
                cid = cid1[0][0]
                self.cursor.execute(f"select con_name from continents where cid={cid}")
                c_name1 = self.cursor.fetchall()
                c_name = c_name1[0][0]
                self.cb1.setCurrentText(c_name)

                self.get_img()



            except Exception as e:
                print(e)
                traceback.print_exc()

        def temp(self):
            try:
                self.pkg = pkg_select()
                self.pkg.show()
                self.hide()
            except Exception as e:
                print(e)
                traceback.print_exc()

        def Home(self):
            self.h = HomePage()
            self.h.show()
            self.hide()

        def tours(self):
            self.pkg = Tours()
            self.pkg.show()
            self.hide()

        def flights(self):
            self.f = Flights()
            self.f.show()
            self.hide()

        def hotels(self):
            self.ho = Hotels()
            self.ho.show()
            self.hide()


    class pkg_select(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('select package')
            self.setGeometry(400, 200, 800, 750)
            self.setStyleSheet("background-color:#FFE5B4")

            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='sairam',
                database='dream_holidays'
            )
            self.cursor = self.connection.cursor()

            self.back_btn = QPushButton("Back", self)
            self.back_btn.setGeometry(700, 0, 90, 60)
            self.back_btn.clicked.connect(self.tours_page)

        def tours_page(self):
            try:
                self.T = Tours()
                self.T.show()
                self.hide()
            except Exception as e:
                traceback.print_exc()




    class Flights(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Dream Holidays')
            self.setGeometry(200, 200, 1350, 750)
            self.setStyleSheet("background-color:#FFE5B4")
            self.setStyleSheet("""
                 QWidget {
                    background-color: #FFE5B4;
                    border-radius: 10px;
                }
                 QPushButton:hover {
                    background-color: #0056b3;
                }

            """)

            self.home_button = QPushButton(self)
            self.home_button.setGeometry(100, 60, 200, 40)
            self.home_button.setStyleSheet(
                "padding: 10px;border-radius: 5px;font-size: 14px;background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/logo2);")
            self.home_button.clicked.connect(self.Home)

            self.tours_button = QPushButton("Tours", self)
            self.tours_button.setGeometry(330, 60, 170, 50)
            self.tours_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.tours_button.clicked.connect(self.temp)

            self.fli_button = QPushButton("Flights", self)
            self.fli_button.setGeometry(530, 60, 170, 50)
            self.fli_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.fli_button.clicked.connect(self.flights)

            self.hotel_btn = QPushButton("Hotels", self)
            self.hotel_btn.setGeometry(730, 60, 170, 50)
            self.hotel_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.hotel_btn.clicked.connect(self.hotels)

            self.abt_btn = QPushButton("About US", self)
            self.abt_btn.setGeometry(950, 60, 170, 50)
            self.abt_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")

        def Home(self):
            self.h = HomePage()
            self.h.show()
            self.hide()

        def temp(self):
            self.pkg = Tours()
            self.pkg.show()
            self.hide()

        def flights(self):
            self.f=Flights()
            self.f.show()
            self.hide()

        def hotels(self):
            self.ho = Hotels()
            self.ho.show()
            self.hide()


    class Hotels(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Dream Holidays')
            self.setGeometry(200, 200, 1350, 750)
            self.setStyleSheet("background-color:#FFE5B4")
            self.setStyleSheet("""
                    QWidget {
                       background-color: #FFE5B4;
                       border-radius: 10px;
                   }
                    QPushButton:hover {
                       background-color: #0056b3;
                   }

               """)

            self.home_button = QPushButton(self)
            self.home_button.setGeometry(100, 60, 200, 40)
            self.home_button.setStyleSheet(
                "padding: 10px;border-radius: 5px;font-size: 14px;background-image : url(C:/Users/XII Info/Downloads/harshith XII CAE/pycharm/dream_holidays/logo2);")
            self.home_button.clicked.connect(self.Home)

            self.tours_button = QPushButton("Tours", self)
            self.tours_button.setGeometry(330, 60, 170, 50)
            self.tours_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.tours_button.clicked.connect(self.tours)

            self.fli_button = QPushButton("Flights", self)
            self.fli_button.setGeometry(530, 60, 170, 50)
            self.fli_button.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.fli_button.clicked.connect(self.flights)

            self.hotel_btn = QPushButton("Hotels", self)
            self.hotel_btn.setGeometry(730, 60, 170, 50)
            self.hotel_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")
            self.hotel_btn.clicked.connect(self.hotels)

            self.abt_btn = QPushButton("About US", self)
            self.abt_btn.setGeometry(950, 60, 170, 50)
            self.abt_btn.setStyleSheet("padding: 10px;border-radius: 5px;font-size: 18px;")

        def Home(self):
            self.h = HomePage()
            self.h.show()
            self.hide()

        def tours(self):
            self.pkg = Tours()
            self.pkg.show()
            self.hide()

        def flights(self):
            self.f = Flights()
            self.f.show()
            self.hide()

        def hotels(self):
            self.ho = Hotels()
            self.ho.show()
            self.hide()


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main_window = MainWindow()

        main_window.show()
        sys.exit(app.exec_())

except Exception as e:
    print(e)