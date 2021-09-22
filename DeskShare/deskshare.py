import socket
from tkinter.ttk import *
from tkinter import simpledialog, filedialog
from middleware.request import Requests

class MainFrame:
	def __init__(self, parent, console):
		self.console = console
		self.parent = LabelFrame(parent, text='Desk Share')
		self.IP = socket.gethostbyname(socket.gethostname())
		self.requests = Requests()
		self.load()

	def load(self):
		self.send = Button(self.parent, text='Send', 
			command = self.server)
		self.recv = Button(self.parent, text='Recv',
			command = self.client)
		self.IP_LABEL = Label(self.parent,
			text = 'Me : ' + self.IP)
		self.IP_LABEL.pack(padx=25, pady=5)
		self.send.pack(padx=25, pady=5)
		self.recv.pack(padx=25, pady=10)

	def server(self):
		self.SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.SERVER.bind((self.IP, 3030))
		self.SERVER.listen()
		address = filedialog.askdirectory()
		self.client, _ = self.SERVER.accept()
		self.console.display(' [*] connection successful')
		self.requests.GET(self.client, address, self.console)
		self.console.display(' [$] completed')
		
	def client(self):
		self.CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ip = simpledialog.askstring("IP Address", "Enter IP", parent=self.parent)
		self.CLIENT.connect((ip, 3030))
		self.console.display(' [*] connection successful')
		self.requests.POST(self.CLIENT, self.console)
		self.console.display(' [$] completed')
