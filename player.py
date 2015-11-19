
class Player(object):

    def __init__(self):
        self.name = ""
        self.weapon = ""
        self.hp = ""


    def stats(self):

        player_stats = {
            'sword': 150,
            'magic': 100,
            'fist': 1000
        }

        self.name = input("\tChallenger, what is your name? > ").title()

        while self.weapon not in player_stats:
            self.weapon = input("\n\tWeapon? Sword, Magic, Fist. > ").lower()

        self.hp = player_stats[self.weapon]
