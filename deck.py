from card import *

class Deck():

	'''
	A class that allows the creation of a deck. The deck is created based on the Card() class. 
	We can perform 2 operations with the deck : shuffle the deck, deal on card of the back of deck
	'''

	def __init__(self):
		self.all_cards = []
		# An empty deck that we are going to fill. NOTE : Thanks to this attribute we can then check the length of the deck. deck.cards_deck

		for suit in suits :
			for rank in ranks :
				created_card = Card(suit, rank)
				self.all_cards.append(created_card)
		# Iteration through the 2 lists in 1st indentation (suits, ranks). Creation of the card with the class Card() and add the card to the empty deck. #

	def deal_one(self):
		return self.all_cards.pop()
		# NOTE : important to return the result. If not it will not be saved, which would be a problem when playing the game

	def shuffle(self, amount=3):
		for i in range(amount):
			random.shuffle(self.all_cards)
		# NOTE : important to call shuffle from the library random & to say what to shuffle (all_cards.deck) If not it does not work.

