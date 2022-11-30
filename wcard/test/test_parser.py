import unittest as ut


class TestParser(ut.TestCase):

	def test_one(self):
		parser = Parser()
		parser.parse()

		for card in parser.get_cards():
			card.show()
			print("-")


