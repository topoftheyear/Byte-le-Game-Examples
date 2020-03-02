from game.common.game_object import GameObject
from game.common.enums import ObjectType, MonsterType


class Monster(GameObject):
    def __init__(self):
        super().__init__()
        self.object_type = ObjectType.monster

        self.monster_type = MonsterType.none
        self.max_health = None
        self.health = None
        self.attack_damage = None
        self.attack_cooldown = None

    def to_json(self):
        data = super().to_json()

        data['class_type'] = self.monster_type
        data['max_health'] = self.max_health
        data['health'] = self.health
        data['attack_damage'] = self.attack_damage
        data['attack_cooldown'] = self.attack_cooldown

        return data

    def from_json(self, data):
        super().from_json(data)

        self.monster_type = data['class_type']
        self.max_health = data['max_health']
        self.health = data['health']
        self.attack_damage = data['attack_damage']
        self.attack_cooldown = data['attack_cooldown']
