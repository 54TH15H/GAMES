
# ROCK PAPER SCISSOR GAME

def checkisdigit(v):
    if v.isdigit():
        return int(v)
    else:
        print(' INVALID ENTRY ')
        exit(0)

print(' ROCK PAPER SCISSOR GAME ')
a = input(' ENTER 1 TO START THE GAME \n ENTER 0 TO EXIT THE GAME \n')
a = checkisdigit(a)
flag = 0
if a == 1:
    flag = True
elif a == 0:
    flag = False
else:
    print(' INVALID CHOICE ')


while flag:

    print(' ENTER ')
    print(' r or R : ROCK \n p or P : PAPER \n s or S : SCISSOR ')
    x = input(' PLAYER 1 : ENTER YOUR CHOICE \n')
    y = input(' PLAYER 2 : ENTER YOUR CHOICE \n')
    x.lower()
    y.lower()

    if x == 'r' or x == 'p' or x == 's' or y == 'r' or y == 'p' or y == 's':

        if x == 'r':
            if y == 's':
                print(' PLAYER 1 WINS ')
            elif y == 'p':
                print(' PLAYER 2 WINS ')
            else:
                print(' TIE ')

        elif x == 'p':
            if y == 's':
                print(' PLAYER 2 WINS ')
            elif y == 'r':
                print(' PLAYER 1 WINS ')
            else:
                print(' TIE ')

        else:
            if y == 'r':
                print(' PLAYER 2 WINS ')
            elif y == 'p':
                print(' PLAYER 1 WINS ')
            else:
                print(' TIE ')

        print(' ENTER 1 TO CONTINUE THE GAME \n ENTER 0 TO STOP THE GAME \n')
        a = int(input())

        if a == 1:
            flag = True
        elif a == 0:
            flag = False
        else:
            print(' INVALID CHOICE \n')
            print(' ENTER 0 OR 1 \n')
            a = int(input())
            if a == 1:
                flag = True
            else:
                flag = False

    else:
        print(' YOU ENTERED WRONG CHOICE ')
        flag = False

else:
    print(' GAME OVER ')
