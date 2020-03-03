from game.common.enums import ActionType
from game.common.stats import GameStats
from game.controllers.controller import Controller


class AttackController(Controller):
    def handle_actions(self, client, monster):
        adventurer = client.adventurer

        if client.action._chosen_action is ActionType.attack:
            if adventurer.attack_cooldown == 0:
                monster.health = max(0, monster.health - adventurer.attack_damage)

                adventurer.attack_cooldown = GameStats.adventurer_attack_cooldown[adventurer.class_type]

        if monster.attack_cooldown == 0:
            adventurer.health = max(0, adventurer.health - monster.attack_damage)

            monster.attack_cooldown = GameStats.monster_cooldown[monster.monster_type]
