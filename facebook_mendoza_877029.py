import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('PTSans.ttf')
    QFontDatabase.addApplicationFont('KlavikaBoldBold.otf')

    widget = QWidget()
    widget.setWindowTitle('facebook_mendoza_877029')
    widget.setFixedSize(800,600)
    widget.setStyleSheet(
        'background-color: #e6e7eb;'
    )
    
    uicomponents(widget)
    logotext(widget)
    subText(widget)

    widget.show()
    sys.exit(app.exec())
            

def logotext(parent):
    logo = QLabel(parent)
    logo.setText('facebook')
    logo.setFont(QFont('KlavikaBoldBold'))
    logo.setGeometry(50,100,280,50)
    logo.setStyleSheet(
        'font-size: 60px;'
        'font:bold;'
        'color: #3c5a99;'
    )

def subText(parent):
    sub = QLabel(parent)
    sub.setText('Connect with friends and the world')
    sub.setGeometry(50,160,300,50)
    sub.setStyleSheet(
        'font-size:15px;'
    )

    sub1 = QLabel(parent)
    sub1.setText('around you on Facebook.')
    sub1.setGeometry(50,200,180,15)
    sub1.setStyleSheet(
        'font-size:15px;'
    )
    

def loginSuccess(user,password, frame_login):
    correct_user = user
    correct_password = 1234

    if user == correct_user and correct_password:
        pass



def uicomponents(parent):
    first_name = QLineEdit(parent)
    first_name.setGeometry(400, 100, 350, 50)
    first_name.setPlaceholderText('Email or phone number: ')
    first_name.setStyleSheet(
        'border: 2px solid #172c80;'
        'font-size: 20px;'
        'color:Black;'
        'padding-left:10px;'
    )

    last_name = QLineEdit(parent)
    last_name.setGeometry(400, 170, 350, 50)
    last_name.setPlaceholderText('Password ')
    last_name.setStyleSheet(
        'border: 2px solid #172c80;'
        'font-size: 20px;'
        'color:black;'
        'padding-left: 10px;'
    )
    last_name.setEchoMode(QLineEdit.Password)

    button = QPushButton('Click to join', parent)
    button.setGeometry(400, 240, 350, 50)
    button.setStyleSheet(
        'border: 2px solid #172c80;'
        'font-size: 20px;'
        'color:black;'
        'padding-left: 10px;'
    )
    
    button.clicked.connect(lambda:loginSuccess())

    
window()