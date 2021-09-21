import pprint
pp = pprint.PrettyPrinter(indent=4)

from imports import pieces
from imports import general
from imports import game
import glb

# print(general.cord("h2"));
# pp.pprint(pieces.seekPossible(glb.directions["left"], general.cord("c5")))


print(game.move(general.cord("e1"), general.cord("g1")))
print(general.consolePrintBoard())