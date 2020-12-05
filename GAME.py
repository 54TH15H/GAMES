from sys import exit
from numpy import array

def func(v):

    if v == '#':
        print(' YOU ENTERED IN WRONG POSITION ')
        print(' PLZ RESTART THE GAME ')
        exit(0)

def disparray():

    print('{}  |  {}  |  {}     {}  |  {}  |  {}'.format(a[0][0], a[0][1], a[0][2], v00, v01, v02))
    print('{}  |  {}  |  {}     {}  |  {}  |  {}'.format(a[1][0], a[1][1], a[1][2], v10, v11, v12))
    print('{}  |  {}  |  {}     {}  |  {}  |  {}'.format(a[2][0], a[2][1], a[2][2], v20, v21, v22))

def win(d,p):

    if p == 1:
        if d == 'X':
            print(' PLAYER 1 WINS ')
        else:
            print(' PLAYER 2 WINS ')
    else:
        if d == 'O':
            print(' PLAYER 1 WINS ')
        else:
            print(' PLAYER 2 WINS ')


print(' A SIMPLE GAME USING PYTHON \n\n')
flag = True
winStatus = False
v00, v01, v02, v10, v11, v12, v20, v21, v22 = 1, 2, 3, 4, 5, 6, 7, 8, 9

a = array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

disparray()

print('\n')
y = ''
print(' SYMBOLS : X AND O ')
p = int(input(' PLAYER 1 : PLZ SELECT YOUR SYMBOL \n PRESS 1 TO SELECT SYMBOL X \n PRESS 0 TO SELECT SYMBOL O \n'))

if p == 1:
    x, y = 'X', 'O'
elif p == 0:
    x, y= 'O', 'X'
else:
    print(' INVALID CHOICE,GAME OVER ')
    exit(0)

print(' SYMBOL FOR PLAYER 1 :  ', x)
print(' SYMBOL FOR PLAYER 2 :  ', y)

print('\n')
disparray()
print(' \n ENTER CORRESPONDING VALUES TO PLACE YOUR SYMBOL AT CORRESPONDING POSITION ')

i = 1
j = 1
while flag:
    c = int(input(' PLAYER {} - ENTER YOUR CHOICE : '.format(i)))
    if c == 1:
        func(v00)
        if i == 1:
            a[0][0], v00 = x, '#'
        else:
            a[0][0], v00 = y, '#'

    elif c == 2:
        func(v01)
        if i == 1:
            a[0][1], v01 = x, '#'
        else:
            a[0][1], v01 = y, '#'

    elif c == 3:
        func(v02)
        if i == 1:
            a[0][2], v02 = x, '#'
        else:
            a[0][2], v02 = y, '#'

    elif c == 4:
        func(v10)
        if i == 1:
            a[1][0], v10 = x, '#'
        else:
            a[1][0], v10 = y, '#'

    elif c == 5:
        func(v11)
        if i == 1:
            a[1][1], v11 = x, '#'
        else:
            a[1][1], v11 = y, '#'

    elif c == 6:
        func(v12)
        if i == 1:
            a[1][2], v12 = x, '#'
        else:
            a[1][2], v12 = y, '#'

    elif c == 7:
        func(v20)
        if i == 1:
            a[2][0], v20 = x, '#'
        else:
            a[2][0], v20 = y, '#'

    elif c == 8:
        func(v21)
        if i == 1:
            a[2][1], v21 = x, '#'
        else:
            a[2][1], v21 = y, '#'

    else:
        func(v22)
        if i == 1:
            a[2][2], v22 = x, '#'
        else:
            a[2][2], v22 = y, '#'

    if i == 1:
        i+=1
    else:
        i-=1

    disparray()
    print('\n')

    j+=1

    if p == 1:
        d = 'X'
        for k in [0,1]:
            if a[0][0] == d and a[0][1] == d and a[0][2] == d:
                flag = False
                winStatus = True
                win('X',1)
                break

            elif a[0][0] == d and a[1][0] == d and a[2][0] == d:
                flag = False
                winStatus = True
                win('X',1)
                break

            elif a[2][0] == d and a[2][1] == d and a[2][2] == d:
                flag = False
                winStatus = True
                win('X',1)
                break

            elif a[0][2] == d and a[1][2] == d and a[2][2] == d:
                flag = False
                winStatus = True
                win('X',1)
                break

            elif a[1][0] == d and a[1][1] == d and a[1][2] == d:
                flag = False
                winStatus = True
                win('X',1)
                break

            elif a[0][1] == d and a[1][1] == d and a[2][1] == d:
                flag = False
                winStatus = True
                win('X',1)
                break

            elif a[0][0] == d and a[1][1] == d and a[2][2] == d:
                flag = False
                winStatus = True
                win('X',1)
                break

            elif a[2][0] == d and a[1][1] == d and a[0][2] == d:
                flag = False
                winStatus = True
                win('X',1)
                break

            else:
                d = 'O'
                continue
    else:
        d = 'O'
        for i in [0, 1]:
            if a[0][0] == d and a[0][1] == d and a[0][2] == d:
                flag = False
                winStatus = True
                win('O',0)
                break

            elif a[0][0] == d and a[1][0] == d and a[2][0] == d:
                flag = False
                winStatus = True
                win('O',0)
                break

            elif a[2][0] == d and a[2][1] == d and a[2][2] == d:
                flag = False
                winStatus = True
                win('O',0)
                break

            elif a[0][2] == d and a[1][2] == d and a[2][2] == d:
                flag = False
                winStatus = True
                win('O',0)
                break

            elif a[1][0] == d and a[1][1] == d and a[1][2] == d:
                flag = False
                winStatus = True
                win('O',0)
                break

            elif a[0][1] == d and a[1][1] == d and a[2][1] == d:
                flag = False
                winStatus = True
                win('O',0)
                break

            elif a[0][0] == d and a[1][1] == d and a[2][2] == d:
                flag = False
                winStatus = True
                win('O',0)
                break

            elif a[2][0] == d and a[1][1] == d and a[0][2] == d:
                flag = False
                winStatus = True
                win('O',0)
                break

            else:
                d = 'X'
                continue

    if j == 10 and (not winStatus):
        print(' TIE ')
        flag = False






