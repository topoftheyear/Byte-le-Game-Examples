from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_name(self):
        return 'Team 2'

    def set_team(self):
        return [
            ClassType.tank,
            ClassType.paladin,
            ClassType.wizard,
            ClassType.mage,
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

        # Get teammate with lowest health
        lowest_health = None
        for character in my_team:
            if lowest_health is None:
                lowest_health = character

            if character.health < lowest_health.health:
                lowest_health = character

        # Paladin heals the lowest health character if health below 40, attacks otherwise
        if ClassType.paladin in my_team_dict and my_team_dict[ClassType.paladin].initiative == 10:
            paladin = my_team_dict[ClassType.paladin]
            if lowest_health.health < 40:
                actions.set_action(paladin, ActionType.skill, lowest_health)
            else:
                actions.set_action(paladin, ActionType.attack, target)

        # Wizard sets target on fire, attacks if already on fire
        if ClassType.wizard in my_team_dict and my_team_dict[ClassType.wizard].initiative == 10:
            wizard = my_team_dict[ClassType.wizard]
            if ClassType.wizard in [e.class_type for e in target.effects]:
                actions.set_action(wizard, ActionType.attack, target)
            else:
                actions.set_action(wizard, ActionType.skill, target)

        # Tank buffs character with lowest health, attacks otherwise
        if ClassType.tank in my_team_dict and my_team_dict[ClassType.tank].initiative == 10:
            tank = my_team_dict[ClassType.tank]
            if ClassType.tank in [e.class_type for e in lowest_health.effects]:
                actions.set_action(tank, ActionType.attack, target)
            else:
                actions.set_action(tank, ActionType.skill, lowest_health)

        # Mage boosts himself, attacks otherwise
        if ClassType.mage in my_team_dict and my_team_dict[ClassType.mage].initiative == 10:
            mage = my_team_dict[ClassType.mage]
            if ClassType.mage in [e.class_type for e in mage.effects]:
                actions.set_action(mage, ActionType.attack, target)
            else:
                actions.set_action(mage, ActionType.skill, mage)
