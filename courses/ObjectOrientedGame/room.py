from game_object import GameObject

class Room:
    escape_code: int
    game_objects: [GameObject]

    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        return code == self.escape_code

    @staticmethod
    def get_name(game_object):
        return game_object.name

    def get_game_object_names(self):
        return map(Room.get_name, self.game_objects)
