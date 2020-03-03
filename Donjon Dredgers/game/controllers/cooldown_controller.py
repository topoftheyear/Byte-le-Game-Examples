from game.controllers.controller import Controller


class CooldownController(Controller):
    def handle_actions(self, client, monster):
        adventurer = client.adventurer
        adventurer.attack_cooldown = max(0, adventurer.attack_cooldown - 1)
        adventurer.heal_cooldown = max(0, adventurer.heal_cooldown - 1)

        monster.attack_cooldown = max(0, monster.attack_cooldown - 1)
