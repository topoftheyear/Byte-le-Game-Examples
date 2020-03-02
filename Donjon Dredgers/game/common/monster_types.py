from game.common.enums import MonsterType
from game.common.monster import Monster
from game.common.stats import GameStats


class Slime(Monster):
    def __init__(self):
        super().__init__()
        self.monster_type = MonsterType.slime

        self.max_health = GameStats.monster_max_health[self.monster_type]
        self.health = self.max_health
        self.attack_damage = GameStats.monster_attack[self.monster_type]
        self.attack_cooldown = 0


class Minotaur(Monster):
    def __init__(self):
        super().__init__()
        self.monster_type = MonsterType.minotaur

        self.max_health = GameStats.monster_max_health[self.monster_type]
        self.health = self.max_health
        self.attack_damage = GameStats.monster_attack[self.monster_type]
        self.attack_cooldown = 0


class Wisp(Monster):
    def __init__(self):
        super().__init__()
        self.monster_type = MonsterType.wisp

        self.max_health = GameStats.monster_max_health[self.monster_type]
        self.health = self.max_health
        self.attack_damage = GameStats.monster_attack[self.monster_type]
        self.attack_cooldown = 0


class Vampire(Monster):
    def __init__(self):
        super().__init__()
        self.monster_type = MonsterType.vampire

        self.max_health = GameStats.monster_max_health[self.monster_type]
        self.health = self.max_health
        self.attack_damage = GameStats.monster_attack[self.monster_type]
        self.attack_cooldown = 0


class Dragon(Monster):
    def __init__(self):
        super().__init__()
        self.monster_type = MonsterType.dragon

        self.max_health = GameStats.monster_max_health[self.monster_type]
        self.health = self.max_health
        self.attack_damage = GameStats.monster_attack[self.monster_type]
        self.attack_cooldown = 0
