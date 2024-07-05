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


'''
GAME SET UP --------------------------------------------------------------------------------------------------------------------------
'''
player_human = Player(input('Please Enter your name : ').upper()) #Create the Human player
player_computer = Player('COMPUTER') # Create the Computer player
print(f'The game opposes {player_human} to {player_computer}.')

game_deck = Deck() # create the deck
game_deck.shuffle() # shuffle the deck

# Distribute the cards between the player
for card_distributed in range(26): 
	player_human.add_cards(game_deck.deal_one())
	player_computer.add_cards(game_deck.deal_one())


'''
GAME INSTRUCTIONS / Explain the rules for the game -----------------------------------------------------------------------------------
'''
print(""" 
	W E L C O M E  T O  W A R !

	The rules are simple, play a card and pray to god that it is a 
	higher rank than your opponents card.

	If you play the same card rank as your opponent, it's WAR !
	You and your opponent will play 5 more cards, only the last one
	needs to be higher rank than your opponents second card.
	If it is, you get all the cards played that round.

	If the computer cannot play, you win !

	LET'S BEGIN ! """)
wait = input("press ENTER to start")  # all "wait" variables, are just there to wait for the player to input something

'''
ROUND LOGIC ---------------------------------------------------------------------------------------------------------------------------
'''
round_num = 0
game_on = True

while game_on == True:
	round_num += 1 #update the round number
	print(f'''
		
	----------------------------------------------------------------------------
	Round {round_num}

	''')

	print(player_human.number_cards()) #print how many card the Human player has
	print(player_computer.number_cards()) #same for the computer player

	''' CHECK IF CARDS REMAINING --------------------------------------------------------'''

	#Check if computer lost
	if len(player_computer.all_cards) == 0 :
		print(f"{player_computer}, you don't have any card left. {player_human} wins !")
		break

	#Check if computer lost
	elif len(player_human.all_cards) == 0 :
		print(f"{player_human}, you don't have any card left. {player_computer} wins !")
		break

	''' START THE ROUND ----------------------------------------------------------------- '''

	print('\nIt is time to play !')

	wait = input('press ENTER to play a card') #Human plays
	player_human_side = []
	player_human_side.append(player_human.remove_one())
	print(f'You played the card {player_human_side[-1]}.')

	player_computer_side = []
	wait = input(f'press ENTER to see what card {player_computer} plays') #Computer plays
	player_computer_side.append(player_computer.remove_one())
	print(f'{player_computer} played {player_computer_side[-1]}.')

	'''
	AT WAR -----------------------------------------------------------------------------------------------------------------------------
	'''
	at_war = True
	
	while at_war == True:
		# Card Human wins over Card Computer -> Human wins the cards
		if player_human_side[-1].value > player_computer_side[-1].value :
			print (f'\n{player_human} won this round with his card {player_human_side[-1]}')
			player_human.add_cards(player_computer_side) #add the card of the opponent
			player_human.add_cards(player_human_side) #add his cards back
			
			at_war = False

		# Card Computer wins over Card Human -> Computer wins the cards
		elif player_human_side[-1].value < player_computer_side[-1].value :
			print (f'\n{player_computer} won this round with its card {player_computer_side[-1]}')
			player_computer.add_cards(player_human_side)#add the card of the opponent
			player_computer.add_cards(player_computer_side) #add its cards back
			
			at_war = False


		else :
			print('\n WAR !!!! \n')
			if len(player_computer.all_cards) <5:
				print ('Computer unable to declare war')
				print (f'{player_human} WINS !')
				break
				game_on = False

			elif len(player_human.all_cards) <5:
				print (f'{player_human} unable to declare war')
				print (f'{player_computer} WINS !')
				break
				game_on = False

			for num in range(5):
				player_human_side.append(player_human.remove_one())
				player_computer_side.append(player_computer.remove_one())
			print(f'There was {len(player_computer_side)+len(player_human_side)} cards to win in this war')























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
