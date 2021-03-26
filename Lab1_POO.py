# This is the first Lab of Object Oriented Programming
# Monday March 22nd

import numpy as np
from numpy import *
import math

def matrix (cards):
    matrixlist=[]
    tuple1=()
    list1=[]
    list1=tuple(tuple1)

    if cards < 10:
        rows = 1
        cols = cards
        print(rows,cols)
    elif cards >= 10:
        rows = float(cards)/float(10)
        print (rows) 
        rowss = math.ceil(rows)
        #print(rowss)
        #leftover = cards - rows*10 
        #cols = leftover 
        cols=10
        print(rowss,cols)

    #rows = cards
    #cols = cards
    rows=int(rows)
    rowss=int(rowss)
    cards=int(cards)
    cols=int(cols)
    print(rows,rowss,cards,cols)

    a = np.zeros((rowss*cols))
    for i in range(rowss):
        list1=[]
        list1.append(i)
        t1=tuple(list1)
        for j in range(cols):
            list1=list(t1)
            list1.append(j)
            t2=tuple(list1)
            matrixlist.append(t2)
            list1.remove(list1[0])
    data=[]
    data= matrixlist
    i=0
    #print(matrixlist)

    m=[data[i:i+cols] for i in range(0, len(data), cols)]
    #print(m)
    for i in m:
        print(i)

    return m

#def user_input():
    
cards = int(input('How many cards will the players have?  '))
#P1_name = input('What is the name of the first player?')
#P2_name = input('What is the name of the second player?')
P1_points = 0
P2_points = 0
PointsP1 = 0
PointsP2 = 0
Turns = 0
#return cards, P1_name, P2_name

#def game_setup(cards):
cards_P1 = range(cards)
cards_P2 = range(cards)

random.shuffle(cards_P1)
random.shuffle(cards_P2)

print (cards_P1)
print (cards_P2)
#    return cards_P1, cards_P2

#user_input()
#game_setup(user_input[0])

mP1 = matrix(len(cards_P1))
mP2 = matrix(len(cards_P2))
dummy_number=0

while PointsP1 < cards/2 or PointsP2 < cards/2:

    if Turns % 2 == 0:
        print(Turns)
        x = input('Enter x coordinate:')
        y = input('Enter y coordinate:')

        mP1[x].insert(mP1[x].index((x, y)), cards_P1.pop(cards_P1[dummy_number]) )
        mP1[x].pop(mP1[x].index((x, y)))
        
        for i in mP1:
            print(i)

        

        PointsP1 +=1
        dummy_number +=1
        
        

    #else:
        #x = input('Enter x coordinate:')
        #y = input('Enter y coordinate:')
    

        #PointsP2 +=1


    



