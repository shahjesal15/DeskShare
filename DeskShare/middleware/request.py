import time
import pickle
import os
from middleware.explorer import Files

class Requests:
	def __init__(self):
		self.CHUNK_SIZE = 102400
		self.running = True
		self.files = Files()
		self.delay = lambda: time.sleep(1/100)

	def GET(self, socket, address, console):
		self.console = console
		while self.running:
			request = socket.recv(self.CHUNK_SIZE)
			request = pickle.loads(request)
			if request["request"] == "XML":
				self.files.config(address)
				self.upload("index.xml", socket)
				self.console.display(' [>] information uploaded')
			elif request["request"] == "FILE":
				self.upload(self.files.EXPLORED[request["name"]], socket)
			elif request["request"] == "close":
				self.running = False

	def upload(self, path, socket):
		response = {"size": os.stat(path).st_size}
		response = pickle.dumps(response)
		socket.send(response)
		self.delay()
		with open(path, "rb") as uploader:
			while True:
				chunk = uploader.read(self.CHUNK_SIZE) # 100KB speed
				if not chunk:
					break
				socket.send(chunk)
				self.delay()
		self.console.display(f' [>] {path} uploaded')

	def POST(self, socket, console):
		self.console = console
		request = {"request": "XML"}
		request = pickle.dumps(request)
		socket.send(request)
		self.download("index.xml", socket)
		self.console.display(' [>] information downloaded')
		self.files.unzip("index.xml")
		self.console.display('files unzipped')
		for file in self.files.UNZIP:
			request = {"request":"FILE", "name":file}
			request = pickle.dumps(request)
			socket.send(request)
			self.download(self.files.UNZIP[file], socket)
		request = {"request": "close"}
		request = pickle.dumps(request)
		socket.send(request)

	def download(self, path, socket):
		response = socket.recv(self.CHUNK_SIZE)
		response = pickle.loads(response)
		with open(path, "wb") as downloader:
			CHUNK_SIZE = 0
			while True:
				chunk = socket.recv(self.CHUNK_SIZE)
				downloader.write(chunk)
				if CHUNK_SIZE > response["size"]:
					break
		self.console.display(f' [>] {path} downloaded')

