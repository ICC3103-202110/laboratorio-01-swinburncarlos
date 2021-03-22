from numpy import *
import pandas as pd
#name = input()

#print (name)

cards=10
'''
def game_setup(cards):
    cards_P1 = list(range(cards))
    cards_P2 = list(range(cards))
    random.shuffle(cards_P1)
    random.shuffle(cards_P2)

    return cards_P1, cards_P2

rows=[]
for i in range(10):
    columns=[]
    for j in range(cards):
        columns.append(str(j))
    rows.append(columns)

print(rows)
'''
    
import numpy as np

def matrix (cards):
    matrixlist=[]
    tuple1=()
    list1=[]
    list1=tuple(tuple1)
    rows = cards
    cols = cards

    a = np.zeros((rows*cols))
    for i in range(rows):
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

m = matrix(10)

number=random.randint(10)
number=tuple(number)
m[0][0]=number
for i in m:
    print(i)

#matrixlist = pd.DataFrame(matrixlist)
#print(matrixlist)

#print(game_setup(10))



