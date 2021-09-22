from tkinter import *
import sys
import os

class MenuBar:
	def __init__(self, parent):
		self.menubar = Menu(parent)
		filemenu = Menu(self.menubar)
		helpmenu = Menu(self.menubar)
		filemenu.add_command(label='Exit', command=lambda: sys.exit())
		helpmenu.add_command(label='About', command=lambda: os.system("start \"\" \"READme.md\""))
		self.menubar.add_cascade(label='File', menu=filemenu)
		self.menubar.add_cascade(label='Help', menu=helpmenu)
