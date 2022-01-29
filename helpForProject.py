import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    QFontDatabase.addApplicationFont('Lobster.ttf')

    #size of window
    widget.setFixedSize(800,600)
    #title of window
    widget.setWindowTitle('monkey time')

    #testInConsole()
    #testParametersInConsole('computer','science')
    firstOfEachWord('Thomas','Mendoza')

    #create a QLabel object
    #put at location 25,25
    #width 150
    #height 50
    #add some style

    outputLabel = QLabel(widget)
    outputLabel.setText(firstOfEachWord('joe','mama'))
    outputLabel.setGeometry(25,25,150,50)
    outputLabel.setFont(QFont('Lobster'))
    outputLabel.setStyleSheet(
        'background-color:blue;'
        'color:white;'
        'padding-right:20px;'
        'font-size:20px;'
    )

    textEdit = QLineEdit(widget)
    textEdit.setPlaceholderText('Text will go into label')
    textEdit.setGeometry(25,140,150,50)
    textEdit.setStyleSheet(
        'background-color:white;'
        'color:black;'
    )

    #QButton called click_me
    clickMe = QPushButton(widget)
    clickMe.setText('Click me')
    clickMe.setGeometry(25,80,150,50)
    clickMe.setStyleSheet(
        'background-color:red;'
        'font-size:20px;'
        'color:white;'
    )

    clickMe.clicked.connect(lambda:outputLabel.setText(textEdit()))

    widget.show()
    sys.exit(app.exec_())



def testInConsole():
    print('Thomas Mendoza')
    
def testParametersInConsole(first,last):
    print(first,last)

def firstOfEachWord(first, second):
    return first[0] + ' ' + second[0]


if __name__ == '__main__': 
    window()
