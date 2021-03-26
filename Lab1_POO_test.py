from numpy import *
import pandas as pd
from array import *
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
    #for i in m:
    #    print(i)

    return m


def change_matrix ():
#    m = matrix(4)
    #lista1=[]
    #lista2=[]
    x = input('Enter x coordinate:')
    y = input('Enter y coordinate:')
    number=random.randint(1,cards+1)
    list1=range(x)
    list2=range(y)
    random.shuffle(list1)
    random.shuffle(list2)
    print (list1)
    print (list2)
  
#    number=str(' ')+str(number)+str('  ')
    number = list1.insert(x, list)
    m[x][y]=number

    for i in m:
        print(i)

    return m

'''
#def remember_change():

m = matrix(
#change_matrix(matrix(4),0,1)

#def remember_change():

i=0
while i < 5:
    change_matrix()
    i+=1
'''

list1=[[(0, 0),(0, 1),(0, 2),(0, 3)],[(1, 0),(1, 1),(1, 2),(1, 3)]]
list2=[0,1,2,3,4,5,6,7]
dummy_number=1

list2.insert(1,4)
print(list2)

print(list1)
print(list2[1])
position = list1[0].index((0, 1))
#print(list1[0].index((0, 1)))
print(position,'position')
insert_num=list2.pop(list2[1])
print(insert_num,'insert_num')

list1[0].insert(position, insert_num )

print(list1)
print(list2)
