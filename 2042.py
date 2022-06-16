from random import randint as random, choice
from time import sleep

global Board
Board = [[0 for x in range(5)] for x in range(5)]

'''
Board: y, x, Board

Board Printed:
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
'''

def Random():
    first = True
    RandomNumbers = []
    while True:
        if not first:
            if random(0, 4) == 2:
                break
        RandomNumbers += str(random(1, 10))
        if first:
            first = False
    return int(choice(RandomNumbers))

def RandomFourxFour():
    first = True
    RandomNumbers = []
    while True:
        if not first:
            if random(0, 4) == 2:
                break
        RandomNumbers += str(random(1, 4))
        if first:
            first = False
    return int(choice(RandomNumbers))

def AddTwo():
    global Board
    Done = False
    while not Done:
        x = RandomFourxFour()
        y = RandomFourxFour()
        if Board[x][y] == 0:
            Board[x][y] = 2
            Done = True

def DisplayBoard():
    global Board
    print('\n')
    print(Board[1][1], Board[1][2], Board[1][3], Board[1][4])
    print(Board[2][1], Board[2][2], Board[2][3], Board[2][4])
    print(Board[3][1], Board[3][2], Board[3][3], Board[3][4])
    print(Board[4][1], Board[4][2], Board[4][3], Board[4][4])

def MoveUp():
    global Board
    if Board[3][1] != 0:
        if Board[4][1] == Board[3][1]:
            Board[3][1] = Board[3][1] + Board[4][1]
    
    if Board[2][1] != 0:
        if Board[3][1] == Board[2][1]:
            Board[2][1] = Board[3][1] + Board[2][1]
            Board[3][1] = 0
        elif Board[4][1] == Board[2][1]:
            Board[2][1] == Board[4][1] + Board[2][1]
            Board[4][1] = 0
    
    if Board[1][1] != 0:
        if Board[2][1] == Board[1][1]:
            Board[1][1] = Board[2][1] + Board[1][1]
            Board[2][1] = 0
        elif Board[3][1] == Board[1][1]:
            Board[1][1] = Board[3][1] + Board[1][1]
            Board[3][1] = 0
        elif Board[4][1] == Board[1][1]:
            Board[1][1] = Board[4][1] + Board[1][1]
            Board[4][1] = 0

while True:
    sleep(6)
    AddTwo()
    DisplayBoard()
    MoveUp()
    DisplayBoard()




