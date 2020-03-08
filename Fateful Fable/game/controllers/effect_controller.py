from game.common.effect import Effect
from game.common.enums import *
from game.common.stats import GameStats
from game.controllers.controller import Controller


class EffectController(Controller):
    def __init__(self):
        super().__init__()
        self.gs = GameStats()
        self.all_effects = list()

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
                if act['action_type'] is ActionType.skill:
                    user = None
                    target = None
                    for character in all_characters:
                        if character.id == act['user']:
                            user = character
                        if character.id == act['target']:
                            target = character

                    # Quick stop loop if user is not found
                    if user is None:
                        continue

                    # Stop loop if user didn't provide a target but class skill requires a target
                    require = [ClassType.rogue, ClassType.tank, ClassType.paladin, ClassType.wizard, ClassType.mage]
                    if user.class_type in require and target is None:
                        continue

                    # Stop if the character's initiative isn't high enough
                    if user.initiative != self.gs.speed_for_turn:
                        continue

                    effect = Effect(user.class_type)

                    effect.time_remaining = self.gs.skill_duration[user.class_type]

                    # Add the effect to the target
                    type_to_method = {
                        ClassType.warrior: self.warrior_skill,
                        ClassType.tank: self.tank_skill,
                        ClassType.paladin: self.paladin_skill,
                        ClassType.rogue: self.rogue_skill,
                        ClassType.wizard: self.wizard_skill,
                        ClassType.mage: self.mage_skill,
                        ClassType.sorcerer: self.sorcerer_skill,
                        ClassType.priest: self.priest_skill,
                    }
                    effect.action = type_to_method[user.class_type]

                    if user.class_type is ClassType.priest:
                        target = client.team

                    effect.target = target

                    # Add the effect to the list and character
                    if user.class_type in [ClassType.rogue, ClassType.tank, ClassType.wizard, ClassType.mage]:
                        target.effects.append(effect)
                    self.all_effects.append(effect)

                    user.initiative = 0

    def warrior_skill(self, target=None):
        self.gs.attack[ClassType.warrior] += 1
        self.gs.attack[ClassType.tank] += 1
        self.gs.attack[ClassType.paladin] += 1
        self.gs.attack[ClassType.rogue] += 1

    def rogue_skill(self, target=None):
        pass

    def tank_skill(self, target=None):
        pass

    def paladin_skill(self, target=None):
        target.health = min(self.gs.health[target.class_type],
                            target.health + self.gs.skill_strength[ClassType.paladin])

    def wizard_skill(self, target=None):
        target.health = max(0, target.health - self.gs.skill_strength[ClassType.wizard])

    def mage_skill(self, target=None):
        pass

    def sorcerer_skill(self, target=None):
        self.gs.defense[ClassType.wizard] += 1
        self.gs.defense[ClassType.mage] += 1
        self.gs.defense[ClassType.sorcerer] += 1
        self.gs.defense[ClassType.priest] += 1

    def priest_skill(self, target=None):
        for character in target:
            character.health = min(self.gs.health[character.class_type],
                                   character.health + self.gs.skill_strength[ClassType.priest])

    def perform_effects(self):
        for effect in self.all_effects:
            effect.action(effect.target)

    def handle_lifespan(self, clients):
        # Create basic list of all characters
        all_characters = list()
        for client in clients:
            all_characters += client.team

        for effect in self.all_effects:
            # Reduce lifespan of the attack
            effect.time_remaining -= 1

            if effect.time_remaining <= 0:
                # Remove the effect from the list and remove it from the character if on a character
                character = None
                for c in all_characters:
                    if effect in c.effects:
                        c.effects.remove(effect)
                        break

                self.all_effects.remove(effect)
