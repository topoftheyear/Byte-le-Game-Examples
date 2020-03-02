import random

from game.common.enums import MonsterType
from game.common.stats import GameStats
from game.config import *
from game.utils.helpers import write_json_file


def generate():
    print('Generating game map...')

    data = dict()

    monster_type_list = [MonsterType.slime,
                         MonsterType.minotaur,
                         MonsterType.wisp,
                         MonsterType.vampire,
                         MonsterType.dragon]
    for floor_number in range(1, GameStats.number_of_floors + 1):
        type_chosen = random.choice(monster_type_list)
        data[str(floor_number)] = type_chosen

    # Verify logs location exists
    if not os.path.exists(GAME_MAP_DIR):
        os.mkdir(GAME_MAP_DIR)

    # Write game map to file
    write_json_file(data, GAME_MAP_FILE)
