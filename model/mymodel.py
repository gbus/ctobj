# mymodel.py - a tiny object model

from persistent import Persistent

class Host(Persistent):
	def __init__(self, hostname, ip, interfaces):
		self.hostname = hostname
		self.ip = ip
		self.interfaces = interfaces



class File(Persistent):
#	name
#	content-type
#	ctime
#	payload
#	md5
	payload = 0
	ctime = 0
	cotype = ""
	md5 = ""

	def __init__(self, name):
		self.name = name
	
	def register_data(input_file):
		pass

	def get_file():
		pass

	def set_time():
		pass

	def compute_md5():
		pass
