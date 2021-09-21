"""we know we are the best, thank you"""
# should never question other's methods

# UpperLeft 0,0 
global running
running = True

global clientDup
clientDup = None

global channel1
channel1 = None

global directions
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

global coraspond
coraspond = {'Bking': ' ♔ ', 'Bqueen': ' ♕ ', 'Bbishop': ' ♗ ', 'Bknight': ' ♘ ', 'Bpawn': '♟', 'Brook': ' ♖ ', 'Wking': ' ♚ ', 'Wqueen': ' ♛ ', 'Wbishop': ' ♝ ', 'Wknight': ' ♞ ', 'Wpawn': ' ♙ ', 'Wrook': ' ♜ '}

global possiblePieces
possiblePieces = ["rook",
"knight",
"bishop",
"queen",
"king",
"pawn"]

#shutup, don't you dare critisize
global sideturn
sideturn = "W"
global castleRights
castleRights = {
    "W": True,
    "B": True
}

global board
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

global boardInitState
boardInitState = [   
            ["Brook", "Bknight", "Bbishop", "Bqueen", "Bking", "Bbishop", "Bknight", "Brook"],
            ["Bpawn", "Bpawn", "Bpawn", "Bpawn", "Bpawn", "Bpawn", "Bpawn", "Bpawn"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["Wpawn", "Wpawn", "Wpawn", "Wpawn", "Wpawn", "Wpawn", "Wpawn", "Wpawn"],
            ["Wrook", "Wknight", "Wbishop", "Wqueen", "Wking", "Wbishop", "Wknight", "Wrook"]
]

def board_get(y, x=None):
    global board
    if x == None:
        #y is a cord array [y, x]
        return board[y[0]][y[1]]
    return board[y][x]


