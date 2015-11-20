
def begin_game(self):
    print("\n\tWelcome to Friend or Foe. \n\tLet's play.\n")

def situation(self, player_name, player_hp, player_weapon, boss_name, boss_hp):
    print("\n\tJust kidding. \n\t{} fooled ya and now wants to kill you. \n\tKill him or be killed. \n\tChallenger {} [{} HP] w/ {} vs. Traitor {} [{} HP]. \n\tLet's go!".format(boss_name, player_name, player_hp, player_weapon, boss_name, boss_hp))
