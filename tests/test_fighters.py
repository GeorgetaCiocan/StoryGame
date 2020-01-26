import unittest

from story.game import Game
from story.fighters import Fighter, Orderus, Beast


class TestFighters(unittest.TestCase):
    game=Game()

    def test_orderus_dranges(self):
        orderus = self.game.orderus
        self.assertEqual(orderus.name,"Orderus")
        self.assertEqual(orderus.dranges['health'],[70,100])
        self.assertEqual(orderus.dranges['strength'], [70, 80])
        self.assertEqual(orderus.dranges['defence'], [45, 55])
        self.assertEqual(orderus.dranges['speed'], [40, 50])
        self.assertEqual(orderus.dranges['luck'], [10, 30])


    def test_orderus(self):
        orderus = self.game.orderus
        self.assertEqual(orderus.name,"Orderus")
        # self.assertTrue(70 <= orderus.health <= 100)
        self.assertTrue(orderus.health in range(70, 100))
        self.assertTrue(orderus.strength in range(70, 80))
        self.assertTrue(orderus.defence in range(45, 55))
        self.assertTrue(orderus.speed in range(40, 50))
        self.assertTrue(orderus.luck in range(10, 30))

        # print(orderus.name)

    def test_beast(self):
        beast = self.game.beast
        self.assertEqual(beast.name,"Beast")
        # self.assertTrue(60 <= beast.health <= 90)
        self.assertTrue(beast.health in range(60, 90))
        self.assertTrue(beast.strength in range(60, 90))
        self.assertTrue(beast.defence in range(40, 60))
        self.assertTrue(beast.speed in range(40, 60))
        self.assertTrue(beast.luck in range(25, 40))
        print(beast.name)

    def test_game_init_class(self):
        self.assertEqual(self.game.orderus.name,"Orderus")
        self.assertTrue(70 <= self.game.orderus.strength <= 80)
        self.assertEqual(self.game.beast.name,"Beast")
        self.assertTrue(25 <= self.game.beast.luck <= 40)
        print(self.game.orderus.name)
        print(self.game.beast.name)
        print(str(self.game.onebattle  ))

    def test_get_first_striker(self):
        self.game.onebattle.get_first_striker()
        print("SPEED Striker [{0:} ? {1:}] Defender\n LUCK Striker [{2:} ? {3:}] Defender".
              format(self.game.onebattle.striker.speed,
                    self.game.onebattle.defender.speed,
                     self.game.onebattle.striker.luck,
                     self.game.onebattle.defender.luck
                     ))
        self.assertTrue((self.game.onebattle.striker.speed >
                        self.game.onebattle.defender.speed)
                        or
                        (self.game.onebattle.striker.speed ==
                         self.game.onebattle.defender.speed
                         and
                         (self.game.onebattle.striker.luck >
                          self.game.onebattle.defender.luck)
                         )
                        )

    def test_battle_init(self):
        battle = self.game.onebattle
        self.assertEqual(battle.number_turns,0)
        print("battle.number_turns = {}".format(battle.number_turns))


    def test_has_rapid_strike(self):
        for i in range(1,21):
            print("step {0:}".format(i))
            self.game.onebattle.battle_flow()
            if self.game.orderus.number_attack % 10 == 0:
                self.assertTrue(self.game.orderus.has_rapid_strike())
            else:
                self.assertFalse(self.game.orderus.has_rapid_strike())
            print("Turn# {0:} Attacks = {1:} has rapid strike = {2:}".
                  format(self.game.onebattle.number_turns,
                         self.game.orderus.number_attack,
                         self.game.orderus.has_rapid_strike()
                     ))
    def test_has_magic_shield(self):
        for i in range(1,21):
            print("step {0:}".format(i))
            self.game.onebattle.battle_flow()
            if self.game.orderus.number_defend % 5 == 0:
                self.assertTrue(self.game.orderus.has_magic_shield())
            else:
                self.assertFalse(self.game.orderus.has_magic_shield())
            print("Turn# {0:} Defend = {1:} has magic shield = {2:}".
                  format(self.game.onebattle.number_turns,
                         self.game.orderus.number_defend,
                         self.game.orderus.has_magic_shield()
                     ))

    def test_has_points(self):
        for i in range(1,21):
            # print("step {0:}".format(i))
            self.game.onebattle.battle_flow()
            if self.game.orderus.number_defend % 5 == 0:
                self.assertTrue(self.game.orderus.has_magic_shield())
            else:
                self.assertFalse(self.game.orderus.has_magic_shield())
            print("Turn# {0:} striker: {5:}\n"
                  "\tDefend = {1:} has magic shield = {2:}\n"
                  "\tAttacks = {3:} has rapid strike = {4:}".
                  format(self.game.onebattle.number_turns,
                         self.game.orderus.number_defend,
                         self.game.orderus.has_magic_shield(),
                         self.game.orderus.number_attack,
                         self.game.orderus.has_rapid_strike(),
                         self.game.onebattle.striker.name
                     ))

    def test_fight(self):
        if self.game.onebattle.striker.name == "Orderus":
            print("Orderus will atack \n"
                  "(rapid strike = {0:} and defender has luck {1:})\n"
                  "defender health before fight {2:}"
                  .format(self.game.onebattle.striker.has_rapid_strike(),
                          self.game.onebattle.defender.has_luck(self.game.onebattle.number_turns),
                          self.game.onebattle.defender.health
                          ))
        else:
            print("Orderus will defend \n"
                  "(magic shield = {0:} and he has luck {1:})\n"
                  "defender health before fight {2:}"
                  .format(self.game.onebattle.defender.has_magic_shield(),
                          self.game.onebattle.defender.has_luck(self.game.onebattle.number_turns),
                          self.game.onebattle.defender.health
                          ))
        self.game.onebattle.fight()
        if self.game.onebattle.striker.name == "Orderus":
            print("Orderus atacked \n"
                  "(rapid strike = {0:} and defender had luck {1:})\n"
                  "defender health after fight {2:}\n"
                  "damage = {3:}"
                  .format(self.game.onebattle.striker.has_rapid_strike(),
                          self.game.onebattle.defender.has_luck(self.game.onebattle.number_turns),
                          self.game.onebattle.defender.health,
                          self.game.onebattle.damage
                          ))
        else:
            print("Orderus defended \n"
                  "(magic shield = {0:} and he had luck {1:})\n"
                  "defender health after fight {2:}\n"
                  "damage = {3:}"
                  .format(self.game.onebattle.defender.has_magic_shield(),
                          self.game.onebattle.defender.has_luck(self.game.onebattle.number_turns),
                          self.game.onebattle.defender.health,
                          self.game.onebattle.damage
                          ))


if __name__ == '__main__':
    unittest.main()
