class Weapon:
    # May add self.ability: stun - chance to lose a turn, freeze - chance frozen player takes damage when attacking, burn - chance burnt player takes
    # more damage when attacked.
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power