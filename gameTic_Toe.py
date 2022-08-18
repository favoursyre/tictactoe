#I want to create a Tic Tac Toe game app in this section

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QStatusBar, QPushButton, QFileDialog
from PyQt5 import uic, QtWidgets, QtCore, QtGui
import sys

class UI_Game(QMainWindow):
    def setupUi_Game(self, imgWindow):

        #Section for loading the image viewer UI file that will be needed
        uic.loadUi("gameTic.ui", self) 

        self.counter = 0 #This helps to keep track of the turns that will be taken
        self.pauseCounter = 0 #This keeps track of when the press/pause is pressed

        #Defining the various widgets for the image viewer window
        self.ticToeLabel = self.findChild(QLabel, "gameLabel")
        self.button1 = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")
        self.button11 = self.findChild(QPushButton, "pushButton_11")
       
        #Button functionalities for main window
        self.button1.clicked.connect(lambda: self.clicker(self.button1)) #Its passing in the button to serve as a parameter
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)
        self.button11.clicked.connect(self.pauseGame)

        self.show()

    def clicker(self, b): #This section is for the selection button
        if self.counter % 2 == 0: #When the counter is even it displays X on the clicked button and O for odd numbers 
            mark = "X"
            self.ticToeLabel.setText("0's Turn") #Immediately it presses x, it displays O's turn
        else:
            mark = "O"
            self.ticToeLabel.setText("X's Turn")
        b.setText(mark) #This displays the mark
        b.setEnabled(False) #This disables the button after it has been clicked
        self.counter += 1 #This increases the counter
        self.checkWin() #This checks who won the game 

    def pauseGame(self): #This function is for pausing/resuming functionality 
        if self.pauseCounter % 2 == 0: #When it's even the pause function happens and resume function for the odd
            self.freeze()
            self.button11.setText("Resume") #This resets the button text
        else:
            self.unfreeze()
            self.button11.setText("Pause")
        self.pauseCounter += 1 #This increments to check the action to take

    def freeze(self): #This function is for pausing the functionalities of the buttons
        buttonList = [
                self.button1,
                self.button2,
                self.button3,
                self.button4,
                self.button5,
                self.button6,
                self.button7,
                self.button8,
                self.button9
            ]
        for b in buttonList:
            b.setEnabled(False)

    def unfreeze(self): #This function is for resuming the functionalities of the buttons
        buttonList = [
                self.button1,
                self.button2,
                self.button3,
                self.button4,
                self.button5,
                self.button6,
                self.button7,
                self.button8,
                self.button9
            ]
        for b in buttonList:
            b.setEnabled(True)

    def checkWin(self): #This functions handles the winner checker, declaring the instances the game will be won 
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.win(self.button1, self.button4, self.button7) #This calls the winning notification on the checked buttons
            self.freeze() #It then pauses the game
        elif self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.win(self.button2, self.button5, self.button8) #This calls the winning notification on the checked buttons
            self.freeze() #It then pauses the game
        elif self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            self.win(self.button3, self.button6, self.button9) #This calls the winning notification on the checked buttons
            self.freeze() #It then pauses the game
        elif self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.win(self.button1, self.button2, self.button3) #This calls the winning notification on the checked buttons
            self.freeze() #It then pauses the game
        elif self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.win(self.button4, self.button5, self.button6) #This calls the winning notification on the checked buttons
            self.freeze() #It then pauses the game
        elif self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.win(self.button7, self.button8, self.button9) #This calls the winning notification on the checked buttons
            self.freeze() #It then pauses the game
        elif self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.win(self.button1, self.button5, self.button9) #This calls the winning notification on the checked buttons
            self.freeze() #It then pauses the game
        elif self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            self.win(self.button3, self.button5, self.button7) #This calls the winning notification on the checked buttons
            self.freeze() #It then pauses the game
        else:
            pass

    def win(self, a, b, c): #This checks handle the winning notification
        a.setStyleSheet("QPushButton {color: red;}") #This colors the victory button to red
        b.setStyleSheet("QPushButton {color: red;}")
        c.setStyleSheet("QPushButton {color: red;}")
        self.ticToeLabel.setText(f"{a.text()} Wins!") #This displays the winner on the game 

    def reset(self):
        buttonList = [
                self.button1,
                self.button2,
                self.button3,
                self.button4,
                self.button5,
                self.button6,
                self.button7,
                self.button8,
                self.button9
            ]
        
        for b in buttonList:
            b.setText("")
            b.setEnabled(True)
            b.setStyleSheet("QPushButton {color: #797979;}")

        self.ticToeLabel.setText("X Starts!")
        self.counter = 0

gameApp = QApplication(sys.argv)
fourthWindow = QtWidgets.QMainWindow()
UIWindowGame = UI_Game()
UIWindowGame.setupUi_Game(fourthWindow)
gameApp.exec_()
