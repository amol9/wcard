import sys



class Arguments:
	def __init__(self):
		self.filename = None

	def parse(self):
		if len(sys.argv) > 1:		
			self.filename = sys.argv[1]
		else:
			raise Exception("please provide a filename")

	def get_filename(self):
		return self.filename
