
class Types:
		types = ["noun", "adverb", "adjective", "verb", "place", "fantasy"]

	def has_types(self, s):
		if s.strip() in Types.types:
			return True


class InputFile:
	def __init__(self):
		self.lines = None

	def read(self, filename):
			with open(filename, 'r') as f:
				self.lines = f.readlines()

	def get_lines(self):
		return self.lines


class Parser:
		up_arrow = b'\\u2191'

	def __init__(self):
		self.cards = []

	def parse(self):
		card = None 
		detail = None
		ftype = False
		fdetail = False

		args = Arguments()
		args.parse()

		ifile = InputFile()
		ifile.read(args.get_filename())

		for line in ifile.get_lines():
			if line[0:3] == "###":
				if card is not None:
					self.cards.append(card)
				if detail is not None:
					card.details.append(detail)

				card = Card()
				card.title = line[4:].strip().rstrip(up_arrow.decode("unicode_escape"))


				detail = None
				continue

			if line.strip()[0:3] == "![]":
				card.images.append(line.strip())
				continue

			if line.strip() == "":
				card.count += 1
				if fdetail:
					fdetail = False
					ftype = False

			'''if card.count == 1:
				continue'''

			types = Types()
			if types.has_types(line):
				if detail is not None:
					card.details.append(detail)
				detail = Detail()
				detail.type = line.strip()
				card.count = 2
				ftype = True
				continue

			'''if card.count == 2:
				card.type += line.strip()
				continue'''

			if ftype:
				detail.text += line.strip()
				fdetail = True
				continue

			'''if card.count == 4:
				card.type += line.strip()
				continue'''


