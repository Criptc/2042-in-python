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

def Add():
    global Board
    Done = False
    while not Done:
        x = RandomFourxFour()
        y = RandomFourxFour()
        if Board[x][y] == 0:
            if random(1, 11) == 5:
                Board[x][y] = 4
                Done = True
            else:
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
    for i in range(4):
        i = i + 1
        
        #Combine
        
        if Board[3][i] != 0:
            if Board[4][i] == Board[3][i]:
                Board[3][i] = Board[3][i] + Board[4][i]
        
        if Board[2][i] != 0:
            if Board[3][i] == Board[2][i]:
                Board[2][i] = Board[3][i] + Board[2][i]
                Board[3][i] = 0
            elif Board[4][i] == Board[2][i]:
                if Board[3][i] == 0:
                    Board[2][i] = Board[2][i] + Board[4][i]
                    Board[4][i] = 0
        
        if Board[1][i] != 0:
            if Board[2][i] == Board[1][i]:
                Board[1][i] = Board[2][i] + Board[1][i]
                Board[2][i] = 0
            elif Board[3][i] == Board[1][i]:
                if Board[2][i] == 0:
                    Board[1][i] = Board[3][i] + Board[1][i]
                    Board[3][i] = 0
            elif Board[4][i] == Board[1][i]:
                if Board[3][i] == 0:
                    if Board[2][i] == 0:
                        Board[1][i] = Board[4][i] + Board[1][i]
                        Board[4][i] = 0
            
        #move
            
        if Board[1][i] == 0:
            if Board[2][i] != 0:
                Board[1][i] = Board[2][i]
                Board[2][i] = 0
        if Board[2][i] == 0:
            if Board[1][i] == 0:
                if Board[3][i] != 0:
                    Board[1][i] = Board[3][i]
                    Board[3][i] = 0
            else:
                if Board[2][i] == 0:
                    if Board[3][i] != 0:
                        Board[2][i] = Board[3][i]
                        Board[3][i] = 0
        if Board[3][i] == 0:
            if Board[2][i] == 0:
                if Board[1][i] == 0:
                    Board[1][i] = Board[4][i]
                    Board[4][i] = 0
                else:
                    Board[2][i] = Board[4][i]
                    Board[4][i] = 0
            else:
                Board[3][i] = Board[4][i]
                Board[4][i] = 0

def Movedown():
    global Board
    for i in range(4):
        i = i + 1
        
        #Combine
        
        if Board[3][i] != 0:
            if Board[1][i] == Board[2][i]:
                Board[2][i] = Board[2][i] + Board[1][i]
        
        if Board[3][i] != 0:
            if Board[2][i] == Board[3][i]:
                Board[3][i] = Board[2][i] + Board[3][i]
                Board[2][i] = 0
            elif Board[1][i] == Board[3][i]:
                if Board[2][i] == 0:
                    Board[3][i] = Board[3][i] + Board[1][i]
                    Board[1][i] = 0
        
        if Board[4][i] != 0:
            if Board[3][i] == Board[4][i]:
                Board[4][i] = Board[3][i] + Board[4][i]
                Board[3][i] = 0
            elif Board[2][i] == Board[4][i]:
                if Board[3][i] == 0:
                    Board[4][i] = Board[2][i] + Board[4][i]
                    Board[2][i] = 0
            elif Board[1][i] == Board[4][i]:
                if Board[2][i] == 0:
                    if Board[3][i] == 0:
                        Board[4][i] = Board[1][i] + Board[4][i]
                        Board[1][i] = 0
            
        #move
            
        if Board[4][i] == 0:
            if Board[3][i] != 0:
                Board[4][i] = Board[3][i]
                Board[3][i] = 0
        if Board[3][i] == 0:
            if Board[4][i] == 0:
                if Board[2][i] != 0:
                    Board[4][i] = Board[2][i]
                    Board[2][i] = 0
            else:
                if Board[3][i] == 0:
                    if Board[2][i] != 0:
                        Board[3][i] = Board[2][i]
                        Board[2][i] = 0
        if Board[2][i] == 0:
            if Board[3][i] == 0:
                if Board[4][i] == 0:
                    Board[4][i] = Board[1][i]
                    Board[1][i] = 0
                else:
                    Board[3][i] = Board[1][i]
                    Board[1][i] = 0
            else:
                Board[2][i] = Board[1][i]
                Board[1][i] = 0

