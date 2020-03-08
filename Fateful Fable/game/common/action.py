from game.common.character import Character
from game.common.enums import *


class Action:
    def __init__(self, team):
        self.object_type = ObjectType.action
        self._moves = dict()
        self._team_ids = [t.id for t in team]

    def set_action(self, user, action_type, target=None):
        if not isinstance(user, Character):
            return
        if action_type not in [ActionType.none, ActionType.attack, ActionType.skill]:
            return
        if target is not None and not isinstance(target, Character):
            return
        if user.id not in self._team_ids:
            return

        self._moves[user.id] = {
            'user': user.id,
            'action_type': action_type,
            'target': target.id if target is not None else None,
        }

    def to_json(self):
        data = dict()

        data['object_type'] = self.object_type
        data['moves'] = self._moves

        return data

    def from_json(self, data):
        self.object_type = data['object_type']
        self._moves = data['moves']

    def __str__(self):
        outstring = ''
        outstring += f'Moves: {self._moves.items()}\n'

        return outstring
