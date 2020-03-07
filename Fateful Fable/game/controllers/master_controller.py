from copy import deepcopy

from game.common.action import Action
from game.common.enums import *
from game.common.player import Player
import game.config as config
from game.utils.thread import CommunicationThread

from game.common.character import Character
from game.common.stats import GameStats
from game.controllers.controller import Controller


class MasterController(Controller):
    def __init__(self):
        super().__init__()
        self.game_over = False

        self.turn = None
        self.game_stats = GameStats()
        self.players = list()

    # Receives all clients for the purpose of giving them the objects they will control
    def give_clients_objects(self, clients):
        self.players = clients

        for client in clients:
            thr = CommunicationThread(client.code.set_team, (), list)
            thr.start()
            thr.join(0.01)

            if thr.is_alive():
                client.functional = False
                client.error = TimeoutError('Client failed to provide a team in time.')
                continue

            if thr.error is not None:
                client.functional = False
                client.error = thr.error
                continue

            team = thr.retrieve_value()

            if len(team) != self.game_stats.team_size:
                client.functional = False
                client.error = ValueError('Client provided an incorrect number of team members.')
                continue

            for ctype in team:
                if ctype not in [ClassType.warrior, ClassType.rogue, ClassType.tank, ClassType.paladin,
                                 ClassType.wizard, ClassType.mage, ClassType.sorcerer, ClassType.priest]:
                    client.functional = False
                    client.error = TypeError('Client provided unaccepted type when building team.')
                    break

                client.team.append(Character(ctype))

    # Generator function. Given a key:value pair where the key is the identifier for the current world and the value is
    # the state of the world, returns the key that will give the appropriate world information
    def game_loop_logic(self, start=1):
        self.turn = start

        while True:
            yield 'world'
            self.turn += 1

    # Receives world data from the generated game log and is responsible for interpreting it
    def interpret_current_turn_data(self, clients, world, turn):
        pass

    # Receive a specific client and send them what they get per turn. Also obfuscates necessary objects.
    def client_turn_arguments(self, client, turn):
        actions = Action()
        client.action = actions

        opponent = None
        for player in self.players:
            if player.id != client.id:
                opponent = player
                break

        # Create deep copies of all objects sent to the player
        my_team = [deepcopy(c) for c in client.team]
        opponent_team = [deepcopy(c) for c in opponent.team]

        # Obfuscate data in objects that that player should not be able to see
        my_team = [c.obfuscate() for c in my_team]
        opponent_team = [c.obfuscate() for c in opponent_team]

        args = (self.turn, actions, my_team, opponent_team)
        return args

    # Perform the main logic that happens per turn
    def turn_logic(self, clients, turn):
        pass

    # Return serialized version of game
    def create_turn_log(self, clients, turn):
        data = dict()

        # Add things that should be thrown into the turn logs here
        data['players'] = list()
        for client in clients:
            data['players'].append(client.to_json())

        return data

    # Gather necessary data together in results file
    def return_final_results(self, clients, turn):
        # Determine scores
        scores = dict()
        client1, client2 = clients
        if len(client1.team) > 1 and len(client2.team) > 1 or len(client1.team) == 0 and len(client2.team) == 0:
            scores[client1.id] = 1
            scores[client2.id] = 1
        elif len(client1.team) == 0:
            scores[client1.id] = 0
            scores[client2.id] = 3
        elif len(client2.team) == 0:
            scores[client1.id] = 3
            scores[client2.id] = 0

        data = dict()

        data['players'] = list()
        # Determine results
        for client in clients:
            d = {
                'id': client.id,
                'team_name': client.team_name,
                'score': scores[client.id]
            }
            data['players'].append(d)

        return data
