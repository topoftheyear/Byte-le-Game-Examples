from game.common.adventurer import Adventurer
from game.common.enums import ClassType
from game.common.stats import GameStats


class Knight(Adventurer):
    def __init__(self):
        super().__init__()
        self.class_type = ClassType.knight

        self.max_health = GameStats.adventurer_max_health[self.class_type]
        self.health = self.max_health
        self.attack_damage = GameStats.adventurer_attack_damage[self.class_type]
        self.attack_cooldown = 0
        self.heal_strength = GameStats.adventurer_heal_strength[self.class_type]
        self.heal_cooldown = 0


class Paladin(Adventurer):
    def __init__(self):
        super().__init__()
        self.class_type = ClassType.paladin

        self.max_health = GameStats.adventurer_max_health[self.class_type]
        self.health = self.max_health
        self.attack_damage = GameStats.adventurer_attack_damage[self.class_type]
        self.attack_cooldown = 0
        self.heal_strength = GameStats.adventurer_heal_strength[self.class_type]
        self.heal_cooldown = 0


class Barbarian(Adventurer):
    def __init__(self):
        super().__init__()
        self.class_type = ClassType.barbarian

        self.max_health = GameStats.adventurer_max_health[self.class_type]
        self.health = self.max_health
        self.attack_damage = GameStats.adventurer_attack_damage[self.class_type]
        self.attack_cooldown = 0
        self.heal_strength = GameStats.adventurer_heal_strength[self.class_type]
        self.heal_cooldown = 0
