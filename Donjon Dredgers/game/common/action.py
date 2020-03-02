from game.common.enums import *


class Action:
    def __init__(self):
        self.object_type = ObjectType.action
        self._chosen_action = ActionType.none

    def set_action(self, act):
        if act in [ActionType.none, ActionType.attack, ActionType.heal]:
            self._chosen_action = act

    def to_json(self):
        data = dict()

        data['object_type'] = self.object_type
        data['chosen_action'] = self._chosen_action

        return data

    def from_json(self, data):
        self.object_type = data['object_type']
        self._chosen_action = data['chosen_action']

    def __str__(self):
        outstring = ''

        outstring += f'Chosen Action: {self._chosen_action}'

        return outstring
