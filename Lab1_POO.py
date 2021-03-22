# This is the first Lab of Object Oriented Programming
# Monday March 22nd

from numpy import *
P1_name = ''
P2_name = ''

def user_input():
    
    cards = int(input('How many cards will the players have?'))
    P1_name = input('What is the name of the first player?')
    P2_name = input('What is the name of the second player?')
    P1_points = 0
    P2_points = 0
    
    return cards, P1_name, P2_name

def game_setup(cards):
    cards_P1 = range(cards)
    cards_P2 = range(cards)

    cards_P1.random.shuffle()
    cards_P2.random.shuffle()

    return cards_P1, cards_P2

user_input()
#game_setup(user_input[0])

    



