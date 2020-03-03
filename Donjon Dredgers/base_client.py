from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_name(self):
        return 'Paladin'
        
    def set_adventurer_class(self):
        return ClassType.paladin

    # This is where your AI will decide what to do
    def take_turn(self, turn, floor, actions, adventurer, monster):
        if adventurer.attack_cooldown == 0:
            actions.set_action(ActionType.attack)

        if adventurer.heal_cooldown == 0 and adventurer.health < adventurer.max_health - adventurer.heal_strength:
            actions.set_action(ActionType.heal)
