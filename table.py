from card import *
from deck import *
from player import *

'''
DRAFT Class Table
'''
class Table(Player):
	# A Class that represent the table : 2 opposing sides that can take card, remove card, can be compared, merge.

	def __init__(self):
		self.side_human = []  #Side from the Player human == were the player human plays his cards
		self.side_computer = [] #identical but for the Player computer
		self.all_cards = [] # a list for the cards won in the round

	def __str__ (self): #a methods that prints if the table is empty or not
		if self.side_computer == [] and self.side_human == [] and self.all_cards == [] :
			return 'No cards are on the table'
		else :
			return 'Some cards are on the table'

	def add_cards_side_human(self, new_cards):
		# A method that add one or many cards to the table on as played by the human player

		if type(new_cards) == type([]):
			self.side_human.extend(new_cards)

		else :
			self.side_human.append(new_cards)

	def add_cards_side_computer(self, new_cards):
		# A method that add one or many cards to the table on as played by the human player

		if type(new_cards) == type([]):
			self.side_computer.extend(new_cards)

		else :
			self.side_computer.append(new_cards)

	def compare(self, stack_one, stack_two) : #Method that compare 2 stacks of cards, or more exactly compare the last cards (element [-1]) from the stacks (list).
		if stack_one[-1].value > stack_two[-1].value :
			return 'side_one'

		if stack_one[-1] < stack_two[-1] :
			return 'side_two'
		
		else :
			return 'draw'

	def merge(self, stack_one, stack_two) : #Method that merge two stacks of cards and save them in a last one. It does NOT shuffle.
		new_stack = stack_one.extend(stack_two)
		return new_stack
