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
        'background-color:grey;'
    )

    makeClassroom(widget,0,0,'blue')
    #makeClassroom(widt,270,)

    widget.show()
    sys.exit(app.exec_())

def makeClassroom(parent,x,y,color):
    
    classBox = QFrame(parent)
    classBox.setGeometry(x+25,y+25,250,300)
    classBox.setStyleSheet(
        'background-color:white;'
        'border-radius: 6px;'
    )

    classroomTop = QFrame(classBox)
    classroomTop.setGeometry(0,0, 250,80)
    classroomTop.setStyleSheet(
        'background-color:'+ color + ';'
        'border-bottom-radius:0px;'

    )

    classroomMiddle = QFrame(classBox)
    classroomMiddle.setGeometry(0,80,250,160)
    classroomMiddle.setStyleSheet(
        'border-top-style: solid;'
        'border-width: 5px;'
        'border-radius: 0px;'
    )

    #classroomBottom = QFrame(classBox)

if __name__ == '__main__':
    window()