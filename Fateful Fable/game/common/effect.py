from game.common.enums import ClassType, ObjectType
from game.common.game_object import GameObject


class Effect(GameObject):
    def __init__(self, ctype=ClassType.none, activated=False, time_remaining=0):
        super().__init__()
        self.object_type = ObjectType.effect

        self.class_type = ctype
        self.activated = activated
        self.time_remaining = time_remaining

    def to_json(self):
        data = super().to_json()

        data['class_type'] = self.class_type
        data['activated'] = self.activated
        data['time_remaining'] = self.time_remaining

        return data

    def from_json(self, data):
        super().from_json(data)

        self.class_type = data['class_type']
        self.activated = data['activated']
        self.time_remaining = data['time_remaining']
