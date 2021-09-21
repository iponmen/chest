import glb
from imports import general
from imports import pieces

def reset():
    glb.board = glb.boardInitState
    glb.sideturn = "W"
    glb.castleRights = {
        "W": True,
        "B": True
    }

# can add timer    
def start():
    print("game starte")
    reset()

# check for winning conditions and stuff everytime anything updates
def tick():
    returnStack = {"id": 0, "description": "default - means nothing happened"}
    if not any("Bking" in x for x in glb.board):
        returnStack = {"id": 10, "description": "white wins"}
        # white wins
    if not any("Wking" in x for x in glb.board):
        returnStack = {"id": 11, "description": "black wins"}

    # think of anything missing need to do

    return returnStack

def move(movString):
    cords = movString.split(" ")
    move(cords[0], cords[1])

# can upgrade to return error codes
def move(fromCord, toCord):
    if not (glb.board_get(fromCord) != "" 
            and pieces.inBord(fromCord) 
            and pieces.inBord(toCord)):
        return False

    #if it is white/blacks turn
    side = pieces.side(glb.board_get(fromCord))
    if side != glb.sideturn:
        return False
    
    focusPiece = glb.board_get(fromCord)
    #checks for if invalid 
    if (glb.board_get(fromCord)=="" 
            or fromCord==toCord 
            or focusPiece[1:] not in glb.possiblePieces):
        return False

    print(fromCord, toCord)

    #check for legal
    if not ifLegal(focusPiece, fromCord, toCord):
        # check for castle
        if focusPiece[1:] == "king":
            legalornot = ifCastleLegalPlusKnightMove(fromCord, toCord);
            if not legalornot: return False
        else:
            return False
    
    if focusPiece[1:] == "king": #not a word, don't you dare
        glb.castleRights[pieces.side(glb.board_get(fromCord))] = False

    databaseMove(fromCord, toCord)

    # if glb.sideturn == "W":
    #     glb.sideturn = "B"
    # else: glb.sideturn = "W"

    # TODO:keep stat of what pieces loss and stuff
    return True

def ifLegal(piece, fromCord, toCord):
    pieceType = piece[1:]
    legalMoves = []
    if pieceType == "rook":
        legalMoves.extend(pieces.rook(fromCord))
    elif pieceType == "knight":
        legalMoves.extend(pieces.knight(fromCord))
    elif pieceType == "bishop":
        legalMoves.extend(pieces.bishop(fromCord))
    elif pieceType == "queen":
        legalMoves.extend(pieces.queen(fromCord))
    elif pieceType == "king":
        legalMoves.extend(pieces.king(fromCord))
    elif pieceType == "pawn":
        legalMoves.extend(pieces.pawn(fromCord))

    if toCord in legalMoves:
        return True
    else: return False

# , and if you dare critisize what's below...
def ifCastleLegalPlusKnightMove(fromCord, toCord):
    print( glb.castleRights["W"])
    if glb.board_get(fromCord)[0] == "W" and glb.castleRights["W"] == True:
        if toCord[0]-fromCord[0] == 0 and toCord[1]-fromCord[1] == 2:
            if (glb.board_get([7,4]) == "Wking"
                and glb.board_get([7,5]) == ""
                and glb.board_get([7,6]) == ""
                and glb.board_get([7,7]) == "Wrook"):
                    databaseMove([7,7], [7,5])
            else: return False
        if toCord[0]-fromCord[0] == 0 and toCord[1]-fromCord[1] == -2:
            if (glb.board_get([7,4]) == "Wking"
                and glb.board_get([7,3]) == ""
                and glb.board_get([7,2]) == ""
                and glb.board_get([7,1]) == ""
                and glb.board_get([7,0]) == "Wrook"):
                    databaseMove([7,0], [7,3])
            else: return False
    elif pieces.side(glb.board_get(fromCord)) == "B" and glb.castleRights["B"] == True:
        if toCord[0]-fromCord[0] == 0 and toCord[1]-fromCord[1] == 2:
            if (glb.board_get([0,4]) == "Bking"
                and glb.board_get([0,5]) == ""
                and glb.board_get([0,6]) == ""
                and glb.board_get([0,7]) == "Wrook"):
                    databaseMove([0,7], [0,5])
            else: return False
        if toCord[0]-fromCord[0] == 0 and toCord[1]-fromCord[1] == -2:
            if (glb.board_get([0,4]) == "Bking"
                and glb.board_get([0,3]) == ""
                and glb.board_get([0,2]) == ""
                and glb.board_get([0,1]) == ""
                and glb.board_get([0,0]) == "Wrook"):
                    databaseMove([0,0], [0,3])
            else: return False
    else: return False
    return True
    

def databaseMove(fromCord, toCord):    
    glb.board[toCord[0]][toCord[1]]=glb.board_get(fromCord)
    glb.board[fromCord[0]][fromCord[1]]=""
    return True
    
def convertCord(fromCord, toCord):
    return [[8-int(fromCord[1]), ord(fromCord[0])-97],[8-int(toCord[1]), ord(toCord[0])-97]]
