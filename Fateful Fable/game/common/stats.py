from game.common.enums import ClassType
from game.utils.singleton import Singleton


class GameStats(metaclass=Singleton):
    def __init__(self):
        self.health = {
            ClassType.warrior: 100,
            ClassType.rogue: 75,
            ClassType.tank: 150,
            ClassType.paladin: 125,
            ClassType.wizard: 80,
            ClassType.mage: 50,
            ClassType.sorcerer: 60,
            ClassType.priest: 75,
        }

        self.attack = {
            ClassType.warrior: 10,
            ClassType.rogue: 14,
            ClassType.tank: 6,
            ClassType.paladin: 6,
            ClassType.wizard: 10,
            ClassType.mage: 20,
            ClassType.sorcerer: 14,
            ClassType.priest: 8,
        }

        self.defense = {
            ClassType.warrior: 2,
            ClassType.rogue: 1,
            ClassType.tank: 3,
            ClassType.paladin: 1,
            ClassType.wizard: 0,
            ClassType.mage: 0,
            ClassType.sorcerer: 0,
            ClassType.priest: 1,
        }

        self.speed = {
            ClassType.warrior: 2,
            ClassType.rogue: 4,
            ClassType.tank: 1,
            ClassType.paladin: 2,
            ClassType.wizard: 2,
            ClassType.mage: 1,
            ClassType.sorcerer: 3,
            ClassType.priest: 2,
        }

        self.skill_strength = {
            ClassType.warrior: 1,
            ClassType.rogue: 2,
            ClassType.tank: 4,
            ClassType.paladin: 25,
            ClassType.wizard: 1,
            ClassType.mage: 1,
            ClassType.sorcerer: 1,
            ClassType.priest: 10,
        }

        self.skill_duration = {
            ClassType.warrior: 0,
            ClassType.rogue: 15,
            ClassType.tank: 15,
            ClassType.paladin: 0,
            ClassType.wizard: 20,
            ClassType.mage: 12,
            ClassType.sorcerer: 0,
            ClassType.priest: 0,
        }

        self.speed_for_turn = 10

        self.team_size = 4
