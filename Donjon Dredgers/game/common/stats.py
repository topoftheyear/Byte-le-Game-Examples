from game.common.enums import ClassType, MonsterType


class GameStats:
    adventurer_max_health = {
        ClassType.knight: 20,
        ClassType.paladin: 30,
        ClassType.barbarian: 15,
    }

    adventurer_attack_damage = {
        ClassType.knight: 3,
        ClassType.paladin: 2,
        ClassType.barbarian: 5,
    }

    adventurer_attack_cooldown = {
        ClassType.knight: 3,
        ClassType.paladin: 3,
        ClassType.barbarian: 2,
    }

    adventurer_heal_strength = {
        ClassType.knight: 5,
        ClassType.paladin: 10,
        ClassType.barbarian: 5,
    }

    adventurer_heal_cooldown = {
        ClassType.knight: 5,
        ClassType.paladin: 3,
        ClassType.barbarian: 5,
    }

    monster_max_health = {
        MonsterType.slime: 6,
        MonsterType.minotaur: 15,
        MonsterType.wisp: 6,
        MonsterType.vampire: 10,
        MonsterType.dragon: 20,
    }

    monster_attack = {
        MonsterType.slime: 1,
        MonsterType.minotaur: 3,
        MonsterType.wisp: 3,
        MonsterType.vampire: 4,
        MonsterType.dragon: 5,
    }

    monster_cooldown = {
        MonsterType.slime: 2,
        MonsterType.minotaur: 3,
        MonsterType.wisp: 2,
        MonsterType.vampire: 4,
        MonsterType.dragon: 4,
    }

    number_of_floors = 50
