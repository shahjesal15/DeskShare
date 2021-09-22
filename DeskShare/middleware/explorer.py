import os
import xml.etree.ElementTree as XML

class Files:
	def __init__(self):
		self.EXPLORED = {}
		self.UNZIP = {}

	# CREATING XML TREE EXPLORING FOLDERS
	def explorer(self, xml):
		folders = os.listdir()
		# LOOKING THROUGH THE FOLDERS
		for data in folders:
			if os.path.isdir(data):
				# changes the folder route
				os.chdir(data)
				_folder = XML.SubElement(xml, 'folder', id=data)
				self.explorer(_folder)
				# changes the folder route to previous route on client side
				os.chdir('..')
			else:
				XML.SubElement(xml, 'file', id=data)
				# getting file path to be sent
				self.EXPLORED[data] = os.getcwd() + f'/{data}'

	def config(self, address):
		# changing dir to root folder
		os.chdir(address)
		# XML
		xml = XML.Element('root', id=address.split('/')[-1])
		self.explorer(xml)
		os.chdir('..')
		tree = XML.ElementTree(xml)
		tree.write('index.xml', encoding='UTF-8')

	# PARSING XML TO CREATE FILE TREES
	def create(self, body):
		for part in body:
			data = part.attrib.get('id')
			if part.tag == 'folder':
				try:
					os.mkdir(data)
				except Exception as error:
					pass
				os.chdir(data)
				self.create(part)
				os.chdir('..')
			else:
				with open(data, 'w') as file:
					self.UNZIP[data] = os.getcwd() + f'/{data}'

	def unzip(self, name):
		fileTree = XML.parse(name)
		rootDir = fileTree.getroot()
		rootDirName = rootDir.attrib.get('id')
		try:
			os.mkdir(rootDirName)
		except Exception as error:
			pass
		os.chdir(rootDirName)
		self.create(rootDir)