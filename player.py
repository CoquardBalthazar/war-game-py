class Player():
	''' 
	A class that symbolise the deck of a player / the cards hold by the player.
	'''

	def __init__(self, name):
		self.name = name
		self.all_cards = []

	def __str__(self):
		# A method that returns the name of the player
		return f'{self.name}'

	def number_cards(self):
		# a method that returns the number of cards hold by the player
		return f'{self.name} holds {len(self.all_cards)} cards.'

	def remove_one(self):
		# A method that remove the last card of the player's deck
		return self.all_cards.pop(0)

	def add_cards(self, new_cards):
		# A method that add one or many cards to the bottom of the player's deck
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else :
			self.all_cards.append(new_cards)

