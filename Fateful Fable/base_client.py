from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_name(self):
        return 'Team 1'

    def set_team(self):
        return [
            ClassType.warrior,
            ClassType.rogue,
            ClassType.sorcerer,
            ClassType.priest,
        ]

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, my_team, enemy_team):
        my_team_dict = dict()
        for character in my_team:
            my_team_dict[character.class_type] = character

        # Pick a target
        target = None
        for character in enemy_team:
            if target is None:
                target = character
                continue

            if character.health < target.health:
                target = character

        # Priest action: heal if character needs healing, attack target otherwise
        if ClassType.priest in my_team_dict and my_team_dict[ClassType.priest].initiative == 10:
            priest = my_team_dict[ClassType.priest]
            for character in my_team:
                if character.health < 50:
                    actions.set_action(priest, ActionType.skill)
                    break
            else:
                actions.set_action(priest, ActionType.attack, target)

        # Warrior buffs eternally unless alone
        if ClassType.warrior in my_team_dict and my_team_dict[ClassType.warrior].initiative == 10:
            warrior = my_team_dict[ClassType.warrior]
            if len(my_team) == 1:
                actions.set_action(warrior, ActionType.attack, target)
            else:
                actions.set_action(warrior, ActionType.skill)

        # Rogue buffs himself then attacks
        if ClassType.rogue in my_team_dict and my_team_dict[ClassType.rogue].initiative == 10:
            rogue = my_team_dict[ClassType.rogue]
            if ClassType.rogue not in [e.class_type for e in my_team_dict[ClassType.rogue].effects]:
                actions.set_action(rogue, ActionType.skill, my_team_dict[ClassType.rogue])
            else:
                actions.set_action(rogue, ActionType.attack, target)

        # Sorcerer only attacks
        if ClassType.sorcerer in my_team_dict and my_team_dict[ClassType.sorcerer].initiative == 10:
            sorcerer = my_team_dict[ClassType.sorcerer]
            actions.set_action(sorcerer, ActionType.attack, target)
