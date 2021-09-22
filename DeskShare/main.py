from tkinter.ttk import *
import tkinter 
import tkinter.font as font
from ttkthemes import ThemedTk
import webbrowser
from deskshare import MainFrame
from console import Console
from menu import MenuBar

class App:
	def __init__(self):
		self.parent = ThemedTk(theme='calm')
		self.parent.title('DS')
		self.parent.geometry('520x420')
		self.parent.resizable(False, False)
		self.console = Console(self.parent)
		self.deskshare = MainFrame(self.parent, self.console)
		self.deskshare.parent.pack(fill='both', padx=10, pady=10)
		self.console.parent.pack(fill='both', padx=10, pady=10)
		self.menubar = MenuBar(self.parent)
		self.load()

	def load(self):
		self.instagram = Button(self.parent, text="Info",
			command = lambda:webbrowser.open("https://www.instagram.com/shahjesal11/"))
		self.nametag = Label(self.parent, text="Shah Jesal")
		self.nametag.config(font=("Serif", 10))
		self.instagram.pack(side=tkinter.LEFT, padx=12, pady=5)
		self.nametag.pack(side=tkinter.RIGHT, padx=12, pady=5)

	def run(self):
		self.parent.config(menu=self.menubar.menubar)
		self.parent.mainloop()

app = App()
app.run()
