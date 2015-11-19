
class Boss(object):

    def __init__(self):
        self.name = ""
        self.hp = ""


    def stats(self, player_weapon):

        boss_stats = {
            'sword': 300,
            'magic': 200,
            'fist': 1000
        }

        self.name = input("\n\tName a friend. He/She will join you on your quest. > ").title()
        self.hp = boss_stats[player_weapon]
        
