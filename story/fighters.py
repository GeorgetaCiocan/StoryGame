import random

class Fighter():

    # number_turns = 0
    dranges = {
        'health': [],
        'strength': [],
        'defence': [],
        'speed': [],
        'luck': []
    }
    luck_probability = 1

    def __init__(self, name, dranges):
        self.name = name
        self.dranges = dranges
        self.get_rand_prop()

    def get_rand_prop(self) -> object:
        self.health = self.get_random(self.dranges['health'])
        self.strength = self.get_random(self.dranges['strength'])
        self.defence = self.get_random(self.dranges['defence'])
        self.speed = self.get_random(self.dranges['speed'])
        self.luck = self.get_random(self.dranges['luck'])


    def get_random(self, listval):
        return random.randrange(listval[0], listval[1])

    def get_luck_probability(self):
        self.luck_probability = int(100 / self.luck)

    def has_luck(self,number_turns):
        self.get_luck_probability()
        if number_turns % self.luck_probability == 0:
            return True
        return False


class Orderus(Fighter):
    number_attack = 0
    number_defend = 0

    def __init__(self, dranges):
        super().__init__("Orderus", dranges)

    def has_rapid_strike(self):
        if self.number_attack % 10 == 0:
            return True
        return False

    def has_magic_shield(self):
        if self.number_defend % 5 == 0:
            return True
        return False


class Beast(Fighter):

    def __init__(self, dranges):
        super().__init__("Beast", dranges)
