from room import Room
from game_object import GameObject

class Game:
    attempts: int
    room: Room

    def __init__(self):
        self.attempts = 0
        self.room = Room(731, Game.create_objects())

    @staticmethod
    def create_objects():
        return [
            GameObject(
                'Sweater',
                '',
                '',
                ''
            ),
            GameObject(
                'Journal',
                '',
                '',
                ''
            ),
            GameObject(
                'Bowl of soup',
                '',
                '',
                ''
            ),
            GameObject(
                'Clock',
                '',
                '',
                ''
            )
        ]

    def get_room_prompt(self):
        prompt = 'Enter the 3-digit lock code or choose an item to interact with:\n'
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt

    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = input(prompt)
