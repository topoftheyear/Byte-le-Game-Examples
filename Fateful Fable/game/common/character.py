from game.common.effect import Effect
from game.common.enums import ClassType, ObjectType
from game.common.game_object import GameObject
from game.common.stats import GameStats


class Character(GameObject):
    def __init__(self, class_type):
        super().__init__()
        self.object_type = ObjectType.character

        stats = GameStats()
        self.health = stats.health[class_type]
        self.class_type = class_type
        self.initiative = 0
        self.effects = list()

    def to_json(self):
        data = super().to_json()

        data['health'] = self.health
        data['class_type'] = self.class_type
        data['initiative'] = self.initiative
        data['effects'] = [e.to_json() for e in self.effects]

        return data

    def from_json(self, data):
        super().from_json(data)

        self.health = data['health']
        self.class_type = data['class_type']
        self.initiative = data['initiative']
        self.effects = [Effect().from_json(d) for d in self.effects]
