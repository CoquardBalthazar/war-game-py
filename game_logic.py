from card import *
from deck import *
from player import *
from instructions import *
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

def run_game():
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
  print_instruction()
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
