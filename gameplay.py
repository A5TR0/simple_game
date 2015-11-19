
class Gameplay(object):

    def battle(self, player_hp, player_weapon, boss_hp):

        damage_output = {
            'ATTACK': int(player_hp/10)
        }

        defend_output = {
            'DEFEND': int(player_hp/5)
        }

        boss_output = {
            'BOSS': int(boss_hp/50)
        }


        while player_hp and boss_hp > 0:

            action = input("\n\tAttack or Defend. > ").upper()

            if action in damage_output:
                boss_hp = boss_hp - damage_output[action]
                print("\n\tYou dealt {} damage.".format(damage_output[action]))

            elif action in defend_output:
                player_hp = player_hp + defend_output[action]
                print("\n\tYou gained {} HP.".format(defend_output[action]))

            else:
                player_hp = player_hp - boss_output['BOSS']
                print("\n\tYou typed incorrectly. You made no action and the boss smacks you for an additional {} damage.".format(boss_output['BOSS']))

            player_hp = player_hp - boss_output['BOSS']
            print("\tThe boss dealt you {} damage.".format(boss_output['BOSS']))
            print("\tYou have {} HP. The boss has {} HP.".format(player_hp, boss_hp))

        if player_hp < 1:
            print("\n\tYou lose.\n")

        elif boss_hp <1 :
            print("\n\tYou win!\n")
