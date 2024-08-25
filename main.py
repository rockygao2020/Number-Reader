import numpy as np
import numpy.linalg as npla
from symbol import Symbol, categorize_img, vectorize_img

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

CANVAS_SIZE = 20
PIXEL_SIZE = 20

class Canvas(QtWidgets.QLabel):
	'''A QLabel that holds a canvas; When writing event handlers in this class definition,
	   we register mouse-events with locations respective to the CANVAS/LABEL, not the whole APP.

	   This is useful because creating a Label(with canvas/pixmap) and its 
	   drawing helper functions(event handlers) inside of the MAIN APP definition means
	   all mouse-events have locations respective to the main app window, NOT our canvas > resize window, 
	   and you can no longer draw where your mouse points'''


	def __init__(self):
		super().__init__()

		#Create Canvas for drawing "pimap"; Link it to a Label "self"
		self.my_pixmap = QtGui.QPixmap(CANVAS_SIZE * PIXEL_SIZE, CANVAS_SIZE * PIXEL_SIZE)
		self.my_pixmap.fill(Qt.white)
		self.setPixmap(self.my_pixmap)

		#Point A of a Line AB
		self.last_x, self.last_y = None, None

		#Default Color
		self.pen_color = QtGui.QColor('#000000')

	def set_pen_color(self, c):
		self.pen_color = QtGui.QColor(c)

	def mouseMoveEvent(self, e):
		'''When Mouse is clicked and dragged, come here to draw on canvas
    	   Note: We don't need a click-mouse-event because by default an event is 
    	   always triggered when we click on the mouse. We'd need an even handler
    	   for tracking the mouse UNCLICKED'''

		print('MOUSE')
		# First event. Store point A as current cursor location, then ignore/return
		if self.last_x is None:
			self.last_x = e.x()
			self.last_y = e.y()
			return

		# Create QPainter Object
		painter = QtGui.QPainter(self.pixmap())
		p = painter.pen()
		p.setWidth(20)
		p.setColor(self.pen_color)
		painter.setPen(p)

		# This time, signal/slot is showing the event location for point B
		painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
		# All drawing stops at the end method
		painter.end()
		
		#Testing: Painter alters self.my_pixmap, but doesn't show up on the Qlabel "Canvas"
		#	When we do Cavnas.setPixmap(self.my_pixmap), we are creating a second pixmap tied to 
		#	the Canvas. It's what's showed on screen, but not my_pixmap, and painter doesn't alter it
		#self.setPixmap(self.my_pixmap)
		
		self.update()

		# Update the point A for next time(= next click cycle or 'tick') > one line is made of smaller ones
		self.last_x = e.x()
		self.last_y = e.y()

	def mouseReleaseEvent(self, e):
		'''Releasing the mouse means we forget the stored point A'''
		self.last_x = None
		self.last_y = None

	def save_image(self):
		#image = self.my_pixmap.toImage()
		#image.save("input.png")

		self.scaled_pixmap = self.pixmap().scaled(20, 20, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.SmoothTransformation)

		self.scaled_pixmap.save("input.png", "PNG")
		print("Image saved as input.png")

	def reset_image(self):
		self.setPixmap(self.my_pixmap)

    	
class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		#Add the canvas to layout
		self.setWindowTitle("Symbol Reader")
		self.setFixedSize(CANVAS_SIZE * PIXEL_SIZE, CANVAS_SIZE * PIXEL_SIZE + 50)
		self.canvas = Canvas()
		l = QtWidgets.QGridLayout()
		l.addWidget(self.canvas, 0, 0, 1, 3)
		
		#Add the save button to layout
		self.save_button = QtWidgets.QPushButton("Classify")
		self.save_button.clicked.connect(self.save_image)
		l.addWidget(self.save_button, 1, 0)

		#Add the output to layout
		self.output = QtWidgets.QPlainTextEdit()
		self.output.setPlainText("This digit is...")
		self.output.setMaximumHeight(30)
		self.output.setReadOnly(True)
		l.addWidget(self.output, 1, 1)

		#Add reset to layout
		self.reset = QtWidgets.QPushButton("Reset Canvas")
		self.reset.clicked.connect(self.reset_image)
		l.addWidget(self.reset, 1, 2)

		#Add the layout to widget
		w = QtWidgets.QWidget()
		w.setLayout(l)

		self.setCentralWidget(w)

	def save_image(self):
		'''Save the image drawn as a 20x20 pixel PNG; classify the number'''
		
		#saves the image using helper function, as "input.png"
		self.canvas.save_image()

		'''============================== SET UP ALL 10 DIGITS WITH THEIR COMPLETED BASES =============================='''
		zero = Symbol('0')
		one = Symbol('1')
		two = Symbol('2')
		three = Symbol('3')
		four = Symbol('4')
		five = Symbol('5')
		six = Symbol('6')
		seven = Symbol('7')
		eight = Symbol('8')
		nine = Symbol('9')

		test_size = 15
		zero_path = 'tests\\0_cases'
		one_path = 'tests\\1_cases'
		two_path = 'tests\\2_cases'
		three_path = 'tests\\3_cases'
		four_path = 'tests\\4_cases'
		five_path = 'tests\\5_cases'
		six_path = 'tests\\6_cases'
		seven_path = 'tests\\7_cases'
		eight_path = 'tests\\8_cases'
		nine_path = 'tests\\9_cases'

		zero.readTestCases(test_size, zero_path)
		one.readTestCases(test_size, one_path)
		two.readTestCases(test_size, two_path)
		three.readTestCases(test_size, three_path)
		four.readTestCases(test_size, four_path)
		five.readTestCases(test_size, five_path)
		six.readTestCases(test_size, six_path)
		seven.readTestCases(test_size, seven_path)
		eight.readTestCases(test_size, eight_path)
		nine.readTestCases(test_size, nine_path)

		symbol_list = [zero, one, two, three, four, five, six, seven, eight, nine]

		image_path = f"input.png"
		closest_symbol, min_res, residuals = categorize_img(vectorize_img(image_path), symbol_list)
		self.output.setPlainText(f"{closest_symbol.getName()}!")



	def reset_image(self):
		self.canvas.reset_image()
		self.output.setPlainText(f"This digit is...")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()