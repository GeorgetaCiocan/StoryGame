import copy
from story.fighters import Fighter, Orderus, Beast

class Game():
    number_turns = 0
    def __init__(self):
        self.orderus = Orderus(
            {'health': [70, 100],
             'strength': [70, 80],
             'defence': [45, 55],
             'speed': [40, 50],
             'luck': [10, 30]
             })
        self.beast = Beast(
            {'health': [60, 90],
             'strength': [60, 90],
             'defence': [40, 60],
             'speed': [40, 60],
             'luck': [25, 40]
             })
        self.onebattle = Battle(self.orderus, self.beast)

    def start_war(self):
        self.number_turns = 0
        self.onebattle.get_first_striker()

        self.show_header()

        while True:
            self.onebattle.battle_flow()
            self.number_turns = self.onebattle.number_turns
            self.show_fight_results()
            self.onebattle.get_winner()
            self.onebattle.switch_place()

            if self.onebattle.stop_battle():
                break

        self.show_footer()



    def show_end_score(self,winner):
        if winner == '':
            print("Last Turn {}".format(self.number_turns))
        else:
            print("Last Turn: {}\nWINNER: {}".format(self.number_turns,winner.name))

    def show_header(self):
        print("\n",'=' * 35, "Fight Results", "=" * 40,"\n")
        print("Orderus [health:{}, stength:{}, defence:{}, speed:{}, luck:{}%]"
              .format(self.orderus.health,
                      self.orderus.strength,
                      self.orderus.defence,
                      self.orderus.speed,
                      self.orderus.luck
                      ))
        print("Beast   [health:{}, stength:{}, defence:{}, speed:{}, luck:{}%]"
              .format(self.beast.health,
                      self.beast.strength,
                      self.beast.defence,
                      self.beast.speed,
                      self.beast.luck
                      ))

        print("\nNo| Attacker| Defender| Rapid Strike | Magic Shield | Has Luck | Damage | Defender Health |")
        print('-' * 91)

    def show_footer(self):
        print('=' * 91)
        self.show_end_score(self.onebattle.winner)

    def show_fight_results(self):

        print("{:2d}| {:7s} | {:7s} |{:14s}|{:14s}|{:10s}|{:8s}|{:17s}|"
              .format(self.number_turns,
                      self.onebattle.striker.name,
                      self.onebattle.defender.name,
                      str(self.onebattle.striker.has_rapid_strike()).center(14) if self.onebattle.striker.name == "Orderus" else "-".center(14),
                      str(self.onebattle.defender.has_magic_shield()).center(14) if self.onebattle.defender.name == "Orderus" else "-".center(14),
                      str(self.onebattle.defender.has_luck(self.number_turns)).center(10),
                      str(int(self.onebattle.damage)).center(8),
                      str(int(self.onebattle.defender.health)).center(17)
                      )
              )



class Battle(Game):
    damage = 0
    def __init__(self, striker, defender):
        self.number_turns = super().number_turns
        self.striker = striker
        self.defender = defender
        self.get_rand_prop()
        self.get_first_striker()
        self.winner = self.striker

    def battle_flow(self):
        self.count_turns()
        self.fight()

    def count_turns(self):
        self.number_turns = self.number_turns + 1

    def get_first_striker(self):
        if self.striker.speed == self.defender.speed:
            if self.striker.luck < self.defender.luck:
                self.switch_place()
        elif self.striker.speed < self.defender.speed:
            self.switch_place()

    def get_points_orderus(self):
        if self.striker.name == "Orderus":
            self.striker.number_attack = self.striker.number_attack + 1
        else:
            self.defender.number_defend = self.defender.number_defend + 1

    def fight(self):
        self.get_points_orderus()

        if self.defender.has_luck(self.number_turns):
            self.damage = 0
        else:
            if self.striker.name == "Orderus":
                if self.striker.has_rapid_strike():
                    self.damage = self.get_damage() * 2
                else:
                    self.damage = self.get_damage()
            else:
                if self.defender.has_magic_shield():
                    self.damage = self.get_damage() / 2
                else:
                    self.damage = self.get_damage()

        self.defender.health = self.defender.health - self.damage

    def get_damage(self):
        return self.striker.strength - self.defender.defence

    def get_winner(self):
        if self.defender.health <= 0:
            self.winner = self.striker
        elif self.striker.health <= 0:
            self.winner = self.defender
        else:
            self.winner = ''

    def stop_battle(self):
        if self.winner != '' or self.number_turns == 20:
            return True
        else:
            return False

    def switch_place(self):
        k = copy.deepcopy(self.striker)
        self.striker = copy.deepcopy(self.defender)
        self.defender = copy.deepcopy(k)

    def get_rand_prop(self):
        self.striker.get_rand_prop()
        self.defender.get_rand_prop()
