#Code of the program.
from random import randint
field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
randomX = randint (0, 9)
randomY = randint (0, 9)
foxes = 5
for n in range (foxes):
    while (field [randomX][randomY] == 1):
        randomX = randint (0, 9)
        randomY = randint (0, 9)
    field [randomX][randomY] = 1
while (foxes != 0):
    x = input ('x - coordinate:')
    y = input ('y - coordinate:')
    x_int = int (x)
    y_int = int (y)
    x_int -= 1
    y_int -= 1
    see = 0
    if (field [x_int][y_int] == 1):
        print ('FOX!!!')
        foxes -= 1
        continue
    else:
        for i in range (len (field)):
            if field[i][y_int] == 1:
                see += 1
            if (field [x_int][i] == 1):
                see += 1
        while (x_int >= 0 and y_int >= 0):
            if (field [x_int][y_int] == 1):
                see += 1
            x_int -= 1
            y_int -= 1
        x_int += 1
        y_int += 1
        while (x_int <= 9 and y_int <= 9):
            if (field [x_int][y_int] == 1):
                see += 1
                x_int += 1
                y_int += 1
            x_int += 1
            y_int += 1
    print ('See:', end =str (see))
    input ()