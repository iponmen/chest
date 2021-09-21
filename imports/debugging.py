import glb

def locatePiece(nameOfPiece):
    f=[]
    for i in range(len(glb.board)):
        for j in range(len(glb.board[0])):
            if glb.board[i][j] == nameOfPiece:
                f.append((i,j))
    return tuple(f)