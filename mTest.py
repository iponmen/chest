text = ["Bking", "Bqueen", "Bbishop", "Bknight", "Bpawn", "Brook", "Wking", "Wqueen", "Wbishop", "Wknight", "Wpawn", "Wrook"]
emoji = ["♔", "♕", "♗", "♘", "♟", "♖", "♚", "♛", "♝", "♞", "♙", "♜"]

dic = {}
for i in range(len(text)):
    dic[text[i]] = emoji[i]
print (dic)