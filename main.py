
# global positions = initalPositions()

# def initalPositions():
#     positions = {
#         "white": [],
#         "black": []
#     }
#     positions["white"] = [[0,i] for i in range(8)] + [[1,i] for i in range(8)]
#     positions["black"] = [[7,i] for i in range(8)] + [[6,i] for i in range(8)]
#     return positions

# ids = ["rook"
# "knight",
# "bishop",
# "queen",
# "king",
# "bishop",
# "knight",
# "rook",
# "pawn",
# "pawn",
# "pawn",
# "pawn",
# "pawn",
# "pawn",
# "pawn",
# "pawn"]

# 012334567
# 9 10 11 12 1


# bottomLeft 0,0 

directions = {
    "up": 1,
    "down": 2,
    "left": 3,
    "right": 4,
    "upRight": 5,
    "downRight": 6,
    "downLeft": 7,
    "upLeft": 8
}
"♔ ♕ ♗ ♘ ♟ ♖  ♚ ♛ ♝ ♞ ♙ ♜"
coraspond = {'Bking': ' ♔ ', 'Bqueen': ' ♕ ', 'Bbishop': ' ♗ ', 'Bknight': ' ♘ ', 'Bpawn': '♟', 'Brook': ' ♖ ', 'Wking': ' ♚ ', 'Wqueen': ' ♛ ', 'Wbishop': ' ♝ ', 'Wknight': ' ♞ ', 'Wpawn': ' ♙ ', 'Wrook': ' ♜ '}

"""
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
"""
"""
:white_large_square: :black_large_square: :white_large_square: :black_large_square: :white_large_square: :black_large_square: :white_large_square: :black_large_square: 
:black_large_square: :white_large_square: :black_large_square: :white_large_square: :black_large_square: :white_large_square: :black_large_square: :white_large_square: 
:white_large_square: :black_large_square: :white_large_square: :black_large_square: :white_large_square:  ♜  :white_large_square: :black_large_square: 
:black_large_square: :white_large_square: :black_large_square: :white_large_square: :black_large_square: :white_large_square: :black_large_square: :white_large_square: 
♜   ♞   ♝   ♛  ♚      ♝   ♞     ♜
"""
board = [   
            ["Brook", "Bknight", "Bbishop", "Bqueen", "Bking", "Bbishop", "Bknight", "Brook"],
            ["Bpawn", "Bpawn", "Bpawn", "Bpawn", "Bpawn", "Bpawn", "Bpawn", "Bpawn"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["Wpawn", "Wpawn", "Wpawn", "Wpawn", "Wpawn", "Wpawn", "Wpawn", "Wpawn"],
            ["Wrook", "Wknight", "Wbishop", "Wqueen", "Wking", "Wbishop", "Wknight", "Wrook"]
]

def printBoard():
    x = True
    bordFin = ""
    for i in range(8):
        for j in range(8):
            if( board[i][j] == "" ):
                if(x):
                    bordFin+=":white_large_square: "
                else:
                    bordFin+=":black_large_square: "
            else:
                bordFin+= coraspond[board[i][j]] + " "
            x = not x
        bordFin+="\n"
        x = not x
    return bordFin

def databaseMove(fromCord, toCord):
    temp=""
    if(piece(fromCord)==""):
        return False
    print(eval(piece(fromCord)[1:]+"(toCord)"))
    print(toCord in eval(piece(fromCord)[1:]+"(toCord)"))
    if(toCord in eval(piece(fromCord)[1:]+"(toCord)")):
        temp=board[toCord[0]][toCord[1]]
        board[toCord[0]][toCord[1]]=piece(fromCord)
        return temp
    return False
    
"""
return "B" or "W"
"""
def piece(cord):return(board[cord[0]][cord[1]])

def side(piece):
    return piece[0]
    

def inBord(cord):
    for i in cord:
        if(i < 0 or i > 7): return False
    return True

def smallerOne(num1, num2):
    return num2 if num1 > num2 else num1

# bottomLeft 0,0 
"""
"""
def seekPossible(direction, cord):
    fin = []
    if(direction == 1):            # up
        for i in range(1, 7 - cord[1] + 1):
            newCord = [cord[0], cord[1] + i]
            if(board[newCord[0], newCord[1]] != ""):
                if sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 2):       # down
        for i in range(1, cord[1] + 1):
            newCord = [cord[0], cord[1] - i]
            if(board[newCord[0], newCord[1]] != ""):
                if sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 3):       # left
        for i in range(1, cord[0] + 1):
            newCord = [cord[0] - i, cord[1]]
            if(board[newCord[0], newCord[1]] != ""):
                if sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 4):       # right
        for i in range(1, 7 - cord[0] + 1):
            newCord = [cord[0] + i, cord[1]]
            if(board[newCord[0], newCord[1]] != ""):
                if sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 5):       # upRight
        numOfIterations = smallerOne((7 - cord[0]), (7 - cord[1]))
        for i in range(1, numOfIterations + 1): # add one because starts at one
            newCord = [cord[0] + i, cord[1] + i]
            if(board[newCord[0], newCord[1]] != ""):
                if sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 6):       # downRight
        numOfIterations = smallerOne(cord[0], 7 - cord[1])
        for i in range(1, numOfIterations + 1): # add one because starts at one
            newCord = [cord[0] - i, cord[1] + i]
            if(board[newCord[0], newCord[1]] != ""):
                if sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 7):       # downLeft
        numOfIterations = samllerOne(cord[0], cord[1])
        for i in range(1, numOfIterations + 1): # add one because starts at one
            newCord = [cord[0] - i, cord[1] - i]
            if(board[newCord[0], newCord[1]] != ""):
                if sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    elif(direction == 8):       # upLeft
        numOfIterations = samllerOne(cord[0], 7 - cord[1])
        for i in range(1, numOfIterations + 1): # add one because starts at one
            newCord = [cord[0] + i, cord[1] - i]
            if(board[newCord[0], newCord[1]] != ""):
                if sameSide(cord, newCord): fin.append(newCord)
                break
            fin.append(newCord)
    
    return fin

