import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('\Roboto-Bold.ttf')
    widget = QWidget()
    widget.setFixedSize(1200,1600)
    widget.setWindowTitle('GoogleClassroom_mendoza_877029')
    widget.setFont(QFont('Roboto-Bold'))
    widget.setStyleSheet(
        'background-color:white;'
    )

    classLogo(widget)
    classBox(widget)

    widget.show()
    sys.exit(app.exec_())

def classLogo(parent):
    label = QLabel(parent)
    pixmap = QPixmap('classroomlogo.PNG')
    label.setPixmap(pixmap)

def classBox(parent):
    box1 = QFrame(parent)
    box1.setGeometry(20,100,300,400)
    box1.setStyleSheet(
        'background-color:#ededed;'
    )
    classColor1 = QLabel(box1)
    classColor1.setGeometry(0,0,300,100)
    classColor1.setStyleSheet(
        'background-color:#407ae6;'
    )
    title1 = QLabel(box1)
    title1.setText('NTHS')
    title1.setGeometry(30,10,200,50)
    title1.setStyleSheet(
        'font-size:20px;'
        'background-color:#407ae6;'
        'color:white;'
    )
    teacher1 = QLabel(box1)
    teacher1.setText('Amber Hall')
    teacher1.setGeometry(30,20,90,20)
    teacher1.setStyleSheet(
        'background-color:#407ae6;'
        'color:white;'
    )
    
    box2 = QFrame(parent)
    box2.setGeometry(330,100,300,400)
    box2.setStyleSheet(
        'background-color:#ededed;'
    )
    classColor2 = QLabel(box2)
    classColor2.setGeometry(0,0,300,100)
    classColor2.setStyleSheet(
        'background-color:Grey'
    )
    title2 = QLabel(box2)
    title2.setText('Midwest Percussion')
    title2.setGeometry(30,10,200,50)
    title2.setStyleSheet(
        'font-size:20px;'
        'background-color:Grey;'
        'color:white;'
    )
    
    
    box3 = QFrame(parent)
    box3.setGeometry(640,100,300,400)
    box3.setStyleSheet(
        'background-color:#ededed;'
    )
    classColor3 = QLabel(box3)
    classColor3.setGeometry(0,0,300,100)
    classColor3.setStyleSheet(
        'background-color:#024cba'
    )
    title3 = QLabel(box3)
    title3.setText('Mu Alpha Theta')
    title3.setGeometry(30,10,200,50)
    title3.setStyleSheet(
        'font-size:20px;'
        'background-color:#024cba;'
        'color:white;'
    )
    
    
    box4 = QFrame(parent)
    box4.setGeometry(20,510,300,400)
    box4.setStyleSheet(
        'background-color:#ededed;'
    )
    classColor4 = QLabel(box4)
    classColor4.setGeometry(0,0,300,100)
    classColor4.setStyleSheet(
        'background-color:black'
    )
    title4 = QLabel(box4)
    title4.setText('LHS Wind Ensemble')
    title4.setGeometry(30,10,200,50)
    title4.setStyleSheet(
        'font-size:20px;'
        'background-color:black;'
        'color:white;'
    )
    
    
    box5 = QFrame(parent)
    box5.setGeometry(330,510,300,400)
    box5.setStyleSheet(
        'background-color:#ededed;'
    )
    classColor5 = QLabel(box5)
    classColor5.setGeometry(0,0,300,100)
    classColor5.setStyleSheet(
        'background-color:#ff63e8'
    )
    title5 = QLabel(box5)
    title5.setText('AP Statistics')
    title5.setGeometry(30,10,200,50)
    title5.setStyleSheet(
        'font-size:20px;'
        'background-color:#ff63e8;'
        'color:white;'
    )


    box6 = QFrame(parent)
    box6.setGeometry(640,510,300,400)
    box6.setStyleSheet(
        'background-color:#ededed;'
    )
    classColor6 = QLabel(box6)
    classColor6.setGeometry(0,0,300,100)
    classColor6.setStyleSheet(
        'background-color:#024cba'
    )
    title6 = QLabel(box6)
    title6.setText('LHS Class of 2022')
    title6.setGeometry(30,10,200,50)
    title6.setStyleSheet(
        'font-size:20px;'
        'background-color:#024cba;'
        'color:white;'
    )

if __name__ == '__main__':
    window()