def MoveRight():
    global Board
    for i in range(4):
        i = i + 1
        
        #Combine
        
        if Board[i][3] != 0:
            if Board[i][1] == Board[i][2]:
                Board[i][2] = Board[i][2] + Board[i][1]
        
        if Board[i][3] != 0:
            if Board[i][2] == Board[i][3]:
                Board[i][3] = Board[i][2] + Board[i][3]
                Board[i][2] = 0
            elif Board[i][1] == Board[i][3]:
                if Board[i][2] == 0:
                    Board[i][3] = Board[i][3] + Board[i][1]
                    Board[i][1] = 0
        
        if Board[i][4] != 0:
            if Board[i][3] == Board[i][4]:
                Board[i][4] = Board[i][3] + Board[i][4]
                Board[i][3] = 0
            elif Board[i][2] == Board[i][4]:
                if Board[i][3] == 0:
                    Board[i][4] = Board[i][2] + Board[i][4]
                    Board[i][2] = 0
            elif Board[i][1] == Board[i][4]:
                if Board[i][2] == 0:
                    if Board[i][3] == 0:
                        Board[i][4] = Board[i][1] + Board[i][4]
                        Board[i][1] = 0
            
        #move
            
        if Board[i][4] == 0:
            if Board[i][3] != 0:
                Board[i][4] = Board[i][3]
                Board[i][3] = 0
        if Board[i][3] == 0:
            if Board[i][4] == 0:
                if Board[i][2] != 0:
                    Board[i][4] = Board[i][2]
                    Board[i][2] = 0
            else:
                if Board[i][3] == 0:
                    if Board[i][2] != 0:
                        Board[i][3] = Board[i][2]
                        Board[i][2] = 0
        if Board[i][2] == 0:
            if Board[i][3] == 0:
                if Board[i][4] == 0:
                    Board[i][4] = Board[i][1]
                    Board[i][1] = 0
                else:
                    Board[i][3] = Board[i][1]
                    Board[i][1] = 0
            else:
                Board[i][2] = Board[i][1]
                Board[i][1] = 0

def MoveLeft():
    global Board
    for i in range(4):
        i = i + 1
        
        #Combine
        
        if Board[i][3] != 0:
            if Board[i][4] == Board[i][3]:
                Board[i][3] = Board[i][3] + Board[i][4]
        
        if Board[i][2] != 0:
            if Board[i][3] == Board[i][2]:
                Board[i][2] = Board[i][3] + Board[i][2]
                Board[i][3] = 0
            elif Board[i][4] == Board[i][2]:
                if Board[i][3] == 0:
                    Board[i][2] = Board[i][2] + Board[i][4]
                    Board[i][4] = 0
        
        if Board[i][1] != 0:
            if Board[i][2] == Board[i][1]:
                Board[i][1] = Board[i][2] + Board[i][1]
                Board[i][2] = 0
            elif Board[i][3] == Board[i][1]:
                if Board[i][2] == 0:
                    Board[i][1] = Board[i][3] + Board[i][1]
                    Board[i][3] = 0
            elif Board[i][4] == Board[i][1]:
                if Board[i][3] == 0:
                    if Board[i][2] == 0:
                        Board[i][1] = Board[i][4] + Board[i][1]
                        Board[i][4] = 0
            
        #move
            
        if Board[i][1] == 0:
            if Board[i][2] != 0:
                Board[i][1] = Board[i][2]
                Board[i][2] = 0
        if Board[i][2] == 0:
            if Board[i][1] == 0:
                if Board[i][3] != 0:
                    Board[i][1] = Board[i][3]
                    Board[i][3] = 0
            else:
                if Board[i][2] == 0:
                    if Board[i][3] != 0:
                        Board[i][2] = Board[i][3]
                        Board[i][3] = 0
        if Board[i][3] == 0:
            if Board[i][2] == 0:
                if Board[i][1] == 0:
                    Board[i][1] = Board[i][4]
                    Board[i][4] = 0
                else:
                    Board[i][2] = Board[i][4]
                    Board[i][4] = 0
            else:
                Board[i][3] = Board[i][4]
                Board[i][4] = 0


Add()
Add()

while True:
    print('\n\n\n\n\n\n\n\n')
    DisplayBoard()
    inp = input('l, r, u, d: ')
    inp = inp.lower()
    if inp == 'l':
        MoveLeft()
    elif inp == 'r':
        MoveRight()
    elif inp == 'u':
        MoveUp()
    elif inp == 'd':
        Movedown()
    else:
        exit(1)
    Add()