# return -1: same position || -2: not within the 8 directions
# def findDirection(fromPos, toPos):
#     if fromPos[0] == toPos[0] and fromPos[1] == toPos[1]:
#         return -1

#     if fromPos[0] == toPos[0] and fromPos[1] != toPos[1]:
#         if fromPos[1] < toPos[1]:
#             return directions["up"]
#         else return directions["down"]
#     else if fromPos[0] != toPos[0] and fromPos[1] == toPos[1]:
#         if fromPos[0] < toPos[0]:
#             return directions["right"]
#         else return directions["left"]
#     else:
#         #diagonals
#         fromPos[0] - toPos[1] == fromPos[1] - toPos[]
        

# return possible cords


# global directions = {
#     "up": 1,
#     "down": 2,
#     "left": 3,
#     "right": 4,
#     "upRight": 5,
#     "downRight": 6,
#     "downLeft": 7,
#     "upLeft": 8
# }

def joinArrays(arr1, arr2):
    return [*arr1, *arr2]

def rook(cord):
    fin = []
    fin.extend(seekPossible(directions["up"], cord))
    fin.extend(seekPossible(directions["down"], cord))
    fin.extend(seekPossible(directions["left"], cord))
    fin.extend(seekPossible(directions["right"], cord))
    return fin

def bishop(cord):
    fin = []
    fin.extend(seekPossible(directions["upRight"], cord))
    fin.extend(seekPossible(directions["downRight"], cord))
    fin.extend(seekPossible(directions["downLeft"], cord))
    fin.extend(seekPossible(directions["upLeft"], cord))
    return fin

def queen(cord):
    fin = []
    fin.extend(seekPossible(directions["up"], cord))
    fin.extend(seekPossible(directions["down"], cord))
    fin.extend(seekPossible(directions["left"], cord))
    fin.extend(seekPossible(directions["right"], cord))
    fin.extend(seekPossible(directions["upRight"], cord))
    fin.extend(seekPossible(directions["downRight"], cord))
    fin.extend(seekPossible(directions["downLeft"], cord))
    fin.extend(seekPossible(directions["upLeft"], cord))
    pass

def pawn(cord):
    positionsPosible = []
    if(side(cord)=="W"):
        x = movePos(cord, [1, 1])
        if(possibleMove(cord, x)):
            positionsPosible.append(x)
        x = movePos(cord, [1, -1])
        if(possibleMove(cord, x)):
            positionsPosible.append(x)
    if(side(cord)=="B"):
        x = movePos(cord, [-1, 1])
        if(possibleMove(cord, x)):
            positionsPosible.append(x)
        x = movePos(cord, [-1, -1])
        if(possibleMove(cord, x)):
            positionsPosible.append(x)
    return positionsPosible

def movePos(cord, move):
    move[0] + cord[0], move[1] + cord[1]


def possibleMove(cord, move):
    return(inBord(move) and not sameSide(cord, move))

def sameSide(one, two):
    return side(board[one[0]],[one[1]]) == side(board[two[0]],[two[1]])


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

def king(cord):
    pass

def queen():
    pass



#def ifAlreadyHave



#def start():
    
print(piece([6,6]))
print(printBoard())
print(databaseMove([6,6],[6,6]))
print(printBoard())

#print(board)

"""
discordId="833059436192989214"

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('play chest'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
"""