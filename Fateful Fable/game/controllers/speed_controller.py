from game.common.enums import *
from game.common.stats import GameStats
from game.controllers.controller import Controller


class SpeedController(Controller):
    def __init__(self):
        super().__init__()
        self.gs = GameStats()

    def handle_actions(self, clients):
        # Create basic list of all characters
        all_characters = list()
        for client in clients:
            all_characters += client.team

        for character in all_characters:
            speed = self.gs.speed[character.class_type]
            # If mage skill on character, boost speed
            if ClassType.mage in [e.class_type for e in character.effects]:
                speed += self.gs.skill_strength[ClassType.mage]

            character.initiative = min(self.gs.speed_for_turn, character.initiative + speed)
