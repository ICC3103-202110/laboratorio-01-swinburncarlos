from numpy import *
import math

# RULES OF THE GAME
# 1) choose a number for two pairs of cards. If you choose 5, then you will get 10 cards. For example you main deck will be: [1,2,3,4,5,1,2,3,4,5]
# 2) The main deck of cards will be shown with the positions of the cards. If you chose 5 pairs, then 
#    the main deck will look like: ['*1*', '*2*', '*3*', '*4*', '*5*', '*6*', '*7*', '*8*', '*9*', '*10*']
# 3) During you're turn, you get to choose two cards that will be flipped over. If they are not the same, then it will be the next players turn.
#    However, if the cards are the same, then '0' will replace the slot of the card (meaning that the slot is empty) and you will get a point.
# 4) If a player chooses an empty slot (if the player chooses '0') instead of a number, then the score will not be true. 
#    In this case restart the game. 
# 5) The game will come to an end when all the cards are '0' in which case a player will win or the players will tie. 
# 5) Enjoy the game !! 

cards = int(input('How many pairs of cards will you be playing with today?: '))
cards1 = range(1,cards+1) # creating first pair of cards
cards2 = range(1,cards+1) # creating second pair of cards
random.shuffle(cards1) # shuffling cards
random.shuffle(cards2)
Cards = []
for i in cards1: # adding first pair to main deck
    Cards.append(i)
for j in cards2: # adding second pair to main deck
    Cards.append(j)
position_of_cards = []
positions = []
for k in range(1,len(Cards)+1): # creating list with positions of cards
    position_of_cards.append('*'+str(k)+'*')
    positions.append('*'+str(k)+'*') # creating secondary list with positions of cards to reset primary list

# IF YOU WISH TO SEE THE DECK OF CARDS WHILE YOU PLAY PRINT THE FOLLOWING: 
#print(Cards,'Cards') 

pointsP1 = 0
pointsP2 = 0
turns = 0
num1 = 0
num2 = 0
cards_chosen = []

while position_of_cards.count(str(0)) != len(position_of_cards): # the game will continue unless position_of_cards is full of '0' 
    if turns % 2 == 0: # Player 1 plays when turns is an even number
        print('                  ')
        print('ITS PLAYER 1s TURN')
        print(position_of_cards)

        while num1 <= 1: # this while allows the first player to play two cards during their turn
            
            x = int(input('What position of card will you choose?  '))
            position_of_cards.pop(x-1) # eliminating the element of the list that the player chose
            position_of_cards.insert(x-1, Cards[x-1]) # adding to the list the card chosen 
            cards_chosen.append(x) # adding the positions of the cards chosen in order to check if they are the same later
            print(position_of_cards)
            num1 += 1 

        if Cards[cards_chosen[0] - 1] == Cards[cards_chosen[1] - 1]: # using the cards_chosen in order to find and compare the cards with the Cards list
            position_of_cards.pop(cards_chosen[0] - 1) # if its true that both cards are the same, the first card gets eliminated from the position_of_cards list
            position_of_cards.pop(cards_chosen[1] - 2) # second card gets eliminated from list. The -2 is because the list got smaller by one element
            position_of_cards.insert(cards_chosen[0] - 1, str(0)) # adding *0* in place for the card that was taken out of the deck. 0 represents an empty spot
            position_of_cards.insert(cards_chosen[1] - 1, str(0))
            pointsP1 += 1 # since the player chose two cards that are the same, they get 1 point
        
        elif Cards[cards_chosen[0] - 1] != Cards[cards_chosen[1] - 1]: # Reseting position_of_cards
            position_of_cards.pop(cards_chosen[0] - 1) # removing first card chosen 
            position_of_cards.pop(cards_chosen[1] - 2) # removing second card chosen 
            position_of_cards.insert(cards_chosen[0] - 1, '*'+str(cards_chosen[0])+'*') # adding again *number* so that position_of_cards is the same as before which means it wont show the other player the cards chosen
            position_of_cards.insert(cards_chosen[1] - 1, '*'+str(cards_chosen[1])+'*')
        
        turns += 1
        print('Player 1 has: '+ str(pointsP1) + ' points so far')
        num1 = 0 # resetting counter for the two turns of player one
        cards_chosen.pop() # erasing cards_chosen list so its clear and ready for the next turn
        cards_chosen.pop()

        if position_of_cards.count(str(0)) == len(position_of_cards):
            if pointsP1 > pointsP2:
                print('--------------------------------------------')
                print('PLAYER 1 WON')
                print('--------------------------------------------')

            elif pointsP1 == pointsP2:
                print('--------------------------------------------')
                print('ITS A TIE')
                print('--------------------------------------------')

    else:
        print('                  ')
        print('ITS PLAYER 2s TURN')
        print(position_of_cards)

        while num2 <= 1: # this while allows the second player to play two cards during their turn     
            x = int(input('What position of card will you choose?  '))
            position_of_cards.pop(x-1) # eliminating the element of the list that the player chose
            position_of_cards.insert(x-1, Cards[x-1]) # adding to the list the card chosen 
            print(position_of_cards)
            cards_chosen.append(x) # adding the positions of the cards chosen in order to check if they are the same later
            num2 += 1 

        if Cards[cards_chosen[0] - 1] == Cards[cards_chosen[1] - 1]: # using the cards_chosen in order to find and compare the cards with the Cards list
            position_of_cards.pop(cards_chosen[0] - 1) # if its true that both cards are the same, the first card gets eliminated from the position_of_cards list
            position_of_cards.pop(cards_chosen[1] - 2) # second card gets eliminated from list
            position_of_cards.insert(cards_chosen[0] - 1, str(0)) # adding *0* in place for the card that was taken out of the deck. 0 represents an empty spot
            position_of_cards.insert(cards_chosen[1] - 1, str(0))
            pointsP2 += 1 # since the player chose two cards that are the same, they get 1 point

        elif Cards[cards_chosen[0] - 1] != Cards[cards_chosen[1] - 1]:
            position_of_cards.pop(cards_chosen[0] - 1) # removing first card chosen 
            position_of_cards.pop(cards_chosen[1] - 2) # removing second card chosen 
            position_of_cards.insert(cards_chosen[0] - 1, '*'+str(cards_chosen[0])+'*') # adding again *number* so that position_of_cards is the same as before which means it wont show the other player the cards chosen
            position_of_cards.insert(cards_chosen[1] - 1, '*'+str(cards_chosen[1])+'*')

        turns += 1
        print('Player 2 has: '+ str(pointsP2) + ' points so far')
        num2 = 0 # resetting counter for the two turns of player two
        cards_chosen.pop() # erasing cards_chosen list so its clear and ready for the next turn
        cards_chosen.pop()

        if position_of_cards.count(str(0)) == len(position_of_cards):
            if pointsP2 > pointsP1:
                print('--------------------------------------------')
                print('PLAYER 2 WON')
                print('--------------------------------------------')
            elif pointsP1 == pointsP2:
                print('--------------------------------------------')
                print('ITS A TIE')
                print('--------------------------------------------')
