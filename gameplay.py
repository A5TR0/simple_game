
class Gameplay(object):

    def battle(self, player_hp, player_weapon, boss_hp):

        output = {
            'ATTACK': int(player_hp/10),
            'DEFEND': int(player_hp/5),
            'BOSS': int(boss_hp/50)
        }


        while player_hp > 0 and boss_hp > 0:

            action = input("\n\tAttack or Defend. > ").upper()

            if action in output:
                boss_hp = boss_hp - output[action]
                print("\n\tYou dealt {} damage.".format(output[action]))

            elif action in output:
                player_hp = player_hp + output[action]
                print("\n\tYou gained {} HP.".format(output[action]))

            else:
                player_hp = player_hp - output['BOSS']
                print("\n\tYou typed incorrectly. You made no action and the boss smacks you for an additional {} damage.".format(output['BOSS']))

            player_hp = player_hp - output['BOSS']
            print("\tThe boss dealt you {} damage.".format(output['BOSS']))
            print("\tYou have {} HP. The boss has {} HP.".format(player_hp, boss_hp))

        if player_hp < 1:
            print("\n\tYou lose.\n")

        elif boss_hp <1 :
            print("\n\tYou win!\n")
