import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
	'''
	A class that allows the creation of card, by giving their suit and their ranks. Based on the rank, the value of the card is also given
	''' 
	
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]
		
		# print(f'{rank} of {suit} created.')
		# With one card created it is interesting, but when creating a deck its problematic

	def __str__ (self):
		return self.rank + " of " + self.suit