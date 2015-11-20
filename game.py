
from instructions import *
from player import *
from boss import *
from gameplay import *

class Game(object):

    def __init__(self):
        self.player = Player()
        self.boss = Boss()
        self.gameplay = Gameplay()

    def begin_game(self):
        begin_game(self)

    def situation(self, player_name, player_hp, player_weapon, boss_name, boss_hp):
        situation(self, player_name, player_hp, player_weapon, boss_name, boss_hp)

game = Game()

game.begin_game()
game.player.stats()
game.boss.stats(game.player.weapon)
game.situation(game.player.name, game.player.hp, game.player.weapon, game.boss.name, game.boss.hp)
game.gameplay.battle(game.player.hp, game.player.weapon, game.boss.hp)
