class Card:
	def __init__(self):
		self.title = None
		self.type = ""
		self.details = []
		self.images = []
		self.count = 1

	def show(self):
		print("Title: ", self.title)
		#print("Type: ", self.type)
		for d in self.details:
			d.show()
		print("Images: ", self.images)
		print("Count: ", self.count)










