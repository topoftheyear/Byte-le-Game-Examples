from game.common.enums import ClassType, ObjectType
from game.common.game_object import GameObject


class Effect(GameObject):
    def __init__(self, ctype=ClassType.none, time_remaining=0):
        super().__init__()
        self.object_type = ObjectType.effect

        self.class_type = ctype
        self.time_remaining = time_remaining
        self.action = None
        self.target = None

    def to_json(self):
        data = super().to_json()

        data['class_type'] = self.class_type
        data['time_remaining'] = self.time_remaining

        return data

    def from_json(self, data):
        super().from_json(data)

        self.class_type = data['class_type']
        self.time_remaining = data['time_remaining']

    def obfuscate(self):
        super().obfuscate()
        self.action = None
