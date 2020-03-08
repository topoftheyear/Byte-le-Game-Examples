from game.common.enums import *
from game.common.stats import GameStats
from game.controllers.controller import Controller


class AttackController(Controller):
    def __init__(self):
        super().__init__()
        self.gs = GameStats()

    def handle_actions(self, clients):
        # Create basic list of all characters
        all_characters = list()
        for client in clients:
            all_characters += client.team

        # Find all attack actions
        for client in clients:
            acts = client.action._moves

            for act in acts.values():
                # Attack logic
                if act['action_type'] is ActionType.attack:
                    user = None
                    target = None
                    for character in all_characters:
                        if character.id == act['user']:
                            user = character
                        if character.id == act['target']:
                            target = character

                    # Quick stop loop if user or target is not found
                    if user is None or target is None:
                        continue

                    # Stop if the character's initiative isn't high enough
                    if user.initiative != self.gs.speed_for_turn:
                        continue

                    # Determine the defense of the target
                    defense = self.gs.defense[target.class_type]
                    # Check if the Tank's skill is in play
                    if ClassType.tank in [effect.class_type for effect in target.effects]:
                        defense += self.gs.skill_strength[ClassType.tank]

                    # Determine attack of the user
                    attack = self.gs.attack[user.class_type]
                    # Check if the Rogue's skill is in play
                    if ClassType.rogue in [effect.class_type for effect in target.effects]:
                        attack *= self.gs.skill_strength[ClassType.rogue]

                    damage = max(0, attack - defense)
                    target.health = max(0, target.health - damage)
                    user.initiative = 0
