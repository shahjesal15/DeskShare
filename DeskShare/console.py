from tkinter import *
from tkinter.ttk import *

class Console:
	def __init__(self, parent):
		self.parent = LabelFrame(parent, text="Console")
		self.output = Text(self.parent, width=120, height=10)
		self.output.insert(END, 'transfer info here...\n')
		self.output["bg"] = "black"
		self.output["fg"] = "white"
		self.output.pack(padx=10, pady=10)

	def display(self, text):
		self.output.insert(END, text + "\n")
		self.output.see('end')
		self.parent.update()
