#we are brainless dreamers that types
#i just realized that my stuttering has extended to typing and coding, oh no. one day my actions will also stutter, not that it not is already :o
import glb

def side(piece):
    return piece[0]

def inBord(cord):
    for i in cord:
        if(i < 0 or i > 7): return False
    return True

def smallerOne(num1, num2):
    return num2 if num1 > num2 else num1
    

def possibleMove(cord, move):
    return(inBord(move) and not sameSide(cord, move))

def sameSide(one, two):
    return side([glb.board[one[0]],[one[1]]]) == side([glb.board[two[0]],[two[1]]])

def joinArrays(arr1, arr2):
    return [*arr1, *arr2]

def movePos(cord, move):
    return [move[0] + cord[0], move[1] + cord[1]]

"""
"""
# treat me like a black box, thanks :) //for loops can be changed to while if wanted :)
def seekPossible(direction, cord):
    fin = []
    if(direction == 1):            # up
        for i in range(1, cord[0] + 1):
            newCord = [cord[0] - i, cord[1]]
            if(glb.board_get(newCord[0], newCord[1]) != ""):
                if not sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 2):       # down
        for i in range(1, 7 - cord[0] + 1):
            newCord = [cord[0] + i, cord[1]]
            print(glb.board[newCord[0]][newCord[1]]+"--\n");
            if(glb.board_get(newCord[0], newCord[1]) != ""):
                if not sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 3):       # left
        for i in range(1, cord[1] + 1):
            newCord = [cord[0], cord[1] - i]
            if(glb.board_get(newCord[0], newCord[1]) != ""):
                if not sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 4):       # right
        for i in range(1, 7 - cord[1] + 1):
            newCord = [cord[0], cord[1] + i]
            if(glb.board_get(newCord[0], newCord[1]) != ""):
                if not sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 5):       # upRight
        numOfIterations = smallerOne((cord[0]), (7 - cord[1]))
        for i in range(1, numOfIterations + 1): # add one because starts at one
            newCord = [cord[0] - i, cord[1] + i]
            if(glb.board_get(newCord[0], newCord[1]) != ""):
                if not sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 6):       # downRight
        numOfIterations = smallerOne(7 - cord[0], 7 - cord[1])
        for i in range(1, numOfIterations + 1): # add one because starts at one
            newCord = [cord[0] + i, cord[1] + i]
            if(glb.board_get(newCord[0], newCord[1]) != ""):
                if not sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 7):       # downLeft
        numOfIterations = smallerOne(7 - cord[0], cord[1])
        for i in range(1, numOfIterations + 1): # add one because starts at one
            newCord = [cord[0] + i, cord[1] - i]
            if(glb.board_get(newCord[0], newCord[1]) != ""):
                if not sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 8):       # upLeft
        numOfIterations = smallerOne(cord[0], cord[1])
        for i in range(1, numOfIterations + 1): # add one because starts at one
            newCord = [cord[0] - i, cord[1] - i]
            if(glb.board_get(newCord[0], newCord[1]) != ""):
                if not sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    
    return fin


def rook(cord):
    fin = []
    fin.extend(seekPossible(glb.directions["up"], cord))
    fin.extend(seekPossible(glb.directions["down"], cord))
    fin.extend(seekPossible(glb.directions["left"], cord))
    fin.extend(seekPossible(glb.directions["right"], cord))
    return fin

def bishop(cord):
    fin = []
    fin.extend(seekPossible(glb.directions["upRight"], cord))
    fin.extend(seekPossible(glb.directions["downRight"], cord))
    fin.extend(seekPossible(glb.directions["downLeft"], cord))
    fin.extend(seekPossible(glb.directions["upLeft"], cord))
    return fin

def queen(cord):
    fin = []
    fin.extend(seekPossible(glb.directions["up"], cord))
    fin.extend(seekPossible(glb.directions["down"], cord))
    fin.extend(seekPossible(glb.directions["left"], cord))
    fin.extend(seekPossible(glb.directions["right"], cord))
    fin.extend(seekPossible(glb.directions["upRight"], cord))
    fin.extend(seekPossible(glb.directions["downRight"], cord))
    fin.extend(seekPossible(glb.directions["downLeft"], cord))
    fin.extend(seekPossible(glb.directions["upLeft"], cord))
    return(fin)


#if you tell me to optimise this, im gonna punch you
def pawn(cord):
    positionsPosible = []
    if(side(glb.board_get(cord))=="W"):
        x = movePos(cord, [-1, 1])
        if(possibleMove(cord, x)) and glb.board_get(x) != "":
            positionsPosible.append(x)
            #if 
        x = movePos(cord, [-1, -1])
        if(possibleMove(cord, x)) and glb.board_get(x) != "":
            positionsPosible.append(x)
        x = movePos(cord, [-1, 0])
        print(x)
        if(inBord(x) and glb.board_get(x) == ""):
            positionsPosible.append(x)
    elif(side(glb.board_get(cord))=="B"):
        print("hee")
        x = movePos(cord, [1, 1])
        if(possibleMove(cord, x)) and glb.board_get(x) != "":
            positionsPosible.append(x)
        x = movePos(cord, [1, -1])
        if(possibleMove(cord, x)) and glb.board_get(x) != "":
            positionsPosible.append(x)
        x = movePos(cord, [1, 0])
        if(inBord(x) and glb.board_get(x) == ""):
            positionsPosible.append(x)
    return positionsPosible


def knight(cord):
    fin=[
    movePos( cord, [2, 1]   ),
    movePos( cord, [2, -1]  ),
    movePos( cord, [-2, 1]  ),
    movePos( cord, [-2, -1] ),
    movePos( cord, [1, 2]   ),
    movePos( cord, [1, -2]  ),
    movePos( cord, [-1, 2]  ),
    movePos( cord, [-1, -2] ),
    ]
    fin2=[]
    for i in range(fin):
        if(possibleMove(cord, fin[i])):
            fin2.append(fin[i])
    return fin2
    # return tuple(fin2)

def king(cord):
    fin=[
    movePos( cord, [1, 1]   ),
    movePos( cord, [1, 0]  ),
    movePos( cord, [1, -1]  ),
    movePos( cord, [0, -1] ),
    movePos( cord, [0, 1]   ),
    movePos( cord, [-1, -1]  ),
    movePos( cord, [-1, 0]  ),
    movePos( cord, [-1, 1] ),
    ]
    fin2=[]
    for i in range(len(fin)):
        if(possibleMove(cord, fin[i])):
            fin2.append(fin[i])
    return fin2
    # return tuple(fin2)

def calculate_distance(fromCord, toCord):
    return [toCord[0]-fromCord[0], toCord[1]-fromCord[1]]

"""
0 1
1 1
1 0
1 -1
0 -1
-1 -1
-1 0
-1 1

"""
