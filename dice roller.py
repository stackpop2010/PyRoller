import random

def logicCheck(x, y):
    try:
        x=int(x)
        print('logic check passes, your rolls are:')
        for i in range (x):
            x = random.randint(1,y)
            print(x)
    except:
        print('how many',y,'sided dice would you like to roll?')
        x = input('Please enter an interger number: ')
        logicCheck(x, y)
    

print('Welcome to the dice roller app \n')

fourStrng = ('How many four sided dice would you like to roll?: ')
fourSide = input(fourStrng)
logicCheck(fourSide, 4)

sixStrng = ('How many six sided dice would you like to roll?: ')
sixSide = input(sixStrng)
logicCheck(sixSide, 6)

eightStrng = ('How many eight sided dice would you like to roll?: ')
eightSide = input(eightStrng)
logicCheck(eightSide, 8)

tenStrng = ('How many ten sided dice would you like to roll?: ')
tenSide = input(tenStrng)
logicCheck(tenSide, 10)

twelveStrng = ('How many twelve sided dice would you like to roll?: ')
twelveSide = input(twelveStrng)
logicCheck(twelveSide, 12)

twentyStrng = ('How many twenty sided dice would you like to roll?: ')
twentySide = input(twentyStrng)
logicCheck(twentySide, 20)


print('Thank you for playing! Remember, the real treasure is the friends you make along the way.')

exit()
