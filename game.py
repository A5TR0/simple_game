
from instructions import *
from player import *
from boss import *
from gameplay import *

class Game(object):

    # do i have to init twice? for example, i inited in player and boss
    def __init__(self):
        self.instructions = Instructions()
        self.player = Player()
        self.boss = Boss()
        self.gameplay = Gameplay()


game = Game()

game.instructions.begin_game()
game.player.stats()
game.boss.stats(game.player.weapon)
game.instructions.situation(game.player.name, game.player.hp, game.player.weapon, game.boss.name, game.boss.hp)
game.gameplay.battle(game.player.hp, game.player.weapon, game.boss.hp)
