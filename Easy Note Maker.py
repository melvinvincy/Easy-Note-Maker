#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import wikipedia 
import sys
import pyperclip
from PyQt5.QtWidgets import QMessageBox
from socket import gethostname, gaierror





class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Easy Note Maker")

		# setting geometry
		self.setGeometry(600, 600, 1010, 600)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

		# method for widgets
	def UiComponents(self):
        
		# creating a label
		self.label = QLabel(self)

		# setting geometry to the label
		self.label.setGeometry(5, 200, 1000, 300)

		# creating label multi line
		self.label.setWordWrap(True)

		# setting style sheet to the label
		self.label.setStyleSheet("QLabel"
								"{"
								"border : 4px solid black;"
								"background : white;"
                                 " padding :35px;"
								"}")

		# setting alignment to the label
		self.label.setAlignment(Qt.AlignLeft)

		# setting font
		self.label.setFont(QFont('Arial', 14))
		self.label1 = QLabel('Keyword Should be Specific...',self)
		self.label1.setFont(QFont('Arial', 8))
		self.label1.move(375, 95)
		self.label1.resize(280,35)
        


		# adding number button to the screen
		# creating a push button
		push1 = QPushButton("search", self)

		# setting geometry
		push1.setGeometry(605, 58, 80, 40)



		# clear button
		push_clear = QPushButton("Clear", self)
		push_clear.setGeometry(330, 510, 200, 40)

		# del one character button
		push_del = QPushButton("Del", self)
		push_del.setGeometry(700, 58, 80, 40)
        
		self.textbox = QLineEdit(self)
		self.textbox.move(300, 50)
		self.textbox.resize(280,50)
		self.textbox.setFont(QFont('Arial', 12))
		self.textbox.setAlignment(Qt.AlignLeft)
		textboxValue = self.textbox.text()
		
		
		# adding action to each of the button

		push1.clicked.connect(self.action1)
		push_clear.clicked.connect(self.action_clear)
		push_del.clicked.connect(self.action_del)


	 

	def action_point(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + ".")


	def action1(self):
		# appending label text
		textboxValue = self.textbox.text()
		try:
			result = wikipedia.summary(textboxValue)
			for x in result:
				self.label.setText(result)
				pyperclip.copy(result)
		except Exception:        
						msg = QMessageBox()
						msg.setWindowTitle("Error box")
						msg.setText("something went wrong")
						x = msg.exec_()

    
       
	def action_clear(self):
		# clearing the label text
		self.label.setText("")

	def action_del(self):
		# clearing a single digit
		text = self.textbox.text()
		self.textbox.setText(text[:len(text)-1])


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())


# In[ ]:





# In[ ]:





# In[ ]:




