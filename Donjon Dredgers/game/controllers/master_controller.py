from copy import deepcopy

from game.common.action import Action
from game.common.enums import *
from game.common.player import Player
import game.config as config
from game.utils.thread import CommunicationThread

from game.common.adventurer_types import *
from game.common.monster_types import *
from game.common.stats import GameStats
from game.controllers.controller import Controller


class MasterController(Controller):
    def __init__(self):
        super().__init__()
        self.game_over = False

        self.turn = None

        self.current_floor = 0
        self.current_monster = None

    # Receives all clients for the purpose of giving them the objects they will control
    def give_clients_objects(self, client):
        class_thread = CommunicationThread(client.code.set_adventurer_class, ())
        class_thread.start()
        class_thread.join(0.01)

        if class_thread.is_alive():
            client.functional = False
            client.error = TimeoutError('Client failed to provide a team name in time.')

        if class_thread.error is not None:
            client.functional = False
            client.error = class_thread.error

        chosen_class = class_thread.retrieve_value()

        adv = None
        if chosen_class == ClassType.knight:
            adv = Knight()
        elif chosen_class == ClassType.paladin:
            adv = Paladin()
        elif chosen_class == ClassType.barbarian:
            adv = Barbarian()

        client.adventurer = adv

    # Generator function. Given a key:value pair where the key is the identifier for the current world and the value is
    # the state of the world, returns the key that will give the appropriate world information
    def game_loop_logic(self, start=1):
        self.turn = start

        while True:
            self.turn += 1

            if self.current_monster is None:
                self.current_floor += 1

            if self.current_floor > GameStats.number_of_floors:
                break

            yield str(self.current_floor)

    # Receives world data from the generated game log and is responsible for interpreting it
    def interpret_current_turn_data(self, client, world, turn):
        if self.current_monster is None:
            mon = None
            if world == MonsterType.slime:
                mon = Slime()
            elif world == MonsterType.minotaur:
                mon = Minotaur()
            elif world == MonsterType.wisp:
                mon = Wisp()
            elif world == MonsterType.vampire:
                mon = Vampire()
            elif world == MonsterType.dragon:
                mon = Dragon()

            self.current_monster = mon

    # Receive a specific client and send them what they get per turn. Also obfuscates necessary objects.
    def client_turn_arguments(self, client, turn):
        actions = Action()
        client.action = actions

        # Create deep copies of all objects sent to the player
        adv_copy = deepcopy(client.adventurer)
        mon_copy = deepcopy(self.current_monster)

        # Obfuscate data in objects that that player should not be able to see
        adv_copy.obfuscate()
        mon_copy.obfuscate()

        args = (self.turn, self.current_floor, actions, adv_copy, mon_copy)
        return args

    # Perform the main logic that happens per turn
    def turn_logic(self, clients, turn):
        pass

    # Return serialized version of game
    def create_turn_log(self, client, turn):
        data = dict()

        data['current_floor'] = self.current_floor
        data['client'] = client.to_json()
        data['monster'] = self.current_monster.to_json()

        return data

    # Gather necessary data together in results file
    def return_final_results(self, client, turn):
        data = dict()

        data['client'] = client.to_json()
        data['score'] = self.current_floor

        return data
