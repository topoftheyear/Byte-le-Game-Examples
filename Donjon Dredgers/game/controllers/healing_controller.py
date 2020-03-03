from game.common.enums import ActionType
from game.common.stats import GameStats
from game.controllers.controller import Controller


class HealingController(Controller):
    def handle_actions(self, client):
        if client.action._chosen_action is ActionType.heal:

            adventurer = client.adventurer
            if adventurer.heal_cooldown == 0:
                adventurer.health = min(adventurer.max_health, adventurer.health + adventurer.heal_strength)

                adventurer.heal_cooldown = GameStats.adventurer_heal_cooldown[adventurer.class_type]
