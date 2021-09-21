import glb

def printBoard():
    x = True
    bordFin = ""
    for i in range(8):
        bordFin+=str(8-i)+" "
        for j in range(8):
            if( glb.board[i][j] == "" ):
                if(x):
                    bordFin+=":white_large_square: "
                else:
                    bordFin+=":black_large_square: "
            else:
                bordFin+= glb.coraspond[glb.board[i][j]] + " "
            x = not x
        bordFin+="\n"
        x = not x
    bordFin+="      a     b     c     d     e      f      g     h"
    return bordFin

def consolePrintBoard():
    return printBoard().replace(":white_large_square:", "   ").replace(":black_large_square:", " _ ").replace("♟", " ♟️ ")
    
def cord(cordString):
    x = ord(cordString.lower()[0]) - 97
    y = 7 - (int(cordString[1]) - 1)
    return [y, x]