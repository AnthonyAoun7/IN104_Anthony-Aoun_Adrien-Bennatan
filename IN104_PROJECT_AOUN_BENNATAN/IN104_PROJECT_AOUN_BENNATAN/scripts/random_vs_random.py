# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.random_vs_random
import aiarena
from ..randomBrain import RandomBrain

brain1 = RandomBrain()
brain2 = RandomBrain()
timeLimit = 40 # each player will have 10 seconds to play
game = aiarena.Game(aiarena.checkers, brain1, timeLimit, brain2, timeLimit)
game.start()

# TODO: Instantier ICI des IA de type RandomBrain

#for module in [aiarena.abalone, aiarena.chess, aiarena.checkers, aiarena.connect4]:
    
    # TODO: ajouter le code pour lancer une partie et afficher son déroulement
    # afficher le PGN en fin de partie
print(game.pgn)
input('press enter to continue')

